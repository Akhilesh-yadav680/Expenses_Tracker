import csv
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Expense

def export_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="expenses.csv"'
    writer = csv.writer(response)
    writer.writerow(["Date", "Title", "Category", "Amount"])
    for exp in Expense.objects.all().order_by("-date"):
        writer.writerow([exp.date, exp.title, exp.category, exp.amount])
    return response

def import_csv(request):
    if request.method == "POST" and request.FILES.get("file"):
        file = request.FILES["file"].read().decode("utf-8").splitlines()
        for row in csv.DictReader(file):
            Expense.objects.create(
                date=row["Date"], title=row["Title"],
                category=row["Category"], amount=row["Amount"]
            )
        return redirect("home")
    return redirect("home")
