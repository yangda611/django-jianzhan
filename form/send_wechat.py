import json
import requests

from form.accessToken import AccessToken
from site_set.models import Site


class SendMessage(object):
    wechat_openid = Site.objects.filter(id=1).first().wechat_openid

    TOUSER = wechat_openid
    print(TOUSER)

    TEMPLATE_ID = '9LboAz3JQd46jkfGFIMym9iY3l1_mY6szmDp2FPD-JM'

    def __init__(self, touser=TOUSER, template_id=TEMPLATE_ID) -> None:

        self.access_token = AccessToken().get_access_token()
        self.touser = touser
        self.template_id = template_id

    def get_send_data(self, json_data) -> object:

        return {
            "touser": self.touser,
            "template_id": self.template_id,
            "topcolor": "#FF0000",
            "data": {
                "keyword1": {
                    "value": json_data["keyword1"],
                    "color": "#173177"
                },
                "keyword2": {
                    "value": json_data["keyword2"],
                    "color": "#173177"
                },
                "keyword3": {
                    "value": json_data["keyword3"],
                    "color": "#173177"
                },
                "keyword4": {
                    "value": json_data["keyword4"],
                    "color": "#173177"
                },
            }
        }

    def send_message(self, json_data) -> None:
        url = f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={self.access_token}"
        data = json.dumps(self.get_send_data(json_data))
        resp = requests.post(url, data=data)
        result = resp.json()

        if result["errcode"] == 0:
            print("消息发送成功")
        else:
            print(result)
