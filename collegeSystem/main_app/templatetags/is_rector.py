from django import template

register = template.Library()


@register.filter(name='is_rector')
def is_rector(user):
    if user.is_superuser:
        return True
    if not hasattr(user, 'profile'):
        return False
    if hasattr(user.profile, 'rector_of_college'):
        return True
    return False
