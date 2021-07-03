from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display=('pk','name', 'age', 'height', 'body_weight', 'prefecture')

admin.site.register(Member, MemberAdmin)