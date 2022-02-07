from django.urls import path
from . import views 

app_name = 'myapp'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('lesson/<int:pk>', views.detail_update_lesson, name='lesson'),
    path('save-notes/<int:pk>', views.save_notes, name='save-notes'),
    path('notes/', views.NoteList.as_view(), name="notes"),
    path('mark-completed/<int:pk>', views.mark_completed, name='mark-completed'),

]
