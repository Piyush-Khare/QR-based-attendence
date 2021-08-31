from django.db import models
from django.contrib.auth.models import User


from datetime import date

from PIL import Image, ImageDraw
from django.core.files import File
from io import BytesIO
import qrcode

# Create your models here.


#user = models.OneToOneField(settings.AUTH_USER_MODEL)


class teacher(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    is_teacher = models.BooleanField(default=True)

    name = models.CharField(max_length = 50)
    #email = models.EmailField(max_length=254)
    mobile_no = models.CharField(max_length = 15)
    gender = models.CharField(max_length = 10)

    department = models.CharField(max_length = 20)

    def __str__(self):
        return self.name






class Student(models.Model):

    BRANCH = (
        ('MCA','MCA'),
        ('BCA','BCA'),
        ('PGDCA','PGDCA'),
        ('O Level','O Level'),
    )
    SEMESTER = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
    )
    SECTION = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
    )

    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    registration_id = models.CharField(max_length=200, null=True)
    branch = models.CharField(max_length=100, null=True, choices=BRANCH)
    semester = models.CharField(max_length=100, null=True, choices=SEMESTER)
    section = models.CharField(max_length=100, null=True, choices=SECTION)
    qr_pic = models.ImageField(upload_to='media/', null=True, blank=True)


    def __str__(self):
        return str(self.registration_id)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.registration_id)
        canvas = Image.new('RGB',(280,280))
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'{self.registration_id}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_pic.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

class Attendence(models.Model):
    # faculty = models.ForeignKey(Faculty, null = True, on_delete= models.SET_NULL)
    # student = models.ForeignKey(Student, null = True, on_delete= models.SET_NULL)
    #Faculty_Name = models.CharField(max_length=200, null=True, blank=True)
    Student_ID = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(auto_now_add = True, null = True)
    time = models.TimeField(auto_now_add=True, null = True)
    branch = models.CharField(max_length=200, null = True)
    semester = models.CharField(max_length=200, null = True)
    section = models.CharField(max_length=200, null = True)
    period = models.CharField(max_length=200, null = True)
    status = models.CharField(max_length=200, null = True, default='Absent')

    def __str__(self):
        return str(self.Student_ID + "_" + str(self.date)+ "_" + str(self.period))