from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('contacts',views.contacts, name='contacts'),
    path('polls',views.polls, name='polls'),
    path('create',views.create, name='create'),
    path('<int:pk>',views.VoteDetailView.as_view(),name ='details_view')
]