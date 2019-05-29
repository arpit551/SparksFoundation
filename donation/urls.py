from django.urls import path,include
from donation import views
urlpatterns = [
    path('',views.homepage,name="home"),
    path('submit/',views.donatesubmit,name="submit")
]
