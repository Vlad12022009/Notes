from django.shortcuts import render, redirect
from .models import Notes
from .forms import NotesForm
from django.views import View
# Create your views here.

def notes_view_all(request):
    return notes_view(request)

def notes_view(request, category=None):
    if category == None:
        qs = Notes.objects.all()
    else:
        qs = Notes.objects.filter(category=category)
    return render(request, 'Notes/index_notes.html', {'all_notes': qs, 'Category': category, 'status_form': False})

class Create_notes(View):
    def get(self, request, category=None):
        if category == None:
            qs = Notes.objects.all()
        else:
            qs = Notes.objects.filter(category=category)

        form = NotesForm()
        return render(request, 'Notes/index_notes.html', {'all_notes': qs, 'Category': category, 'form': form, 'status_form': True})
    
    def post(self, request, category=None):
        if category == None:
            qs = Notes.objects.all()
        else:
            qs = Notes.objects.filter(category=category)

        form = NotesForm(request.POST)
        if form.is_valid():
            article = form.cleaned_data.get('article')
            body = form.cleaned_data.get('body')
            category_form = form.cleaned_data.get('category')
            obj = Notes.objects.create(article=article, body=body, category=category_form)
            obj.save()
        
        return redirect('/') if category == None else redirect(f"/category/{category}/")


def delete_note(request, pk):
    Notes.objects.get(id=pk).delete()
    return redirect("/")

def done_or_not_notes(request, pk, category=None):
    obj = Notes.objects.get(id=pk)
    obj.done = True if obj.done == False else False
    obj.save()
    return redirect('/') if category == None else redirect(f"/category/{category}/")