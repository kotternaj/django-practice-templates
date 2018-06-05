from django import template

register = template.Library()

def cutt(value, arg):
    return value.replace(arg,'')

register.filter('cutt', cutt)


