import csv
from faker import Faker
import random

fake = Faker()

with open("fake_weather_data.csv", "w", newline="") as csvfile:
    # fieldnames = ["Name", "Date", "Country"]
    fieldnames = ["Date", "Country", "Weather"]
    
    weather_conditions = ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Windy', 'Stormy']

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for _ in range(5000):
        writer.writerow(
            {
                "Date": fake.date_between(start_date="-90d", end_date="today"),
                "Country": fake.country(),
                "Weather": random.choice(weather_conditions)
            }
        )
