from django import template

register = template.Library()

@register.filter(name="intprice")
def intprice(value):

    try:
        return f'{round(float(value))}৳'
    except (ValueError, TypeError):
        return value