from django import template

register = template.Library()


@register.filter(name='is_rector')
def is_rector(user):
    if user.is_superuser:
        return True
    if not hasattr(user, 'profile'):
        return False
    if hasattr(user.profile, 'teacher_profile') and hasattr(user.profile.teacher_profile, 'head_of_faculty'):
        return True
    return False
