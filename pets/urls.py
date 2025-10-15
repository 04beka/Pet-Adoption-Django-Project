from django.urls import path
from . import views

app_name = "pets"

urlpatterns = [
    path("", views.PetListView.as_view(), name="pet_list"),
    path("pets/create/", views.PetCreateView.as_view(), name="pet_create"),
    path("pets/<int:pk>/", views.PetDetailView.as_view(), name="pet_detail"),
    path("pets/<int:pk>/update/", views.PetUpdateView.as_view(), name="pet_update"),
    path("pets/<int:pk>/delete/", views.PetDeleteView.as_view(), name="pet_delete"),


    path("profile/edit/", views.ProfileUpdateView.as_view(), name="profile_edit"),


    path("profile/<str:username>/", views.ProfileDetailView.as_view(), name="profile_detail"),
]
