from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.contrib.auth.validators import UnicodeUsernameValidator, ASCIIUsernameValidator
from django.core.validators import MinLengthValidator
from django.contrib.auth.password_validation import CommonPasswordValidator, MinimumLengthValidator, NumericPasswordValidator, UserAttributeSimilarityValidator




class SecurityQuestion(models.Model):
    question_text = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.question_text
    
    
class EmailAccount(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    email_address = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  

    def __str__(self):
        return self.email_address
    
class CustomUser(AbstractUser):
    # Personal Information
    full_name = models.CharField(max_length=255, blank=True)
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[UnicodeUsernameValidator(), ASCIIUsernameValidator()],
        help_text="Required. name with max 150 characters.  Letters, digits and @/./+/-/_ only.",
    )
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    nationality = CountryField(blank=True, null=True)

    # Contact Information
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(blank=True, null=True, help_text="International format, e.g., +1 123-456-7890")

    # Address Information
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = CountryField(blank=True, null=True)

    # Additional Information
    OCCUPATION_CHOICES = [
        ('home', 'Home'),
        ('work', 'Work'),
        ('other', 'Other'),
    ]
    occupation = models.CharField(max_length=100, choices=OCCUPATION_CHOICES, blank=True)
    company_name = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)

    # Security Information
    password = models.CharField(
        ('password'),
        max_length=128,
        validators=[
            MinimumLengthValidator(8),
            CommonPasswordValidator(),
            NumericPasswordValidator(),
            UserAttributeSimilarityValidator(),
        ],
        help_text=_('Your password must be at least 8 characters long and contain a mix of letters, digits, and symbols.'),
    )
    security_question = models.ForeignKey(SecurityQuestion, on_delete=models.SET_NULL, null=True, blank=True)
    security_answer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username
