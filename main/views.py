from django.shortcuts import render, HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf
from .models import Goods


def index(request):
    args = {
        'goods': Goods.objects.all().order_by('goodsrate__rate_count'),
    }
    args.update(csrf(request))
    return render(request, 'main/index.html', args)


def selected_item(request, item_id):
    args = {
        'item': Goods.objects.get(id=item_id),
    }
    if request.is_ajax():
        return render(request, 'main/selected_item_ajax.html', args)
    else:
        return render(request, 'main/selected_item.html', args)


def login(request):
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponse('authorized')
        else:
            return HttpResponse('Ошибка входа.')
    else:
        print('Something wrong...')
        return HttpResponse('Something wrong...')
