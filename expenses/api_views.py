from django.http import JsonResponse
from django.db.models import Sum
from .models import Expense
from .utils import _apply_filters

def api_summary(request):
    qs, _, _, _ = _apply_filters(Expense.objects.all(), request)
    total = qs.aggregate(s=Sum("amount"))["s"] or 0
    return JsonResponse({"total": total})

def api_by_category(request):
    qs, _, _, _ = _apply_filters(Expense.objects.all(), request)
    data = list(qs.values("category").annotate(total=Sum("amount")))
    return JsonResponse(data, safe=False)

def api_by_day(request):
    qs, _, _, _ = _apply_filters(Expense.objects.all(), request)
    data = list(qs.values("date").annotate(total=Sum("amount")).order_by("date"))
    return JsonResponse(data, safe=False)
