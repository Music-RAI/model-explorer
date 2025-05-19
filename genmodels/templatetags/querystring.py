from django import template
from django.utils.http import urlencode

register = template.Library()

@register.filter
def append_tag_param(query_string, tag_param):
    if query_string:
        query_params = [tuple(param.split('=')) for param in query_string.split('&')]
    else:
        query_params = []

    query_params.append(("tag", tag_param))
    return urlencode(set(query_params))

@register.filter
def remove_tag_param(query_string, tag_param):
    query_params = []
    if query_string:
        query_params = [tuple(param.split('=')) for param in query_string.split('&')]

    query_params = set(query_params) - set([("tag", tag_param)])
    return urlencode(query_params)
