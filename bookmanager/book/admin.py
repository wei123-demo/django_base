from django.contrib import admin

# Register your models here.
from book.models import BookInFo,PropleInFo

admin.site.register(BookInFo)
admin.site.register(PropleInFo)