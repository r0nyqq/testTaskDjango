from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import NewsModel


class NewsListView(ListView):
    paginate_by = 5
    model = NewsModel
    template_name = 'news_list.html'
    context_object_name = 'news_list'


class NewsDetailView(DetailView):
    model = NewsModel
    template_name = 'news.html'

    def get(self, request, *args, **kwargs):
        models = self.model.objects.get(id=kwargs['pk'])
        return render(request, 'news_detail.html', {'object': models})