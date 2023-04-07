from django.views.generic.edit import CreateView
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404

class UserRegisterForm(CreateView):
    form_class = UserRegistrationForm
    template_name = 'user/auth/user_registration.html'
    success_url = reverse_lazy('main-page')
    form_name = 'register_form'


    def form_valid(self, form):
        response = super().form_valid(form)

        user = form.save(commit=False)
        active_status = get_object_or_404(Status, status='Active')
        user.status = active_status
        user.save()

        email = form.cleaned_data.get('email').lower()
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(email=email, password=raw_password)
        login(self.request, user)
        return response