from django.contrib import admin

from . models import *

class AutomovilAdmin(admin.ModelAdmin):
    list_display = ("marca", "modelo", "tipo", "color", "precio")

class PersonalAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "dni", "email")

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "cuil", "direccion", "dni", "email")



admin.site.register(Automovil, AutomovilAdmin)
admin.site.register(Personal, PersonalAdmin)
admin.site.register(Cliente, ClienteAdmin)