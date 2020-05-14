from django import template

register = template.Library()

@register.filter(name='my_str_reverse')
def my_str_reverse(value):
    return value[::-1]