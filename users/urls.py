from django.urls import path
from . import views


urlpatterns = [path("<str:name>/", views.ProfileDetail.as_view()),
               path("cart/<str:name>", views.CartDetail.as_view()),





               ]
