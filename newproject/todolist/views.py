from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar

#importing forms
from todolist.form import UserTaskForm
from todolist.form import AssignedTaskDescForm
from todolist.form import UserNoteForm
from todolist.form import PersonalTaskForm

#importing models
from todolist.models import UserNote

# Create your views here.
def index(request, year=date.today().year, month=date.today().month):
    year = int(year)

    if year < 1999 and year > 2099:
        year = date.today().year

    month_name = calendar.month_name[month]

    cal = HTMLCalendar().formatmonth(year, month)    

    title = "Current month: " + month_name #demo
    data = {'demo':title, 'year':year, 'cal':cal} 
    return render(request, "base.html", data )

def user_task(request):
    userTask = UserTaskForm
    return render(request, "index.html", {'form':userTask})


def user_task_post(request):
    task_title = request.POST['task_title']
    task_description = request.POST['task_description']
    task_assigned_at = request.POST['task_assigned_at']
    task_accomplish_date = request.POST['task_accomplish_date']
    task_assigned_by = request.POST['task_assigned_by']
    task_progress_status = request.POST['task_progress_status']
    task_assigned_to = request.POST['task_assigned_to']

    request_data = {
        'task_title' : task_title,
        'task_description' : task_description,
        'task_assigned_at' : task_assigned_at,
        'task_accomplish_date' : task_accomplish_date,
        'task_assigned_by' : task_assigned_by,
        'task_progress_status' : task_progress_status,
        'task_assigned_to' : task_assigned_to,
    }
    return render(request, "base.html", {'data': request_data})  


def assigned_task_desc(request):
    assign = AssignedTaskDescForm
    return render(request, 'index.html', {'form':assign })

def personal_task(request):
    personal = PersonalTaskForm
    return render(request, 'personal_task.html', {'form': personal})

def personal_task_post(request):
    personal = PersonalTaskForm
    request_data = {
        'form' : PersonalTaskForm,
        'task_title' : request.GET['task_title'],
        'task_description' :  request.GET['task_description'],
        'task_assigned_at' :  request.GET['task_assigned_at'],
        'task_accomplish_date' :  request.GET['task_accomplish_date'],
        'task_progress_status' :  request.GET['task_progress_status'],
    }
    return render(request, "personal_task.html", request_data)




def user_note(request):
    note = UserNoteForm
    return render(request, 'note.html', {'form': note})


def user_note_add(request):
    template = 'note.html'
    # filtering request method
    if request.method == "POST":
        # filtering request data
        title = request.POST.get('note_title')
        description = request.POST.get('note_description')
        added_at = request.POST.get('note_added_at')
        
        # creating object of model
        un = UserNote(note_title=title, note_description=description, note_added_at=added_at)
        un.save()
        # creating object of form
        note = UserNoteForm
        
        # success message
        msg = "Success"

        # sending response to request
        return render(request, template, {'form': note, 'msg': msg, 'data': un})
    else:
        note = UserNoteForm
        msg = "Fail"
        return render(request, template, {'form': note, 'msg': msg}) 



#loads the note index page 
def note(request):
    note = UserNoteForm
    return render(request, 'note.html', {'form': note}) 

#stores the note data to database
def note_add(request):
    template = 'note.html'
    # filtering request method
    if request.method == "POST":
        # filtering request data
        title = request.POST.get('note_title')
        description = request.POST.get('note_description')
        added_at = request.POST.get('note_added_at')
        
        # creating object of model
        un = UserNote(note_title=title, note_description=description, note_added_at=added_at)
        un.save()
        # creating object of form
        note = UserNoteForm
        
        # success message
        msg = "Success"

        # sending response to request
        return render(request, template, {'form': note, 'msg': msg, 'data': un})
    else:
        note = UserNoteForm
        msg = "Fail"
        return render(request, template, {'form': note, 'msg': msg}) 





def custom(request):
    return HttpResponse("<html><body>This is custom page</body></html>")
