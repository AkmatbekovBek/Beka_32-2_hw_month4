from django.shortcuts import render, get_object_or_404
from . import models

def watch_shop_view(request):
    watch = models.watch.objects.all()
    return render(request, 'watchs/watch.html', {'watch_key': watch})

def watch_shop_detail_view(request, id):
    watch_id = get_object_or_404(models.watch, id=id)
    return render(request, 'watchs/watch_detail.html', {'watch_id_key': watch_id})