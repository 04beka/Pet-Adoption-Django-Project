from django import forms
from .models import Pet, Profile

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ["name", "species", "breed", "age", "city", "description", "photo", "is_adopted"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["phone", "city", "bio"]

class SearchForm(forms.Form):
    q = forms.CharField(required=False, label="ძებნა", widget=forms.TextInput(attrs={"placeholder": "სახელი, ჯიში, ქალაქი"}))
    species = forms.ChoiceField(
        required=False,
        choices=[("", "ყველა")] + list(Pet._meta.get_field("species").choices)
    )
    adopted = forms.ChoiceField(
        required=False,
        choices=[("", "ყველა"), ("0", "არ არის აყვანილი"), ("1", "აყვანილია")]
    )
