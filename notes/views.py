from django.shortcuts import render, redirect
from .models import Notes
from .forms import NotesForm
from django.views import View
from django.http import JsonResponse
# Create your views here.

class Notes_view(View):
    def get(self, request, category=None):
        if category == None:
            qs = Notes.objects.all() 
        else:
            qs = Notes.objects.filter(category=category) 

        form = NotesForm()
        return render(request, 'Notes/index_notes.html', {'all_notes': qs, 'Category': category, 'form': form})
    
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
    response = {
        'delete_status': True
    }
    return JsonResponse(response)

def done_or_not_notes(request, pk):
    obj = Notes.objects.get(id=pk)
    obj.done = True if obj.done == False else False
    obj.save()
    response = {
        'boolean': obj.done
    }
    return JsonResponse(response)

