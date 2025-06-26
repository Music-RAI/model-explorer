import markdown
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm, MLModelForm
from .models import MLModel, Tag
from .views_util import email_contacts

def index(request):
    tags = Tag.objects.all()
    ml_models = MLModel.objects.all()

    context = {}
    if tag_names := request.GET.getlist("tag"):
        for tag_name in tag_names:
            ml_models = ml_models.filter(tags__name=tag_name)

    context.update({"ml_models": ml_models, "tags": tags, "selected_tags": tag_names})
    return render(request, "genmodels/index.html", context)

def add_model(request):
    if request.method == "POST":
        form = MLModelForm(request.POST)
        if form.is_valid():
            form.save()

            name = form.cleaned_data['name']
            email_contacts(
                "Request to add model",
                f"A new model was added: {name}\n\n" + \
                f"Go to the admin panel and review moderated objects.",
                tag="Add model",
            )
            return render(request, "genmodels/add_model_response.html")
    else:
        form = MLModelForm()

    return render(request, "genmodels/add_model_form.html", {"form": form})

def add_model_success(request):
    return render(request, "genmodels/add_model_response.html")

def detail(request, model_id):
    md = markdown.Markdown(extensions=["fenced_code"])

    model = get_object_or_404(MLModel, identifier=model_id)
    model.guide = md.convert(model.guide)

    return render(request, "genmodels/detail.html", {"model": model})

def detail_edit_form(request, model_id):
    model = get_object_or_404(MLModel, identifier=model_id)

    if request.method == "POST":
        form = MLModelForm(request.POST, instance=model)
        if form.is_valid():
            form.save()

            name = form.cleaned_data['name']
            email_contacts(
                "Request to edit model",
                f"{name} model was edited.\n\n" + \
                f"Go to the admin panel and review moderated objects.",
                tag="Edit model",
            )
            return render(request, "genmodels/detail_edit_response.html")
    else:
        form = MLModelForm(instance=model)

    context = {"form": form, "model": model}
    return render(request, "genmodels/detail_edit_form.html", context)

def edit_success(request):
    return render(request, "genmodels/detail_edit_response.html")

def about(request):
    return render(request, "genmodels/about.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            title = form.cleaned_data['title']
            message = form.cleaned_data['message']

            email_contacts(
                title,
                f"From: {name} <{email}>\n\n{message}",
                email,
                "Contact form",
            )

            return render(request, "genmodels/contact_success.html")
    else:
        form = ContactForm()

    return render(request, "genmodels/contact.html", {"form": form})
