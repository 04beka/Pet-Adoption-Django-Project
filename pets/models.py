from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=60, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Profile: {self.user.username}"

SPECIES_CHOICES = [
    ("dog", "Dog"),
    ("cat", "Cat"),
    ("bird", "Bird"),
    ("other", "Other"),
]

class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pets")
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=16, choices=SPECIES_CHOICES)
    breed = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField(help_text="Age in years")
    city = models.CharField(max_length=60, blank=True)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="pet_photos/", blank=True, null=True)
    is_adopted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.get_species_display()})"
