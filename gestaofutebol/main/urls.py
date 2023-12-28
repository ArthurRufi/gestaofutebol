from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name= "main"),
    path("<int:questionid>/", views.details, name="details"),
    path("<int:questionid>/results/", views.results, name="results"),
    path("<int:questionid>/vote/", views.vote, name="vote"),
    path("login/", views.login, name="login"),
    #path("<path:null>/", views.pagnull, name="")
]


