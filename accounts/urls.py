from django.urls import path
from . import views

urlpatterns = [


    path('sign_in_admin', views.sign_in_admin , name='sign_in_admin'),
    

    path('signup_teacher', views.signup_teacher , name="signup_teacher"),
    path('sign_in_teacher', views.sign_in_teacher , name='sign_in_teacher'),
    path('saveddata/<str:teacherusername>', views.saveddata , name='saveddata'),

    path('logout', views.logout , name='logout'),
]