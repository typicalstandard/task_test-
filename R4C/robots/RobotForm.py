from django import forms
from django.utils.deconstruct import deconstructible
from django.utils.dateparse import parse_datetime
from django.core.exceptions import ValidationError

from .models import Robot

@deconstructible
class AlphanumericAndLengthValidator:
    def __init__(self, max_length=2):
        self.max_length = max_length

    def __call__(self, value):
        if not value:
            raise ValidationError("Это поле не может быть пустым.")
        if not value.isalnum() or len(value) > self.max_length:
            raise ValidationError(f"Поле должно быть буквенно-цифровым и не более {self.max_length} символов.")
        return value


class RobotForm(forms.ModelForm):
    model = forms.CharField(
        label='Model',
        max_length=2,
        required=True,
        validators=[AlphanumericAndLengthValidator(max_length=2)]
    )

    version = forms.CharField(
        label='Version',
        max_length=2,
        required=True,
        validators=[AlphanumericAndLengthValidator(max_length=2)]
    )

    created = forms.DateTimeField(
        label='Created',
        required=False
    )

    class Meta:
        model = Robot
        fields = ['model', 'version', 'created']

    def clean_created(self):
        created = self.cleaned_data.get('created')
        if created:
            try:
                parse_datetime(str(created))
            except ValueError:
                raise forms.ValidationError("Введите корректную дату и время.")
        return created
