from django.contrib import admin

from meeting.models import Meeting, Comment, Purchase

# Register your models here.
admin.site.register(Meeting)
admin.site.register(Purchase)
admin.site.register(Comment)
