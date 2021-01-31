"""from django.contrib import admin
from .models import (
    Teacher, Department, Course
    )

admin.site.register(Teacher)
admin.site.register(Department)
admin.site.register(Course)



# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, user_type


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'name', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)

# We can register our models like before
# This was the model we commented in the previous snippet.

admin.site.register(user_type)"""




from django.contrib import admin
from .models import teacher, Student, Attendence

# Register your models here.

admin.site.register(teacher)
admin.site.register(Student)
admin.site.register(Attendence)