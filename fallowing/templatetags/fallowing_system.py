from django import template

register = template.Library()


@register.filter
def who_is_my_fallowed(user, my_fallowed):
    if user.username in my_fallowed:
        return True
    return False
