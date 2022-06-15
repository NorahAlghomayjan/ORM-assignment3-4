from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.index),
    path('addDojo',views.addDojo),
    path('addNinja', views.addNinja),
    path('deleteDojo/<int:id>',views.deleteDojo),
]