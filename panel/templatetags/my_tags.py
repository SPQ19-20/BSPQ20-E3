from django import template
import re
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def add(html_input, properties):
    """
    Inserta propiedades en un campo html.

    Uso: {{ form.field_name|add:'class="form-control" placeholder="Placeholder here"' }}
    """
    pattern = r'(\s\/>|>)'
    regex = re.compile(pattern, re.IGNORECASE)
    replace = ' {0}>'.format(properties)
    html = regex.sub(replace, str(html_input))
    return mark_safe(html)

@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """
    Return encoded URL parameters that are the same as the current
    request's parameters, only with the specified GET parameters added or changed.

    It also removes any empty parameters to keep things neat,
    so you can remove a parm by setting it to ``""``.

    For example, if you're on the page ``/things/?with_frosting=true&page=5``,
    then

    <a href="/things/?{% param_replace page=3 %}">Page 3</a>

    would expand to

    <a href="/things/?with_frosting=true&page=3">Page 3</a>

    Based on
    https://stackoverflow.com/questions/22734695/next-and-before-links-for-a-django-paginated-query/22735278#22735278
    """
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()