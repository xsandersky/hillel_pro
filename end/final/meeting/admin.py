from django.contrib import admin

from meeting.models import Meeting, Comment, Purchase, User

# Register your models here.
admin.site.register(Meeting)
admin.site.register(Purchase)
admin.site.register(Comment)
admin.site.register(User)
