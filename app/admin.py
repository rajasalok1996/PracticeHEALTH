# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Roles, Person, Amenity, Department, Hospital


# Register your models here.
class RolesModelAdmin(admin.ModelAdmin):
    list_display = ('role',)
admin.site.register(Roles, RolesModelAdmin)

class PersonModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_no', 'emergency_contact', 'age',)

    # def get_roles(self, obj):
    #     return "\n".join([p.products for p in obj.roles.all()])
admin.site.register(Person, PersonModelAdmin)

class AmenityModelAdmin(admin.ModelAdmin):
    list_display = ('amenity',)
admin.site.register(Amenity,AmenityModelAdmin)

class DepartmentModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Department, DepartmentModelAdmin)

class HospitalModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
admin.site.register(Hospital, HospitalModelAdmin)



