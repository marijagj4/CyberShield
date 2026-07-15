from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import CyberbullyingReport, ReportStatistics


def update_statistics():
    statistics, created = ReportStatistics.objects.get_or_create(
        pk=1
    )

    statistics.total_reports = CyberbullyingReport.objects.count()

    statistics.reports_with_help = (
        CyberbullyingReport.objects
        .filter(asked_for_help=True)
        .count()
    )

    statistics.save()


@receiver(post_save, sender=CyberbullyingReport)
def report_created_or_updated(sender, instance, **kwargs):
    update_statistics()


@receiver(post_delete, sender=CyberbullyingReport)
def report_deleted(sender, instance, **kwargs):
    update_statistics()