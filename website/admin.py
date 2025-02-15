from django.contrib import admin
from .models import BlogPost, ContactMessage

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(ContactMessage)