from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["title", "amount", "category", "date"]  # ✅ date included
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"})  # HTML5 date picker
        }
