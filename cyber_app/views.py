from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.db.models import Count
from django.shortcuts import redirect, render

from .forms import CyberbullyingReportForm
from .models import CyberbullyingReport, Scenario


def home(request):
    return render(request, "cyber_app/home.html")


def report_incident(request):
    if request.method == "POST":
        form = CyberbullyingReportForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Your anonymous report was submitted successfully.",
            )

            return redirect("report_incident")
    else:
        form = CyberbullyingReportForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "cyber_app/report_incident.html",
        context,
    )


def quiz(request):
    scenarios = Scenario.objects.all()
    results = []

    if request.method == "POST":
        for scenario in scenarios:
            selected_answer = request.POST.get(
                f"scenario_{scenario.id}"
            )

            results.append(
                {
                    "scenario": scenario,
                    "selected_answer": selected_answer,
                    "is_correct": (
                        selected_answer == scenario.correct_option
                    ),
                }
            )

    context = {
        "scenarios": scenarios,
        "results": results,
        "submitted": request.method == "POST",
    }

    return render(
        request,
        "cyber_app/quiz.html",
        context,
    )


def dashboard(request):
    type_statistics = (
        CyberbullyingReport.objects
        .values("bullying_type")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    platform_statistics = (
        CyberbullyingReport.objects
        .values("platform")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    context = {
        "total_reports": CyberbullyingReport.objects.count(),
        "type_statistics": type_statistics,
        "platform_statistics": platform_statistics,
    }

    return render(
        request,
        "cyber_app/dashboard.html",
        context,
    )