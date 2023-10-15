from django import template

register = template.Library()

# Create your views here.


@register.filter
def starts_with(text, starts):
    # if isinstance(text, basestring):
    # return text.startswith(starts)
    return True
    # return False
