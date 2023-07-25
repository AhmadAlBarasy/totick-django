from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = "home"),
    path('lists/<int:id>',views.lists,name = "home"),
    path('lists/create',views.create,name = "create"),
    path('lists-view',views.viewUserLists,name = "view"),

    
]
