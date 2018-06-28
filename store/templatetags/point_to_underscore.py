from django import template
register = template.Library()

@register.filter
def point_to_underscore(value):
    if value is None:
        return None
    else:
        processed_string = value.replace(".","_")
        return processed_string




#@register.filter
#def point_to_underscore(self):
#    if self is None:
#        return None
#    try:
#        self.replace(".","_")
#    return
