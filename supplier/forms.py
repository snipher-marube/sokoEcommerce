# forms.py
from django import forms
from .models import SupplyRequest, Commodity

class CommodityForm(forms.ModelForm):
    class Meta:
        model = Commodity
        fields = ['name', 'available_amount', 'price']

    def __init__(self, *args, **kwargs):
        super(CommodityForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class SupplyRequestForm(forms.ModelForm):
    class Meta:
        model = SupplyRequest
        fields = ['commodities']

    def __init__(self, *args, **kwargs):
        super(SupplyRequestForm, self).__init__(*args, **kwargs)
        self.fields['commodities'].widget.attrs['class'] = 'form-control'
        self.fields['commodities'].widget.attrs['placeholder'] = 'Select commodities'
        self.fields['commodities'].queryset = self.fields['commodities'].queryset.order_by('name')
            
