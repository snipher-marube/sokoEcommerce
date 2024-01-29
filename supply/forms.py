from django import forms

from .models import ProductRequest

class ProductRequestForm(forms.ModelForm):
    class Meta:
        model = ProductRequest
        fields = ('product_name', 'product_description', 'product_image', 'product_price', 'product_quantity')
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'product_description': forms.Textarea(attrs={'class': 'form-control'}),
            'product_image': forms.FileInput(attrs={'class': 'form-control'}),
            'product_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'product_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'product_name': 'Product Name',
            'product_description': 'Product Description',
            'product_image': 'Product Image',
            'product_price': 'Product Price',
            'product_quantity': 'Product Quantity',
        }
        
        error_messages = {
            'product_name': {
                'required': 'Please enter the name of the product you want to supply',
            },
            'product_description': {
                'required': 'Please enter a description of the product you want to supply',
            },
            'product_image': {
                'required': 'Please upload an image of the product you want to supply',
            },
            'product_price': {
                'required': 'Please enter the price of the product you want to supply',
            },
            'product_quantity': {
                'required': 'Please enter the quantity of the product you want to supply',
            },
        }