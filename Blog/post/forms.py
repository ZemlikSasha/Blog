from django import forms
from .models import Reviews, ReviewContact


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Reviews #ПРИВЯЗКА ФОРМЫ К МОДЕЛИ(КОМЕНТЫ)
        fields = ('name', 'email', 'text') #ПОЛЯ В ФОРМЕ


class ReviewFormContact(forms.ModelForm):

    class Meta:
        model = ReviewContact #(ОТЗЫВ)
        fields = ('name', 'email', 'text')
