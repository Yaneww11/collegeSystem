from django import template

register = template.Library()


@register.filter(name='is_student')
def is_student(user):
    return hasattr(user.profile, 'student_profile')
