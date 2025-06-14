from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin
from collegeSystem.users.models import Profile

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    list_display = ('username', 'email', 'is_staff', 'is_active')
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display = ('user', 'phone_number', 'profile_picture')
    search_fields = ('user__username', 'phone_number')
    list_filter = ('user__is_active', 'user__is_staff')
    raw_id_fields = ('user',)
    readonly_fields = ('user',)
    fieldsets = (
        (None, {
            'fields': ('user', 'profile_picture', 'phone_number')
        }),
    )


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass