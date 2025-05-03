from django.shortcuts import get_object_or_404, render

from .models import MLModel

def index(request):
    ml_models = MLModel.objects.all()
    context = {"ml_models": ml_models}
    return render(request, "genmodels/index.html", context)

def detail(request, model_id):
    model = get_object_or_404(MLModel, pk=model_id)
    return render(request, "genmodels/detail.html", {"model": model})

def detail_edit(request, model_id):
    model = get_object_or_404(MLModel, pk=model_id)
    return render(request, "genmodels/detail_edit.html", {"model": model})

def edit(request, model_id):
    return render(request, "genmodels/detail_edit_response.html")
