from django.urls import path

from schemavalidator.views import ValidateSchemaView

urlpatterns = [
    path("schema", ValidateSchemaView.as_view(), name="schema.validator"),
]
