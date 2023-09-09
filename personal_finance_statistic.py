import csv
import re
from datetime import datetime

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Creating a dictionary to represent the days of the week
week_days = {
    "Monday": {"spent_amount": 0.0, "day_type": "working"},
    "Tuesday": {"spent_amount": 0.0, "day_type": "working"},
    "Wednesday": {"spent_amount": 0.0, "day_type": "working"},
    "Thursday": {"spent_amount": 0.0, "day_type": "working"},
    "Friday": {"spent_amount": 0.0, "day_type": "working"},
    "Saturday": {"spent_amount": 0.0, "day_type": "weekend"},
    "Sunday": {"spent_amount": 0.0, "day_type": "weekend"}
}

date_pattern = r'\d{1,2}-(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-\d{4}'


def update_spent_amount(day_structure, day_name, amount):
    if day_name in day_structure:
        day_structure[day_name]["spent_amount"] += amount


def build_monthly_stats(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            match = re.match(date_pattern, row[0])
            if match:
                date_obj = datetime.strptime(match.group(), '%d-%b-%Y')
                # Get the day of the week as an integer (0 = Monday, 6 = Sunday)
                day_index = date_obj.weekday()
                # Get the corresponding day name
                day_name = days_of_week[day_index]
                update_spent_amount(week_days, day_name, float(row[1]))
    for day, data in week_days.items():
        print(f"{day}, Spent Amount: {data['spent_amount']}")


