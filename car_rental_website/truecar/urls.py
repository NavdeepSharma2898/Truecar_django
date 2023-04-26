
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("about/", views.about, name='AboutUs'),
    path("registration/", views.registration, name='registration'),
    path("search/", views.search, name='search'),

    path('login/', views.handeLogin, name="handleLogin"),
    path('logout/', views.handelLogout, name="handleLogout"),
    path("checkout/", views.checkout, name='checkout'),
    path("bookings/", views.bookings, name='bookings'),
    path("suv/", views.suv, name='suv'),
    path("sedan/", views.sedan, name='sedan'),
    path("hatchback/", views.hatchback, name='hatchback')
]
