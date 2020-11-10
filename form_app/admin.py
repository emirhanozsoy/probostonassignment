from django.contrib import admin

# Register your models here.
from .models import Form_Info

class MyAdmin(admin.ModelAdmin):
     def has_add_permission(self, request, obj=None):
        return False

admin.site.register(Form_Info, MyAdmin)