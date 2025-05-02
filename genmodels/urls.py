from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:model_id>/", views.detail, name="detail"),
    path("<slug:model_id>/edit/", views.detail_edit, name="detail_edit"),
    path("<slug:model_id>/edit/submit/", views.edit, name="submit_edits"),
]
