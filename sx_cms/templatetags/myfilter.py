import re

from django import template
from django.template import Node

register = template.Library()


@register.filter
def sp(value):
    return value.split('\r\n')


@register.filter
def ap(value):
    return value.split(':')


@register.filter
def rep(value):
    return value.replace('\r\n', '<br>')


@register.filter
def repp(value):
    return value.replace('——', '<br>')


@register.filter
def refiles(value):
    return value.replace('files/', '')


@register.filter
def retable(value):
    return value.replace('<table', '<div class="pc_table"><table')


@register.filter
def retablelast(value):
    return value.replace('</table>', '</table></div>')


@register.filter
def getimage(value):
    pic_url = re.findall('src="(.*?)"', value)
    if len(pic_url) > 0:
        photo_url = pic_url[0]
    else:
        photo_url = '/static/Image/news_img.jpg'
    return photo_url

@register.tag
def lineless(parser, token):
    nodelist = parser.parse(('endlineless',))
    parser.delete_first_token()
    return LinelessNode(nodelist)


class LinelessNode(Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        input_str = self.nodelist.render(context)
        output_str = ''
        for line in input_str.splitlines():
            if line.strip():
                output_str = '\n'.join((output_str, line))
        return output_str


@register.filter
def cutstr(value, num):
    pattern = re.compile(r'<[^>]+>', re.S)
    result = pattern.sub('', value)
    result = re.sub('\s|\t|\n', '', result)
    result = re.sub('&nbsp;', '', result)
    result = re.sub('&emsp;', '', result)
    result = result.strip()
    if len(result) > num:
        string = result[0:num] + '...'
    else:
        string = result
    return string
