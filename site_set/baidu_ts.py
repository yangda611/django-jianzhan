import requests as r

class BaiduTS:

    def __init__(self, site, token):
        self.SITE = site

        self.TOKEN = token

        self.API = 'http://data.zz.baidu.com/{ACTION}?site={SITE}&token={TOKEN}'

    def _do(self, action, page_list):
        page_string = ''

        for page in page_list:
            page_string += page + '\n'

        content_length = len(page_string)

        response = r.post(

            self.API.format(ACTION=action,

                            SITE=self.SITE,

                            TOKEN=self.TOKEN),

            headers={

                'User-Agent': 'curl/7.12.1',

                'Host': 'data.zz.baidu.com',

                'Content-Length': str(content_length)

            },

            data=page_string

        )

        return response.json()

    def push(self, page_list): return self._do('urls', page_list)

    def update(self, page_list): return self._do('update', page_list)

    def delete(self, page_list): return self._do('del', page_list)