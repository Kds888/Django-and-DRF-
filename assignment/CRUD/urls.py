from django.urls import path
from . import views

app_name='CRUD'

urlpatterns=[
    path('',views.home,name='home'),
    path('list/',views.MyModelListView.as_view(),name='list'),
    path('create/',views.MyModelCreateView.as_view(),name='create'),
    path('delete/<int:pk>/',views.MyModelDeleteView.as_view(),name='delete'),
    path('update/<int:pk>/',views.MyModelUpdateView.as_view(),name='update'),
]