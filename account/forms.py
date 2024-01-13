from django import forms
from django_countries.fields import CountryField
from .models import CustomUser, SecurityQuestion

class RegistrationForm(forms.ModelForm):
    nationality = CountryField().formfield()

    # Using ModelChoiceField for the security_question field
    security_question = forms.ModelChoiceField(
        queryset=SecurityQuestion.objects.all(),
        empty_label="Select a security question",
        required=False,  # You may adjust this based on your requirements
    )

    class Meta:
        model = CustomUser
        fields = ['full_name', 'username', 'date_of_birth', 'gender', 'email', 'phone_number',
                  'address', 'city', 'state', 'postal_code', 'country', 'occupation',
                  'company_name', 'website', 'security_question', 'security_answer', 'password']

        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['security_answer'].label = "Security Answer"
        self.fields['password'].required = True  # Ensure password is required

    def clean(self):
        cleaned_data = super().clean()
        security_question = cleaned_data.get("security_question")
        security_answer = cleaned_data.get("security_answer")

        # Validate that both security question and answer are provided together
        if security_question and not security_answer:
            self.add_error('security_answer', 'Please provide an answer to the selected security question.')
        elif security_answer and not security_question:
            self.add_error('security_question', 'Please select a security question for the provided answer.')

        return cleaned_data
