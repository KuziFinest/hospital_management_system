class Patient:
    def __init__(self, patient_id, name, age, condition, priority):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.condition = condition
        self.priority = priority

    def display(self):
        return [self.patient_id, self.name, self.age, self.condition, self.priority]
