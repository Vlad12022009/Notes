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
    return render(request, 'Notes/index_notes.html', {'all_notes': qs, 'Category': category})

class Create_notes(View):
    def get(self, request):
        form = NotesForm()
        return render(request, 'Notes/form_notes.html', {'form':form})
    
    def post(self, request):
        form = NotesForm(request.POST)
        if form.is_valid():
            article = form.cleaned_data.get('article')
            body = form.cleaned_data.get('body')
            category = form.cleaned_data.get('category')
            obj = Notes.objects.create(article=article, body=body, category=category)
            obj.save()
        return redirect("/")

def delete_note(request, pk):
    Notes.objects.get(id=pk).delete()
    return redirect("/")

def done_or_not_notes(self, pk, category=None):
    obj = Notes.objects.get(id=pk)
    obj.done = True if obj.done == False else False
    obj.save()
    if category == None:
        return redirect("/")
    else:
        return redirect(f"/category/{category}")
    