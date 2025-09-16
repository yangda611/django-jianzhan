
"""此模块为全局变量，给前端用"""
from goods.models import GoodsCatalog
from news.models import NewsCatalog
from tuwen.models import TuWenCatalog
from site_set.models import Site

cache_time = 3600 * 24 * 7



def global_variable(request):
    global_dict = {}
    if not Site.objects.filter(id=1).exists():
        Site.objects.create(name='临时名称', url='http://www.xxx.com')
    site_mes = Site.objects.get(id=1)
    global_dict['site_mes'] = site_mes

    comm_pro_c = GoodsCatalog.objects.filter(category=31).order_by('sort', 'id')
    global_dict['comm_pro_c'] = comm_pro_c

    comm_case_c = TuWenCatalog.objects.filter(category=13).order_by('sort', 'id')
    global_dict['comm_case_c'] = comm_case_c

    comm_news_c = NewsCatalog.objects.filter(category=17).order_by('sort', 'id')
    global_dict['comm_news_c'] = comm_news_c

    return global_dict
