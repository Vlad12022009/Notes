from django import forms

class NotesForm(forms.Form):
    article = forms.CharField(max_length=100, label='Задача')
    body = forms.CharField(required=False, label='Описание', widget=forms.Textarea, max_length=1000)
    category = forms.ChoiceField(required=False, choices=(
                ('Работа', 'Работа'),
                ('Семья', 'Семья'),
                ('Личное', 'Личное'),
                ('Дом', 'Дом'),
                ('Здоровье', 'Здоровье'),
                ('Деньги', 'Деньги'),
                ('Другое', 'Другое')
                ), label='Категория')