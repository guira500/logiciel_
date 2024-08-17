from django.contrib import admin
from .models import administrateur, employe
# Register your models here.

admin.site.register(employe)

@admin.register(administrateur)
class adminAdmin(admin.ModelAdmin):
    list_display = ('id','nom_admin','prenom_admin', 'email', 'password')