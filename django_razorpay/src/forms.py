from django import forms
from .models import ColdCoffe
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Button, Submit


class CoffeePaymentForm(forms.ModelForm):
    class Meta:
        model = ColdCoffe
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'name',
            'amount',
            Submit('submit', 'Buy', css_class="button white btn-black btn-primary")
        )
