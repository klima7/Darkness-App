from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import black, white, gray, Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def draw_grid(c, width, height, card_width, card_height, edge_gap):
    """Draw the grid lines for the cards."""
    c.setStrokeColor(gray)
    
    # Vertical lines
    for i in range(1, 4):
        c.line(i * card_width, edge_gap, i * card_width, height - edge_gap)
        
    # Horizontal lines
    for i in range(1, 8):
        c.line(edge_gap, i * card_height, width - edge_gap, i * card_height)

def draw_card_front(c, card, x, y, card_width, card_height, edge_gap, strip_height, font_name):
    """Draw a single card front."""
    # Draw colored strip at the top
    first_color = card.get('first_color', (1, 1, 1))
    second_color = card.get('second_color', (1, 1, 1))
    
    # Draw first half of the strip
    c.setFillColor(Color(*first_color))
    c.rect(x + edge_gap, y + card_height - strip_height - edge_gap, 
           card_width/2 - edge_gap, strip_height, fill=1, stroke=0)
    
    # Draw second half of the strip
    c.setFillColor(Color(*second_color))
    c.rect(x + card_width/2, y + card_height - strip_height - edge_gap, 
           card_width/2 - edge_gap, strip_height, fill=1, stroke=0)
    
    # Add front content
    c.setFont(font_name, 50)
    c.setFillColor(black)
    text_x = x + (card_width / 2)
    
    font_size = 50
    descent = font_size * 0.25
    text_y = y + edge_gap + descent
    
    first = card.get('first', '')
    second = card.get('second', '')
    combined_text = f"{first}{second}"
    c.drawCentredString(text_x, text_y, combined_text)

def transform_word(word, first_letter, second_letter):
    """
    Transform a word by capitalizing the first occurrence of first_letter and
    the first occurrence of second_letter after the first_letter's position.
    If letter is 'u', also searches for 'ó' and vice versa.
    
    Args:
        word (str): The word to transform
        first_letter (str): The first letter to capitalize
        second_letter (str): The second letter to capitalize (after first_letter)
    
    Returns:
        str: The transformed word with appropriate letters capitalized
    """
    word = word.lower()
    first_letter = first_letter.lower()
    second_letter = second_letter.lower()
    
    # Helper function to find first occurrence of letter or its variant
    def find_letter_pos(text, letter):
        pos = text.find(letter)
        if letter == 'u':
            pos_alt = text.find('ó')
            if pos == -1 or (pos_alt != -1 and pos_alt < pos):
                return pos_alt
        elif letter == 'ó':
            pos_alt = text.find('u')
            if pos == -1 or (pos_alt != -1 and pos_alt < pos):
                return pos_alt
        return pos
    
    # Helper function to get the actual letter at position
    def get_letter_at_pos(text, pos, letter):
        if letter == 'u' and text[pos] == 'ó':
            return 'Ó'
        elif letter == 'ó' and text[pos] == 'u':
            return 'U'
        return letter.upper()
    
    # Find first occurrence of first letter
    first_pos = find_letter_pos(word, first_letter)
    if first_pos != -1:
        first_upper = get_letter_at_pos(word, first_pos, first_letter)
        word = word[:first_pos] + first_upper + word[first_pos + 1:]
        
        # Find first occurrence of second letter after first_pos
        second_pos = find_letter_pos(word[first_pos + 1:], second_letter)
        if second_pos != -1:
            second_pos += first_pos + 1  # Adjust position to account for substring
            second_upper = get_letter_at_pos(word, second_pos, second_letter)
            word = word[:second_pos] + second_upper + word[second_pos + 1:]
    
    return word

def draw_card_back(c, card, x, y, card_width, card_height, font_name):
    """Draw a single card back."""
    c.setFont(font_name, 25)
    c.setFillColor(black)
    text_x = x + (card_width / 2)
    
    font_size = 25
    descent = font_size * 0.25
    text_y = y + (card_height / 2) - descent
    
    word = card.get('word', '')
    first_letter = card.get('first', '')
    second_letter = card.get('second', '')
    
    transformed_word = transform_word(word, first_letter, second_letter)
    c.drawCentredString(text_x, text_y, transformed_word)

def create_flashcards(c, cards_data, cards_per_page=32):
    """
    Create a PDF with flashcards from a list of dictionaries.
    
    Args:
        cards_data (list): List of dictionaries with 'first', 'second', 'word', 'first_color', and 'second_color' keys
        output_filename (str): Name of the output PDF file
        cards_per_page (int): Number of cards per page (default: 32)
    
    Returns:
        str: Path to the created PDF file
    """
    pdfmetrics.registerFont(TTFont('DejaVuSans', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
    font_name = 'DejaVuSans'
    
    width, height = A4
    
    # Calculate card dimensions without margins
    margin = 0
    card_width = width / 4  # 4 cards horizontally
    card_height = height / 8  # 8 cards vertically
    
    # Define the gap at edges (0.5 cm in points)
    edge_gap = 0.5 * 28.35  # 1 cm ≈ 28.35 points
    
    # Define the height of the colored strip (1/6 of card height)
    strip_height = card_height / 6
    
    # Process cards in batches of cards_per_page
    total_pages = (len(cards_data) + cards_per_page - 1) // cards_per_page
    
    for page in range(total_pages):
        # Get the batch of cards for this page
        start_idx = page * cards_per_page
        end_idx = min(start_idx + cards_per_page, len(cards_data))
        page_cards = cards_data[start_idx:end_idx]
        
        # Create front page
        draw_grid(c, width, height, card_width, card_height, edge_gap)
        
        # Draw front of each card
        for i, card in enumerate(page_cards):
            row = i // 4
            col = i % 4
            x = col * card_width
            y = height - ((row + 1) * card_height)
            draw_card_front(c, card, x, y, card_width, card_height, edge_gap, strip_height, font_name)
        
        # Move to next page for backs of this batch
        c.showPage()
        
        # Create back page for this batch
        draw_grid(c, width, height, card_width, card_height, edge_gap)
        
        # Draw back of each card
        for i, card in enumerate(page_cards):
            row = 7 - (i // 4)
            col = i % 4
            x = col * card_width
            y = height - ((row + 1) * card_height)
            draw_card_back(c, card, x, y, card_width, card_height, font_name)
        
        # Move to next page for next batch's fronts (if any)
        if page < total_pages - 1:
            c.showPage()
