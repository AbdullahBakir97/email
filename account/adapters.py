from allauth.account.adapter import DefaultAccountAdapter
from django.utils.translation import gettext_lazy as _

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Override the save_user method to perform additional actions when saving a new user.
        For example, you could send a welcome email or perform other custom logic.
        """
        user = super().save_user(request, user, form, commit=False)
        # Add your custom logic here

        # For example, set a custom attribute on the user
        user.custom_attribute = form.cleaned_data.get('custom_attribute')

        if commit:
            user.save()
        return user

    def get_email_confirmation_url(self, request, emailconfirmation):
        """
        Override the get_email_confirmation_url method to customize the email confirmation URL.
        For example, you could use a custom URL or add additional query parameters.
        """
        url = super().get_email_confirmation_url(request, emailconfirmation)
        # Add your custom logic here

        # For example, add a query parameter to the confirmation URL
        url += f'?custom_param=example'

        return url

    def respond_email_verification_sent(self, request, user):
        """
        Override the respond_email_verification_sent method to customize the response
        after sending the email verification email.
        """
        # Add your custom logic here

        # For example, set a custom message in the response
        return _("Verification email sent. Please check your inbox and spam folder.")

    def respond_email_verification_resent(self, request, emailconfirmation):
        """
        Override the respond_email_verification_resent method to customize the response
        after resending the email verification email.
        """
        # Add your custom logic here

        # For example, set a custom message in the response
        return _("Verification email resent. Please check your inbox and spam folder.")
