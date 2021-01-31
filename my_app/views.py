from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import date

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User , auth

from .forms import CreateStudentForm
from .models import teacher, Student, Attendence
from .filters import AttendenceFilter, StudentFilter


# Create your views here.





def home(request):

  if request.method == 'GET':
        
      if request.user.is_authenticated:
        if request.user.is_superuser:
          return render(request, 'admin/admin_ui/admin_ui.html')
        elif request.user.teacher:
          return render(request, 'teacher/teacher_ui/profile.html')
      else :
        return render(request,'homepage/index.html')



   

       


def admin_ui(request):

    if request.method == 'GET':

      if request.user.is_authenticated:

        auser = request.user

        return render(request,'admin/admin_ui/admin_ui.html' , {"auser":auser})

      else :
        return redirect('home')


def teacher_ui(request):
    if request.method == 'GET':

      teacherid = request.session['teacherusername']
      duser = User.objects.get(username=teacherid)

    
      #return render(request,'teacher/teacher_ui/profile.html',{"duser":duser})
    studentForm = CreateStudentForm()

    if request.method == 'POST':
      studentForm = CreateStudentForm(data = request.POST, files=request.FILES)
      # print(request.POST)
      stat = False 
      try:
        student = Student.objects.get(registration_id = request.POST['registration_id'])
        stat = True
      except:
        stat = False
      if studentForm.is_valid() and (stat == False):
        studentForm.save()
        name = studentForm.cleaned_data.get('firstname') +" " +studentForm.cleaned_data.get('lastname')
        messages.success(request, 'Student ' + name + ' was successfully added.')
        return redirect('teacher_ui')
      else:
        messages.error(request, 'Student with Registration Id '+request.POST['registration_id']+' already exists.')
        return redirect('teacher_ui')

    context = {'studentForm':studentForm, "duser":duser}
    return render(request, 'teacher/teacher_ui/profile.html', context)


      


def dviewprofile(request, teacherusername):

    if request.method == 'GET':
      duser = User.objects.get(username=teacherusername)
      return render(request,'teacher/view_profile/view_profile.html', {"duser":duser})



def searchAttandance(request):
  if request.method == 'GET':
    attendences = Attendence.objects.all()
    myFilter = AttendenceFilter(request.GET, queryset=attendences)
    attendences = myFilter.qs
    context = {'myFilter':myFilter, 'attendences': attendences, 'ta':False}
    return render(request, 'student/student_ui.html', context)



def card(request):
  if request.method == 'GET':
    students = Student.objects.all()
    myStudentFilter = StudentFilter(request.GET, queryset=students)
    students = myStudentFilter.qs
    context = {'myStudentFilter':myStudentFilter, 'students': students}
    return render(request, 'id/id_card.html', context)


def takeAttendence(request):
  if request.method == 'POST':
    details = {
      'branch':request.POST['branch'],
      'year': request.POST['year'],
      'section':request.POST['section'],
      'period':request.POST['period'],
       #'faculty':request.user.faculty
      }
    if Attendence.objects.filter(date=str(date.today()),branch=details['branch'],year=details['year'],section=details['section'],period=details['period']).count()!=0:
      messages.error(request, "Attendence already recorded.")
      return redirect('home')
    else:
      students = Student.objects.filter(branch = details['branch'], year = details['year'], section = details['section'])
      names = Recognizer(details)
      for student in students:
        if str(student.registration_id) in names:
         #attendence = Attendence(Faculty_Name = request.user.faculty, 
          Student_ID = str(student.registration_id), 
          period = details['period'], 
          branch = details['branch'], 
          year = details['year'], 
          section = details['section'],
          status = 'Present'
          attendence.save()
        else:
          #attendence = Attendence(Faculty_Name = request.user.faculty, 
          Student_ID = str(student.registration_id), 
          period = details['period'],
          branch = details['branch'], 
          year = details['year'], 
          section = details['section']
          attendence.save()
      attendences = Attendence.objects.filter(date = str(date.today()),branch = details['branch'], year = details['year'], section = details['section'],period = details['period'])
      context = {"attendences":attendences, "ta":True}
      messages.success(request, "Attendence taking Success")
      return render(request, 'student/student_ui.html', context)        
  context = {}
  return render(request, 'teacher/teacher_ui/profile.html', context)