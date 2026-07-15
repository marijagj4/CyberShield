from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("report/", views.report_incident, name="report_incident"),
    path("quiz/", views.quiz, name="quiz"),
    path("dashboard/", views.dashboard, name="dashboard"),
]