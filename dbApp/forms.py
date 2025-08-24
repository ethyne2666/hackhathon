
from django import forms
from datetime import timedelta, date

TIME_SLOTS = [
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('every_10_days', 'Every 10 Days'),
    ('every_15_days', 'Every 15 Days'),
    ('monthly', 'Monthly'),
    ('every_3_months', 'Every 3 Months'),
]

class ScheduleForm(forms.Form):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'min': date.today().isoformat()})
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'min': date.today().isoformat()})
    )
    frequency = forms.ChoiceField(
        choices=TIME_SLOTS,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        today = date.today()

        if start_date and start_date < today:
            self.add_error("start_date", "Start date cannot be before today.")

        if start_date and end_date:
            # End date must be AFTER start date
            if end_date <= start_date:
                self.add_error("end_date", "End date must be after start date.")
            # End date cannot exceed 1 year from start date
            if end_date > start_date + timedelta(days=365):
                self.add_error("end_date", "End date cannot be more than 1 year from start date.")

        return cleaned_data