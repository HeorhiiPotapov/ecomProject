from django.template import Library
from ..models import Category

register = Library()


@register.simple_tag
def cat_list():
    return Category.objects.all()
