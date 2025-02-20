import csv
from faker import Faker

fake = Faker()

with open("fake_login_data.csv", "w", newline="") as csvfile:
    fieldnames = ["Name", "Date", "Country"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for _ in range(5000):
        writer.writerow(
            {
                "Name": fake.name(),
                "Date": fake.date_between(start_date="-90d", end_date="today"),
                "Country": fake.country(),
            }
        )
