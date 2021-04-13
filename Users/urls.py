from django.urls import path,include

from Users import views

app_name="Users"

urlpatterns = [
    path("",views.indexs,name="login"),
]
