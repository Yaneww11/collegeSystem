from django import template

register = template.Library()


@register.filter(name='is_student')
def is_student(user):
    if user.is_superuser:
        return False
    if not hasattr(user, 'profile'):
        return False
    return hasattr(user.profile, 'student_profile')
