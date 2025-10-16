from django.urls import path
from .views import PatientView

urlpatterns = [
    path("patients/", PatientView.as_view(), name="patients_list"),
    path("patients/<int:id>", PatientView.as_view(), name="patients_process")
]