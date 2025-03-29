from django.urls import path
import AppSicop.views_list.filter.filter_view as f_view

urlpatterns = [
    path('', f_view.filter),
]
