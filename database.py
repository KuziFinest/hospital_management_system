import csv
import os

# Automatically create data folder if missing
os.makedirs("data", exist_ok=True)

FILE_PATH = "data/patients.csv"


def save_patient(patient_data):
    file_exists = os.path.isfile(FILE_PATH)

    with open(FILE_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Patient ID",
                "Name",
                "Age",
                "Condition",
                "Priority"
            ])

        writer.writerow(patient_data)