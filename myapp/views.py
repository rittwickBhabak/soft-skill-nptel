from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponseForbidden
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Lesson


class Home(ListView):
    model = Lesson

class LessonDetail(DetailView):
    model = Lesson

class CreateLesson(CreateView):
    model = Lesson

def detail_update_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    next = Lesson.objects.filter(pk__gt=pk).order_by('pk').first()
    prev = Lesson.objects.filter(pk__lt=pk).order_by('-pk').first()
    return render(request, 'myapp/lesson_detail.html', context={'lesson': lesson, 'next': next, 'prev': prev})

def save_notes(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    lesson.detail = request.POST.get('notes')
    print(lesson.pk)
    print(request.POST.get('notes'))
    lesson.save()
    return JsonResponse({"status": 'Success'}) 

class NoteList(ListView):
    model = Lesson 
    template_name= 'myapp/note_list.html'



def mark_completed(request, pk):
    if request.method == 'POST':
        lesson = get_object_or_404(Lesson, pk=pk)
        lesson.is_completed = not lesson.is_completed
        lesson.save() 
        return JsonResponse({"status": "success"})
    return HttpResponseForbidden("Not Allowed")