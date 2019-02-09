from django.contrib import admin

from .models import User, Task, File, Message, Chat, BugReport

admin.site.register(User)
admin.site.register(Task)
admin.site.register(File)
admin.site.register(Message)
admin.site.register(Chat)
admin.site.register(BugReport)
