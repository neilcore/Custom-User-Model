from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UserRegistrationForm(UserCreationForm):
    """
        help_text: if something is entered invalid
        add email field
    """
    email = forms.EmailField(max_length=100, help_text="Valid email address is required")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'register-id'
        self.helper.form_method = 'post'
        self.helper.form_action = 'user_registration'
        self.helper.add_input(Submit('submit', 'Register', css_class="btn btn-success btn-block"))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
        """
            fields: required fields
        """

    """
        what happens after submitting the form
    """

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        print(email)
        try:
            account = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f'Email {email} is already in use.')
