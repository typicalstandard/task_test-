from django import forms
from .models import Robot
from django.utils.dateparse import parse_datetime

class RobotForm(forms.ModelForm):
    model = forms.CharField(
        label='Model',
        max_length=2,
        required=True
    )
    
    version = forms.CharField(
        label='Version',
        max_length=2,
        required=True
    )

    created = forms.DateTimeField(
        label='Created',
        required=False
    )

    class Meta:
        model = Robot
        fields = ['model', 'version', 'created']

    def clean_model(self):
        model = self.cleaned_data.get('model')
        if not model:
            raise forms.ValidationError("This field cannot be null.")
        if not model.isalnum() or len(model) > 2:
            raise forms.ValidationError("Model must be alphanumeric and no more than 2 characters.")
        return model

    def clean_version(self):
        version = self.cleaned_data.get('version')
        if not version:
            raise forms.ValidationError("This field cannot be null.")
        if not version.isalnum() or len(version) > 2:
            raise forms.ValidationError("Version must be alphanumeric and no more than 2 characters.")
        return version

    def clean_created(self):
        created = self.cleaned_data.get('created')
        if created:
            try:
                parse_datetime(str(created))
            except ValueError:
                raise forms.ValidationError("Enter a valid date and time.")
        return created
