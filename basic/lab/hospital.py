class Hospital:
    def __init__(self, capacity):
        self.capacity = capacity
        self.patients = {}  # patient_id -> patient_info

    def admit_patient(self, patient_id, name, age):
        """Admits a patient if beds are available."""
        active_patients = sum(1 for p in self.patients.values() if p["status"] == "Admitted")
        
        # FIXED: Capacity check restored to prevent over-admitting
        if active_patients >= self.capacity:  
            return False, "Hospital is at full capacity"
        
        if patient_id in self.patients and self.patients[patient_id]["status"] == "Admitted":
            return False, "Patient is already currently admitted"
        
        self.patients[patient_id] = {"name": name, "age": age, "status": "Admitted"}
        return True, "Patient admitted successfully"

    def discharge_patient(self, patient_id):
        """Discharges a currently admitted patient."""
        if patient_id not in self.patients:
            return False, "Patient not found"
        
        if self.patients[patient_id]["status"] == "Discharged":
            return False, "Patient already discharged"
        
        self.patients[patient_id]["status"] = "Discharged"
        return True, "Patient discharged successfully"

    def get_patient_info(self, patient_id):
        """Retrieves patient information by ID."""
        return self.patients.get(patient_id, None)

    def available_beds(self):
        """Returns the number of available beds."""
        active_patients = sum(1 for p in self.patients.values() if p["status"] == "Admitted")
        return self.capacity - active_patients