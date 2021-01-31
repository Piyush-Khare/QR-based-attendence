from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages
from django.contrib.auth.models import User , auth
from my_app.models import teacher
from datetime import datetime

# Create your views here.


   
def logout(request):
    auth.logout(request)
    request.session.pop('teacherid', None)
    request.session.pop('adminid', None)
    return render(request,'homepage/index.html')




def sign_in_admin(request):

    if request.method == 'POST':

          username =  request.POST.get('username')
          password =  request.POST.get('password')
 
          user = auth.authenticate(username=username,password=password)

          if user is not None :
             
              try:
                if ( user.is_superuser == True ) :
                  auth.login(request,user)

                  return redirect('admin_ui')
                else:
                  messages.info(request,'Please enter the correct username and password for a admin account.')
                  return redirect('sign_in_admin')
              except :
                  messages.info(request,'Please enter the correct username and password for a admin account.')
                  return redirect('sign_in_admin')
          else :
             messages.info(request,'Please enter the correct username and password for a admin account.')
             return redirect('sign_in_admin')


    else :
      return render(request,'admin/signin/signin.html')




#teachers account...........operations......
    

def signup_teacher(request):

    if request.method == 'GET':
    
       return render(request,'teacher/signup_Form/signup.html')


    if request.method == 'POST':
      
      if request.POST['username'] and request.POST['email'] and  request.POST['name'] and request.POST['gender'] and request.POST['mobile'] and request.POST['password'] and request.POST['password1'] and request.POST['department'] :

          username =  request.POST['username']
          email =  request.POST['email']

          name =  request.POST['name']
         
          gender =  request.POST['gender']
          
          mobile_no = request.POST['mobile']
          
          department =  request.POST['department']
          
          password =  request.POST.get('password')
          password1 =  request.POST.get('password1')

          if password == password1:
              if User.objects.filter(username = username).exists():
                messages.info(request,'username already taken')
                return redirect('signup_teacher')

              elif User.objects.filter(email = email).exists():
                messages.info(request,'email already taken')
                return redirect('signup_teacher')
                
              else :
                user = User.objects.create_user(username=username,password=password,email=email)   
                user.save()
                
                teachernew = teacher( user=user, name=name,  gender=gender, mobile_no=mobile_no, department=department)
                teachernew.save()
                messages.info(request,'user created sucessfully')
                print("teachercreated")
                
              return redirect('sign_in_teacher')

          else:
            messages.info(request,'password not matching, please try again')
            return redirect('signup_teacher')

      else :
        messages.info(request,'Please make sure all required fields are filled out correctly')
        return redirect('signup_teacher') 






def sign_in_teacher(request):

    if request.method == 'GET':
    
       return render(request,'teacher/signin_page/index.html')

  
    if request.method == 'POST':

          username =  request.POST.get('username')
          password =  request.POST.get('password')
 
          user = auth.authenticate(username=username,password=password)

          if user is not None :
              
              try:

                if ( user.teacher.is_teacher == True ) :
                  auth.login(request,user)
                  
                  request.session['teacherusername'] = user.username

                  return redirect('teacher_ui')
               
              except :
                  messages.info(request,'invalid credentials')
                  return redirect('sign_in_teacher')

          else :
             messages.info(request,'invalid credentials')
             return redirect('sign_in_teacher')


    else :
      return render(request,'teacher/signin_page/index.html')





def saveddata(request,teacherusername):
  if request.method == 'POST':
    name =  request.POST['name']

    email = request.POST['email']
    
    gender =  request.POST['gender']
    
    mobile_no = request.POST['mobile_no']
    
    department =  request.POST['department']
    

    duser = User.objects.get(username=teacherusername)

    teacher.objects.filter(pk=duser.teacher).update( name=name, email=email, gender=gender, mobile_no=mobile_no, department=department)

    return redirect('dviewprofile',teacherusername)

