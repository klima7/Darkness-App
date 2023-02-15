# Generated by Django 4.1.7 on 2023-02-15 15:34

import json

from django.db import migrations


def import_data(apps, schema_editor):
    Pair = apps.get_model('core', 'Pair')
    Word = apps.get_model('core', 'Word')

    with open('data.json') as f:
        data = json.load(f)

    for pair_letters, pair_data in data.items():
        pair = Pair(first=pair_letters[0], second=pair_letters[1])
        pair.save()

        for word_text in pair_data['all']:
            if 'brak' in word_text:
                continue

            fixed_text = word_text
            description = None

            if '(' in word_text and ')' in word_text:
                index = word_text.index('(')
                description = word_text[index+1:-1]
                fixed_text = word_text[:index]

            word = Word(pair=pair, word=fixed_text, description=description)
            word.save()

            if word_text == pair_data['best']:
                pair.best = word
                pair.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_data),
    ]
