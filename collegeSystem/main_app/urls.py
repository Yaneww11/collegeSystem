from django.urls import path, include

from collegeSystem.main_app.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    # path('addres-book/', address_book_view, name='address-book'),
]