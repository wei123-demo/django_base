from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#视图函数
#请求（request）from django.http import HttpRequest
#返回HttpResponse   from django.http import HttpResponse

def index(request):

  #  return HttpResponse("Hello, Django!")
    #render渲染模板
    #request,template_name,content=None

    #模拟数据查询
    context = {
        'name':'点击有惊喜'
    }

    return render(request,'book/index.html',context=context)