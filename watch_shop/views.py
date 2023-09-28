from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse
from django.views import generic


class WatchShopView(generic.ListView):
    template_name = 'watchs/watch.html'
    queryset = models.watch.objects.all()

    def get_queryset(self):
        return models.watch.objects.all()

# def watch_shop_view(request):
#     watch = models.watch.objects.all()
#     return render(request, 'watchs/watch.html', {'watch_key': watch})

class WatchShopDetailView(generic.DetailView):
    template_name = 'watchs/watch_detail.html'

    def get_object(self, **kwargs):
        watch_id = self.kwargs.get('id')
        return get_object_or_404(models.watch, id=watch_id)


# def watch_shop_detail_view(request, id):
#     watch_id = get_object_or_404(models.watch, id=id)
#     return render(request, 'watchs/watch_detail.html', {'watch_id_key': watch_id})


class AddWatchShopView(generic.CreateView):
    template_name = 'watchs/crud/create_watch.html'
    form_class = forms.WatchShopForm
    queryset = models.watch.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(AddWatchShopView, self).form_valid(form=form)


# def add_watch_shop_view(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.WatchShopForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Добавление <<Часов>> прошло успешно!')
#     else:
#         form = forms.WatchShopForm()
#     return render(request, 'watchs/crud/create_watch.html', {'form': form})



class DeleteWatchShopView(generic.DeleteView):
    template_name = 'watchs/crud/confirm_delete.html'
    success_url = '/'

    def get_object(self, **kwargs):
        watch_id = self.kwargs.get('id')
        return get_object_or_404(models.watch, id=watch_id)


# def delete_watch_shop_view(request, id):
#     watch_id_delete = get_object_or_404(models.watch, id=id)
#     watch_id_delete.delete()
#     return HttpResponse('Удаление <<Часов>> прошло успешно!')


class UpdateWatchShopView(generic.UpdateView):
    template_name = 'watchs/crud/update_watch.html'
    form_class = forms.WatchShopForm
    success_url = '/'

    def get_object(self, **kwargs):
        watch_id = self.kwargs.get('id')
        return get_object_or_404(models.watch, id=watch_id)

    def form_valid(self, form):
        return super(UpdateWatchShopView, self).form_valid(form=form)


# def update_watch_shop_view(request, id):
#     watch_id = get_object_or_404(models.watch, id=id)
#     if request.method == 'POST':
#         form = forms.WatchShopForm(instance=watch_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Объект успешно обновлен')
#     else:
#         form = forms.WatchShopForm(instance=watch_id)
#
#         context = {
#             'form': form,
#             'object': watch_id
#         }
#     return render(request, 'watchs/crud/update_watch.html', context)

class Search(generic.ListView):
    template_name = 'watchs/watch.html'
    context_object_name = 'watch'
    paginate_by = 5

    def get_queryset(self):
        return models.watch.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

