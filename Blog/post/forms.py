from django import forms
from .models import Reviews, ReviewContact


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')


class ReviewFormContact(forms.ModelForm):

    class Meta:
        model = ReviewContact
        fields = ('name', 'email', 'text')
