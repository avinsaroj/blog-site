from django.contrib import admin
from .models import Contact,Post,auther,comment

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','message')

admin.site.register(Contact,ContactAdmin)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','desc','auther','data')

admin.site.register(Post, PostAdmin)
class autherAdmin(admin.ModelAdmin):
    list_display = ('user','image','about','profession')

admin.site.register(auther, autherAdmin)

@admin.register(comment)
class commentAdmin(admin.ModelAdmin):
    list_display=('user','Posts','comment')
    
