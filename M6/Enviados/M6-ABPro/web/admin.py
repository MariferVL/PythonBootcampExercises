from django.contrib import admin

# Register your models here.

from . models import Funfact, Scale, Tip, Post, Link, Photo, Suscriptor



class table_format1(admin.ModelAdmin):
    list_display = ('title', 'text', 'photo')
class table_format2(admin.ModelAdmin):
    list_display = ('title', 'icon', 'text',)
class table_format3(admin.ModelAdmin):
    list_display = ('full_name', 'email')

class table_format4(admin.ModelAdmin):
    list_display = ('typesb', 'text', 'cause', 'photo')


admin.site.register(Funfact, table_format1)
admin.site.register(Scale, table_format4)
admin.site.register(Tip, table_format2)
admin.site.register(Post, table_format1)
admin.site.register(Link, table_format2)
admin.site.register(Photo, table_format1)
admin.site.register(Suscriptor, table_format3)

