from django.db import models

# Create your models here.
from django.db import models


class CyberbullyingReport(models.Model):
    BULLYING_TYPES = [
        ("insult", "Insulting messages"),
        ("threat", "Threats"),
        ("fake_profile", "Fake profile"),
        ("private_content", "Sharing private content"),
        ("exclusion", "Exclusion from online groups"),
        ("rumours", "Spreading rumours"),
        ("other", "Other"),
    ]

    PLATFORMS = [
        ("instagram", "Instagram"),
        ("tiktok", "TikTok"),
        ("facebook", "Facebook"),
        ("snapchat", "Snapchat"),
        ("discord", "Discord"),
        ("gaming", "Online game"),
        ("messaging", "Messaging application"),
        ("other", "Other"),
    ]

    AGE_GROUPS = [
        ("11-12", "11–12"),
        ("13-15", "13–15"),
        ("16-18", "16–18"),
        ("18+", "18+"),
    ]

    bullying_type = models.CharField(
        max_length=30,
        choices=BULLYING_TYPES,
    )

    platform = models.CharField(
        max_length=30,
        choices=PLATFORMS,
    )

    age_group = models.CharField(
        max_length=10,
        choices=AGE_GROUPS,
    )

    asked_for_help = models.BooleanField(default=False)

    description = models.TextField(
        blank=True,
        help_text="Do not enter names or personal information.",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.get_bullying_type_display()} - "
            f"{self.get_platform_display()}"
        )


class Scenario(models.Model):
    question = models.TextField()

    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)

    correct_option = models.CharField(
        max_length=1,
        choices=[
            ("A", "Option A"),
            ("B", "Option B"),
            ("C", "Option C"),
        ],
    )

    explanation = models.TextField()

    def __str__(self):
        return self.question[:60]


class ReportStatistics(models.Model):
    total_reports = models.PositiveIntegerField(default=0)
    reports_with_help = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Report statistics"

    def __str__(self):
        return f"Total reports: {self.total_reports}"