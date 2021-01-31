import django_filters

from .models import Attendence, Student

class AttendenceFilter(django_filters.FilterSet):
    class Meta:
        model = Attendence
        fields = '__all__'
        exclude = ['Faculty_Name', 'status','time','branch','section', 'qr_pic']

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['branch', 'year', 'section', 'qr_pic']