from django import forms
from feedback.models import AnonymousFeedback, Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)

        # Add placeholders and classes to form inputs
        self.fields['message'].widget.attrs['placeholder'] = 'Enter You feedback here'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    



class AnonymousFeedbackForm(forms.ModelForm):
    class Meta:
        model = AnonymousFeedback
        exclude = ('user',)
