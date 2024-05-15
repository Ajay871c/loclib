from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Language)
admin.site.register(BookInstrance)
admin.site.register(Genre)
