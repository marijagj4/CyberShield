from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import (
    CyberbullyingReport,
    ReportStatistics,
    Scenario,
)


@admin.register(CyberbullyingReport)
class CyberbullyingReportAdmin(admin.ModelAdmin):
    list_display = (
        "bullying_type",
        "platform",
        "age_group",
        "asked_for_help",
        "created_at",
    )

    list_filter = (
        "bullying_type",
        "platform",
        "age_group",
        "asked_for_help",
    )

    search_fields = ("description",)

    readonly_fields = ("created_at",)


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    list_display = (
        "short_question",
        "correct_option",
    )

    search_fields = ("question",)

    def short_question(self, obj):
        return obj.question[:60]

    short_question.short_description = "Question"


@admin.register(ReportStatistics)
class ReportStatisticsAdmin(admin.ModelAdmin):
    list_display = (
        "total_reports",
        "reports_with_help",
        "last_updated",
    )

    readonly_fields = (
        "total_reports",
        "reports_with_help",
        "last_updated",
    )

    def has_add_permission(self, request):
        return not ReportStatistics.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False