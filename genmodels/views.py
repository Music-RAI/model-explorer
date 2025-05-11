from django.shortcuts import get_object_or_404, redirect, render

from .forms import MLModelForm
from .models import MLModel, Tag

def index(request):
    tags = Tag.objects.all()
    context = {}
    if tag_name := request.GET.get("tag"):
        tag = Tag.objects.get(name=tag_name)
        ml_models = MLModel.objects.filter(tags=tag)
        context["selected_tag"] = tag_name
    else:
        ml_models = MLModel.objects.all()
        context["selected_tag"] = ""
    context.update({"ml_models": ml_models, "tags": tags})
    return render(request, "genmodels/index.html", context)

def add_model(request):
    if request.method == "POST":
        form = MLModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "genmodels/add_model_response.html")
    else:
        form = MLModelForm()

    return render(request, "genmodels/add_model_form.html", {"form": form})

def add_model_success(request):
    return render(request, "genmodels/add_model_response.html")

def detail(request, model_id):
    model = get_object_or_404(MLModel, pk=model_id)
    return render(request, "genmodels/detail.html", {"model": model})

def detail_edit(request, model_id):
    model = get_object_or_404(MLModel, pk=model_id)
    return render(request, "genmodels/detail_edit.html", {"model": model})

def detail_edit_form(request, model_id):
    model = get_object_or_404(MLModel, pk=model_id)

    if request.method == "POST":
        form = MLModelForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
            return render(request, "genmodels/detail_edit_response.html")
    else:
        form = MLModelForm(instance=model)

    return render(request, "genmodels/detail_edit_form.html", {"form": form})

def edit_success(request):
    return render(request, "genmodels/detail_edit_response.html")
