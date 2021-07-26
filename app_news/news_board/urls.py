from django.urls import path
from .views import NewsListView, NewsDetailView

urlpatterns = [
    path('news_list/', NewsListView.as_view(), name='news_list'),
    path('news_list/<int:pk>/', NewsDetailView.as_view(), name='detail_news')
]