from django.contrib import admin
from django.urls import path,include
from .views import login,register,contacts,Spam,Name_search,Mobile_search


urlpatterns = [
    path("login",login.as_view(),name  = "login"), #login the user
    path("register", register.as_view(),name = "register"),#Register new User
    path("contacts/",contacts.as_view(),name = "contacts"),# gets method retrieve all the contacts,post method create contacts
    path("spam/",Spam.as_view(), name = "spam"),#can mark a number spam, when number is provided
    path("name_search/", Name_search.as_view(), name = "name_search"),#can retrieve contacts based on name
    path("mobile_search/", Mobile_search.as_view(),name = "mobile_search")#retrieves contacts based on mobile number
]
