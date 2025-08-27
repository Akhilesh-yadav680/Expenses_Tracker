from django.urls import path
from . import views, api_views, import_export

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_expense, name="add_expense"),
    path("edit/<int:expense_id>/", views.edit_expense, name="edit_expense"),
    path("delete/<int:expense_id>/", views.delete_expense, name="delete_expense"),
    path("duplicate/<int:expense_id>/", views.duplicate_expense, name="duplicate_expense"),
    path("bulk_delete/", views.bulk_delete, name="bulk_delete"),

    # CSV
    path("export/", import_export.export_csv, name="export_csv"),
    path("import/", import_export.import_csv, name="import_csv"),

    # API
    path("api/summary/", api_views.api_summary, name="api_summary"),
    path("api/by_category/", api_views.api_by_category, name="api_by_category"),
    path("api/by_day/", api_views.api_by_day, name="api_by_day"),
]
