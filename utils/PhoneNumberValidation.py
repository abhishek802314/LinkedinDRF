from django.core.validators import RegexValidator


phone_validator = RegexValidator(
    regex=r'^(\+91)\d{9}$',
    message="Please write +91*********"
)