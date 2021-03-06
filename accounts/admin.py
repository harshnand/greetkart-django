from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','username','last_login','is_active')
    readonly_fields = ('last_login',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    list_display_links = ('email','first_name','last_name')

admin.site.register(Account,AccountAdmin)