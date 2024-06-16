from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Notes
from django.test import Client

c = Client()

User = get_user_model()

class NotesTest(TestCase):
    def setUp(self):
        n1 = Notes.objects.create(
            article='Test 1',
            body='body',
            category='Работа')
        n2 = Notes.objects.create(
            article='Test 2',
            body='body',
            category='Семья')
    
    def test_notes_count(self):
        notes_count = Notes.objects.count()
        self.assertEqual(notes_count, 2)
    
    def test_notes_delete(self):
        response = c.get('/delete/2/', follow=True)
        redirect_path = response.request.get("PATH_INFO")
        self.assertEqual(redirect_path, "/")
        self.assertEqual(response.status_code, 200)
