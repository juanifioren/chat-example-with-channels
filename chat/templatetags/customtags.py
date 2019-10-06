from django import template
from django.urls import reverse_lazy as reverse


register = template.Library()


@register.simple_tag
def build_chat_room_name(username1, username2):
    return '-'.join(sorted([username1, username2]))


@register.simple_tag
def build_chat_url(username1, username2):
    return reverse('chat', kwargs={
        'chatname': build_chat_room_name(username1, username2)})
