from django.urls import path

from main.views import foods

urlpatterns = [
    path('foods/', foods.FoodsListView.as_view(), name='shops-list'),
]
