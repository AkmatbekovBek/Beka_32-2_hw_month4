from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse


def watch_shop_view(request):
    watch = models.watch.objects.all()
    return render(request, 'watchs/watch.html', {'watch_key': watch})

def watch_shop_detail_view(request, id):
    watch_id = get_object_or_404(models.watch, id=id)
    return render(request, 'watchs/watch_detail.html', {'watch_id_key': watch_id})


def add_watch_shop_view(request):
    method = request.method
    if method == 'POST':
        form = forms.WatchShopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Добавление <<Часов>> прошло успешно!')
    else:
        form = forms.WatchShopForm()
    return render(request, 'watchs/crud/create_watch.html', {'form': form})

def delete_watch_shop_view(request, id):
    watch_id_delete = get_object_or_404(models.watch, id=id)
    watch_id_delete.delete()
    return HttpResponse('Удаление <<Часов>> прошло успешно!')

def update_watch_shop_view(request, id):
    watch_id = get_object_or_404(models.watch, id=id)
    if request.method == 'POST':
        form = forms.WatchShopForm(instance=watch_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Объект успешно обновлен')
    else:
        form = forms.WatchShopForm(instance=watch_id)

        context = {
            'form': form,
            'object': watch_id
        }
    return render(request, 'watchs/crud/update_watch.html', context)

