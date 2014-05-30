from django.http import HttpResponse
from django.template import loader, Context

from news.models import News


def news(request):
    news_all = News.objects.all().order_by('-pub_date')
    template = loader.get_template('news.html')
    context = Context({
        'news_all': news_all,
    })
    return HttpResponse(template.render(context))
