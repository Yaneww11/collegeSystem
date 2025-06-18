from django import template

register = template.Library()


@register.filter(name='is_teacher')
def is_teacher(user):
    if user.is_superuser:
        return True
    if not hasattr(user, 'profile'):
        return False
    return hasattr(user.profile, 'teacher_profile')
