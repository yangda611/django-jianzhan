import datetime
import re
import time
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from form.models import Message
from site_set.models import Site
from sx_cms.settings import EMAIL_HOST_USER


# from web import message_page
@csrf_exempt
def message(request):
    if request.method == 'POST':
        name = request.POST['guest']
        tel = request.POST['tel']
        content = request.POST['content']
        if 'email' in request.POST:
            if request.POST['email']:
                mail = request.POST['email']
            else:
                mail = ''
        else:
            mail = ''

        if request.META.get('HTTP_X_FORWARDED_FOR'):
            ip = request.META.get("HTTP_X_FORWARDED_FOR")
        else:
            ip = request.META.get("REMOTE_ADDR")
        ip_queryset = Message.objects.filter(ipaddress=ip).order_by('-created_time')[:1]
        now_time = datetime.datetime.now()
        now_tuple = now_time.timetuple()
        now_times = time.mktime(now_tuple)
        if any(ip_queryset):
            for item in ip_queryset:
                database_time = int(item.created_time.timestamp())
        else:
            database_time = 0
        en_keyword = re.findall('[a-zA-Z]+', tel)
        if en_keyword:
            tel = re.sub(en_keyword[0], '_', tel)

        not_keyword = ['<', '>', '.html', 'http', 'https', '.script', '/', '../', '.js', 'or', 'ls -l', 'ls', 'ls -a', 'ls -l -a', 'ls - la', 'pwd', 'cd', 'touch', 'rm', 'rf', 'mkdir', 'rm - f', 'cp', 'mv', 'cat', 'head', 'tail', 'grep', 'find', 'wc', '|', 'cip', 'unzip', 'tar', '- cjf', '- czf', 'sudo', 'chmod', 'echo', 'date', 'whoami', 'df', 'df - Th', 'history', 'shutdown', 'groupadd', 'groupdel', 'useradd', 'passwd', 'userdel', 'apt', 'dpkg', 'service', 'ssh']

        for item in not_keyword:
            if item in name:
                name = re.sub(item, '_', name)
            if item in content:
                content = re.sub(item, '_', content)

        if not name or not tel:
            res = {"status": 0, "msg": "姓名和电话不能为空"}

        elif len(content) < 5:
            res = {"status": 1, "msg": "你好！请输入至少5个汉字"}

        elif (now_times - database_time) < 300:
            res = {"status": 3, "msg": "你的留言太频繁了，请五分钟后再来吧！"}

        else:
            fbook = Message.objects.create(name=name, tel=tel, email=mail, content=content, ipaddress=ip)

            if fbook.id:
                res = {"status": 4, "msg": "您的留言已提交，我们会尽快与您取得联系！"}
            else:
                res = {"status": 5, "msg": "您的留言提示失败，请稍后留言！"}

            import pymysql
            kwargs = {
                'host': '122.114.165.105',
                'port': 3306,
                'user': 'sxerp_sxglpx_com',
                'password': '6HPYTwB5p2rAwHTE',
                'database': 'sxerp_sxglpx_com',
                'charset': 'utf8'
            }

            db = pymysql.connect(**kwargs)
            cur = db.cursor()

            up_time = '%s-%s-%s' % (
                datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)

            obj = Site.objects.all().first()
            company = obj.name
            url = obj.url
            person = obj.person
            phone = obj.phone
            try:
                # 写入
                sql = f"insert into web_seodepartmessage (created_time,person,phone,note,company,url,name,c_phone,is_talk,inform_time,create_time) values ('{up_time}','{name}','{tel}','{content}','{company}','{url}','{person}','{phone}',FALSE,'','{up_time}');"
                cur.execute(sql)
                db.commit()

            except Exception as e:
                print(e)
                db.rollback()

        return HttpResponse(json.dumps(res))
