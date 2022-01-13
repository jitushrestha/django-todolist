from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('task-create/', views.user_task, name="task.create"),
    path('task-create/task-post/', views.user_task_post, name="task.post"),
    path('task-assign/', views.assigned_task_desc, name="task.assign"),
    path('task-personal/', views.personal_task, name="task.personal"),
    path('task-personal/task-post/', views.personal_task_post, name="task.personal.post"),
    path('user-note/', views.user_note, name="user.note"),
    path('user-note-add/', views.user_note_add, name="user.note.add"),
    path('custom-index/', views.custom, name="custom"),



    path('note/', views.note, name="note.index"),
    path('note-add/', views.note_add, name="note.add"),
]