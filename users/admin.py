from django.contrib import admin
from users.models import User, AvatarUser, BackgroundUser
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
    
    
admin.site.register(User, UserAdmin)
admin.site.register(AvatarUser)
admin.site.register(BackgroundUser)