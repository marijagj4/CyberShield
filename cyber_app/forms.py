from django import forms

from .models import CyberbullyingReport


class CyberbullyingReportForm(forms.ModelForm):
    class Meta:
        model = CyberbullyingReport

        fields = [
            "bullying_type",
            "platform",
            "age_group",
            "asked_for_help",
            "description",
        ]

        labels = {
            "bullying_type": "What happened?",
            "platform": "Where did it happen?",
            "age_group": "Age group",
            "asked_for_help": "Did you ask someone for help?",
            "description": "Anonymous description",
        }

        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": (
                        "Describe the situation without names, "
                        "usernames, phone numbers or addresses."
                    ),
                }
            ),
        }

    def clean_description(self):
        description = self.cleaned_data.get("description", "").strip()

        forbidden_words = [
            "phone number",
            "address",
            "username",
            "full name",
        ]

        for word in forbidden_words:
            if word in description.lower():
                raise forms.ValidationError(
                    "Do not include personal or identifying information."
                )

        return description