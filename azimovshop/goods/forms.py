from django.forms import ModelForm

from .models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
        help_texts = {
            'rating': 'Выберете рейтинг из списка'
        }
