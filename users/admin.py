from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import EmailSubscribe, User


class UserAdmin(BaseUserAdmin):
    """
    Customize the users admin in the django admin site.
    We can customize the fields to disply in the list view and edit view.
    Also set the search and filters for the user admin.
    """

    list_display = ('email', 'first_name', 'last_name',
                    'is_superuser', 'is_staff', 'is_active')
    list_filter = ('is_superuser', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password',
                           'is_superuser', 'is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)


class EmailSubscribeAdmin(admin.ModelAdmin):
    search_fields = ('email',)


admin.site.register(User, UserAdmin)
admin.site.register(EmailSubscribe, EmailSubscribeAdmin)
