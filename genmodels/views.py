from django.shortcuts import render

from .models import MLModel

def index(request):
    ml_models = MLModel.objects.all()
    context = {"ml_models": ml_models}
    return render(request, "genmodels/index.html", context)
