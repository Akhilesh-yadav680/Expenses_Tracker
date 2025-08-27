from datetime import timedelta
from django.utils.timezone import now

def _get_date_range(filter_by):
    today = now().date()
    if filter_by == "today":
        return today, today
    elif filter_by == "week":
        return today - timedelta(days=7), today
    elif filter_by == "month":
        return today - timedelta(days=30), today
    return today - timedelta(days=30), today   # default last 30 days

def _apply_filters(queryset, request):
    # Text search
    q = request.GET.get("q", "").strip()
    if q:
        queryset = queryset.filter(title__icontains=q)

    # Sorting
    sort = request.GET.get("sort", "-date")
    if sort:
        queryset = queryset.order_by(sort)

    # Date range
    filter_by = request.GET.get("filter_by", "month")  # default last 30 days
    start_date, end_date = _get_date_range(filter_by)
    queryset = queryset.filter(date__range=(start_date, end_date))

    return queryset, (start_date, end_date), q, sort
