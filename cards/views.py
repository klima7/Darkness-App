from io import BytesIO

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from .services import create_flashcards
from core.models import Pair

def generate_test_pdf(request):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    
    pairs = Pair.objects.select_related(
        'first__face',
        'first__face__color',
        'second__face',
        'second__face__color',
        'best'
    )
    
    sample_cards = [
        {
            "first": pair.first.char.upper(),
            "second": pair.second.char.upper(),
            "word": pair.best.word,
            "first_color": pair.first.face.color.normalized_tuple,
            "second_color": pair.second.face.color.normalized_tuple
        }
        for pair in pairs
    ]
    create_flashcards(p, sample_cards)
    
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="test.pdf"'
    response.write(pdf)
    return response
