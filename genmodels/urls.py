from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add-model/", views.add_model, name="add_model"),
    path("add-model/submit", views.add_model_success, name="add_model_success"),
    path("<slug:model_id>/", views.detail, name="detail"),
    path("<slug:model_id>/edit/", views.detail_edit_form, name="detail_edit_form"),
    path("<slug:model_id>/edit/submit/", views.edit_success, name="edit_success"),
]
