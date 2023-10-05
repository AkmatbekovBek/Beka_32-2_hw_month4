from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse
from django.views import generic

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView, ListView


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

class AddWatchShopReviews(generic.CreateView):
    template_name = 'watchs/crud/write_reviews.html'
    form_class = forms.WatchShopReviewsForm
    queryset = models.watch.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(AddWatchShopReviews, self).form_valid(form=form)



class RegistrationView(CreateView):
    form_class = forms.RegistraionNewForm
    success_url = '/'
    template_name = 'registration/registration.html'

class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'
    success_url = '/'

    def get_success_url(self):
        return reverse('users:user_list')

class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'registration/user_list.html'

    def get_queryset(self):
        return User.objects.all()








