from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Sum
from .models import Expense
from .forms import ExpenseForm
from .utils import _apply_filters

def home(request):
    """Dashboard with filters, charts, pagination, and stats."""
    qs, (start, end), q, sort = _apply_filters(Expense.objects.all(), request)

    total = qs.aggregate(s=Sum("amount"))["s"] or 0
    days = (end - start).days + 1
    avg_daily = total / days if days else 0
    by_category = qs.values("category").annotate(total=Sum("amount")).order_by("-total")

    page_size = max(int(request.GET.get("page_size", 10)), 1)
    paginator = Paginator(qs, page_size)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(request, "expenses/home.html", {
        "expenses": page_obj, "page_obj": page_obj, "paginator": paginator,
        "total": total, "avg_daily": avg_daily, "by_category": by_category,
        "start": start, "end": end, "q": q, "sort": sort, "page_size": page_size,
        "sort_options": [("-date", "Newest"), ("date", "Oldest"),
                         ("-amount", "Amount ↓"), ("amount", "Amount ↑"),
                         ("title", "Title A→Z"), ("-title", "Title Z→A"),
                         ("category", "Category A→Z"), ("-category", "Category Z→A"),
                         ("id", "ID ↑"), ("-id", "ID ↓")]
    })

def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ExpenseForm()
    return render(request, "expenses/add_expense.html", {"form": form})

def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ExpenseForm(instance=expense)
    return render(request, "expenses/edit_expense.html", {"form": form, "expense": expense})

def delete_expense(request, expense_id):
    get_object_or_404(Expense, id=expense_id).delete()
    return redirect("home")

def duplicate_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    expense.pk = None
    expense.save()
    return redirect("home")

def bulk_delete(request):
    ids = request.POST.getlist("ids")
    if ids:
        Expense.objects.filter(id__in=ids).delete()
    return redirect("home")
