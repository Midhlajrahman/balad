from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [
        (1, "1 Star"),
        (2, "2 Stars"),
        (3, "3 Stars"),
        (4, "4 Stars"),
        (5, "5 Stars"),
    ]

    rating = forms.ChoiceField(
        choices=RATING_CHOICES, widget=forms.RadioSelect, required=True
    )

    class Meta:
        model = Review
        fields = ["fullname", "headline", "content", "rating"]
        widgets = {
            "fullname": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your Full Name"}),
            "headline": forms.TextInput(attrs={"class": "form-control", "placeholder": "What’s most important to know"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "What did you like or dislike? What did you use this product for?"}),
        }
