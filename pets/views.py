from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import PetForm, SearchForm, ProfileForm
from .models import Pet, Profile

class PetListView(generic.ListView):
    model = Pet
    template_name = "pets/pet_list.html"
    paginate_by = 10
    context_object_name = "pets"

    def get_queryset(self):
        qs = Pet.objects.select_related("owner").all()
        self.form = SearchForm(self.request.GET or None)
        if self.form.is_valid():
            q = self.form.cleaned_data.get("q")
            species = self.form.cleaned_data.get("species")
            adopted = self.form.cleaned_data.get("adopted")

            if q:
                qs = qs.filter(
                    Q(name__icontains=q) | Q(breed__icontains=q) | Q(city__icontains=q) | Q(description__icontains=q)
                )
            if species:
                qs = qs.filter(species=species)
            if adopted in ("0", "1"):
                qs = qs.filter(is_adopted=(adopted == "1"))
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["search_form"] = getattr(self, "form", SearchForm())
        return ctx

class PetDetailView(generic.DetailView):
    model = Pet
    template_name = "pets/pet_detail.html"
    context_object_name = "pet"

class OwnerOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user or self.request.user.is_staff

class PetCreateView(LoginRequiredMixin, generic.CreateView):
    model = Pet
    form_class = PetForm
    template_name = "pets/pet_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("pets:pet_detail", kwargs={"pk": self.object.pk})

class PetUpdateView(LoginRequiredMixin, OwnerOnlyMixin, generic.UpdateView):
    model = Pet
    form_class = PetForm
    template_name = "pets/pet_form.html"

    def get_success_url(self):
        return reverse_lazy("pets:pet_detail", kwargs={"pk": self.object.pk})

class PetDeleteView(LoginRequiredMixin, OwnerOnlyMixin, generic.DeleteView):
    model = Pet
    template_name = "pets/pet_confirm_delete.html"
    success_url = reverse_lazy("pets:pet_list")

class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = "pets/profile_detail.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        user = get_object_or_404(User, username=self.kwargs["username"])
        return user.profile

class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "pets/pet_form.html"

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        return reverse_lazy("pets:profile_detail", kwargs={"username": self.request.user.username})
