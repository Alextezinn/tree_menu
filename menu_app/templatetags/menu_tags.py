from typing import Optional
from django import template
from django.template import RequestContext

from menu_app.models import MenuItem


register = template.Library()


@register.inclusion_tag('menu_app/tree_menu.html', takes_context=True)
def draw_menu(context: RequestContext, title: str = '', parent: Optional[int] = None):

    if parent is not None:
        items = context.get('next_menu')
    else:
        items = MenuItem.objects.filter(menu__title=title)

    request_path = context.get('request')

    return {'next_menu': items, 'menu': tuple(item for item in items if item.parent_id == parent),
            'active': request_path if request_path is None else request_path.path}
