from django import template

register = template.Library()


@register.filter(name='is_teacher')
def is_teacher(user):
    return hasattr(user.profile, 'teacher_profile') or user.is_superuser
