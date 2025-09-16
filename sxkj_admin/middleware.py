import re
from urllib.parse import urlparse, parse_qsl
from django.http import Http404


class InvalidQueryStringMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not re.match(".*sxkjcms-admin/", request.path):
            parsed_url = urlparse(request.get_full_path())
            query_params = dict(parse_qsl(parsed_url.query))

            if 'page' in query_params:
                page_value = query_params['page']
                if not page_value.isdigit() or len(query_params) > 1:
                    raise Http404

            if 'dir' in query_params:
                image = query_params['dir']
                if image != 'image':
                    raise Http404

            if not query_params and '?' in request.get_full_path():
                raise Http404

            # code_id 是小程序登陆
            if query_params and 'page' not in query_params and 'dir' not in query_params and 'code_id' not in query_params:
                raise Http404

        return self.get_response(request)



