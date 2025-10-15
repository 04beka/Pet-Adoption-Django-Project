from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# auth_views აღარ გჭირდებათ აქ, რადგან იყენებთ include("django.contrib.auth.urls")
# from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),

    # ეს ხაზი მოიცავს ყველა სტანდარტულ ავთენთიფიკაციის URL-ს (login, logout, password_change და ა.შ.)
    # სტანდარტული URL სახელებით (e.g., 'logout') და პრეფიქსით /accounts/
    path("accounts/", include("django.contrib.auth.urls")),

    # დუბლირებული 'logout/' ხაზი ამოღებულია
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path("", include("pets.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)