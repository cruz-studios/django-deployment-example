from django import template

register = template.Library()

# {% load my_templates %}

def cut(value,arg):
    """
    This cuts out all values of 'arg from the string!
    """
    return value.replace(arg,'')

register.filter('cut', cut)