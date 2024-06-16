from django import forms

class NotesForm(forms.Form):
    article = forms.CharField(max_length=100)
    body = forms.CharField(required=False)
    category = forms.ChoiceField(required=False, choices=(
                ('Работа', 'Работа'),
                ('Семья', 'Семья'),
                ('Личное', 'Личное'),
                ('Дом', 'Дом'),
                ('Здоровье', 'Здоровье'),
                ('Деньги', 'Деньги'),
                ('Другое', 'Другое')
                ))