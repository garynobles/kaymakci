from django import template
register = template.Library()

@register.filter
def point_to_underscore(value):
    return value.replace(".","_")
