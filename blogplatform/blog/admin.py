from django.contrib import admin
from .models import *

admin.site.register(BlogPost)
admin.site.register(BlogAuthor)
admin.site.register(BlogComment)
