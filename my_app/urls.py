from django.urls import path , re_path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path('admin_ui', views.admin_ui , name='admin_ui'),

    path('teacher_ui', views.teacher_ui , name='teacher_ui'),
    path('dviewprofile/<str:teacherusername>', views.dviewprofile , name='dviewprofile'),
    

    path('searchattandance', views.searchAttandance, name='searchattandance'),

    path('id_card', views.card, name='id_card'),
    path('attendence', views.takeAttendence, name='attendence'),

    
]  
