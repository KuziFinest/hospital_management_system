from patient import Patient
from billing import generate_bill
from database import save_patient
import heapq

priority_queue = []


def add_patient():
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = input("Enter Age: ")
    condition = input("Enter Condition: ")
    priority = int(input("Enter Priority (1-Emergency, 2-Serious, 3-Regular): "))

    patient = Patient(patient_id, name, age, condition, priority)

    heapq.heappush(priority_queue, (priority, patient))

    save_patient(patient.display())

    print("Patient Added Successfully")


def view_patients():
    if len(priority_queue) == 0:
        print("No patients available")
    else:
        print("Patient Queue:")
        for item in priority_queue:
            print(item[1].display())


def next_patient():
    if len(priority_queue) == 0:
        print("No patients in queue")
    else:
        patient = heapq.heappop(priority_queue)
        print("Next Patient:")
        print(patient[1].display())


def billing_system():
    consultation = float(input("Consultation Fee: "))
    medicine = float(input("Medicine Fee: "))
    tests = float(input("Test Fee: "))

    total = generate_bill(consultation, medicine, tests)

    print(f"Total Bill: ₹{total}")


def menu():
    while True:
        print("===== Hospital Management System =====")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Call Next Patient")
        print("4. Billing")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == '1':
            add_patient()

        elif choice == '2':
            view_patients()

        elif choice == '3':
            next_patient()

        elif choice == '4':
            billing_system()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice")


menu()