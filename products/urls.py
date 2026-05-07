from django.urls import path
from . import views

urlpatterns = [path("", views.howdy),
               path("cats/", views.CategoryList.as_view()),
               path("prod/<int:pk>", views.ProductDetail.as_view()),
               path("prods/", views.ProductList.as_view()),
               #    path("<str:name>/", views.products_of_category),



               ]
