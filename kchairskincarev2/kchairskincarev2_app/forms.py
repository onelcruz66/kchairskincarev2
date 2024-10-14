from django import forms
from kchairskincarev2_app.models import AppointmentRequest, MessageRequest
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class AppointmentForm(forms.ModelForm): 
    class Meta:
        model = AppointmentRequest
        fields = ['name', 'phone_number', 'date_requested', 'time_requested', 'service_type', 'barber_name']

        time_requested = forms.ChoiceField(
            choices=[
                ('9:00', '9:00'), 
                ('10:00', '10:00'), 
                ('11:00', '11:00'),
                ('12:00', '12:00'),
                ('1:00', '1:00'), 
                ('2:00', '2:00'), 
                ('3:00', '3:00'),
                ('4:00', '4:00'),
                ('5:00', '5:00')])
        
        service_type = forms.ChoiceField(
            choices=[
                ('Hair Styling', 'Hair Styling'), 
                ('Face Mask', 'Face Mask'), 
                ('Shaving', 'Shaving'),
                ('Beard Trimming', 'Beard Trimming'),
                ('Hair Wash', 'Hair Wash')])
        
        barber_name = forms.ChoiceField(
            choices=[
                ('Kamji', 'Kamji'), 
                ('Joel', 'Joel'), 
                ('Katiria', 'Katiria')])
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = MessageRequest
        fields = ['name', 'phone_number', 'email_address', 'subject', 'question']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        # Remove help texts
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

class CustomAuthenticationForm(AuthenticationForm):
    # Add any additional fields or customization if needed
    pass