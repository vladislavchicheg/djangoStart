
from django.contrib import admin
from django.urls import include, path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view()),
    path("news/", views.NewsPageView.as_view()),
    path("courses_list/", views.CoursesPageView.as_view()),
    path("contacts/", views.ContactsPageView.as_view()),
    path("doc_site/", views.DocSitePageView.as_view()),
    path("login/", views.LoginPageView.as_view()),
]
