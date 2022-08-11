from django import template

register = template.Library()


@register.filter
def my_filter(x):
    return f"{x}_filtered"


@register.simple_tag
def my_tag():
    return "mY TAG CONTENT deployed a"