from django.http import JsonResponse
from django.views import View

from .models import Patient
import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class PatientView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            patients = list(Patient.objects.filter(id=id).values())
            if len(patients)>0:
                patient = patients[0]
                datos = {"Message" : "Success" ,"patient":patient}
            else:
                datos = {"Message" : "Patient not found..."}
            return JsonResponse(datos)

        else:
            patients = list(Patient.objects.values())
            if len(patients)>0:
                datos = {"Message" : "Success", "patients":patients}
            else:
                datos = {"Message" : "Patients not found..."}
            return JsonResponse(datos)
    
    def post(self, request):
        JsonData = json.loads(request.body)
        Patient.objects.create(name = JsonData["name"],
                               lastname = JsonData["lastname"],
                               age = JsonData["age"],
                               insurance = JsonData["insurance"])
        datos = {"Message" : "Success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        JsonData = json.loads(request.body)
        patients = list(Patient.objects.filter(id=id).values())
        if len(patients)>0:
            patient = Patient.objects.get(id=id)
            patient.name = JsonData["name"]
            patient.lastname = JsonData["lastname"]
            patient.age = JsonData["age"]
            patient.insurance = JsonData["insurance"]
            patient.save()
            datos = {"Message" : "Success"}
        else:
            datos = {"Message" : "Patient not found..."}
        return JsonResponse(datos)
    
    def delete(slef, request, id):
        patients = list(Patient.objects.filter(id=id).values())
        if len(patients)>0:
            Patient.objects.filter(id=id).delete()
            datos = {"Message" : "Success"}
        else:
            datos = {"Message" : "Patient not found..."}
        return JsonResponse(datos)
