import pytest
from hospital import Hospital

# --- EXISTING TEST CASES ---

def test_initial_capacity():
    h = Hospital(5)
    assert h.available_beds() == 5

def test_admit_patient_success():
    h = Hospital(2)
    success, msg = h.admit_patient(101, "Ali", 45)
    assert success is True
    assert msg == "Patient admitted successfully"
    assert h.available_beds() == 1

def test_hospital_full():
    """Verifies that the system correctly rejects patients when at capacity."""
    h = Hospital(1)
    h.admit_patient(101, "Ali", 45)
    success, msg = h.admit_patient(102, "Sara", 30)
    assert success is False
    assert msg == "Hospital is at full capacity"

def test_discharge_patient_success():
    h = Hospital(3)
    h.admit_patient(101, "Ali", 45)
    success, msg = h.discharge_patient(101)
    assert success is True
    assert msg == "Patient discharged successfully"
    assert h.available_beds() == 3

def test_invalid_discharge():
    h = Hospital(2)
    success, msg = h.discharge_patient(999) 
    assert success is False
    assert msg == "Patient not found"

# --- TASK 4: EXPANDED TEST CASES ---

def test_admit_duplicate_patient():
    """Edge Case: Ensures a patient cannot be admitted twice simultaneously."""
    h = Hospital(3)
    h.admit_patient(101, "Ali", 45)
    success, msg = h.admit_patient(101, "Ali", 45)
    assert success is False
    assert msg == "Patient is already currently admitted"

def test_discharge_already_discharged():
    """Edge Case: Ensures a patient cannot be discharged more than once."""
    h = Hospital(3)
    h.admit_patient(101, "Ali", 45)
    h.discharge_patient(101)
    success, msg = h.discharge_patient(101)
    assert success is False
    assert msg == "Patient already discharged"

def test_get_patient_info_valid():
    """Logic Check: Verifies data integrity of stored patient info."""
    h = Hospital(3)
    h.admit_patient(50, "Zain", 22)
    info = h.get_patient_info(50)
    assert info["name"] == "Zain"
    assert info["status"] == "Admitted"

def test_complex_workflow():
    """Integration Check: Multiple admissions and discharges to verify bed count stability."""
    h = Hospital(5)
    h.admit_patient(1, "A", 20) # 4 left
    h.admit_patient(2, "B", 30) # 3 left
    h.admit_patient(3, "C", 40) # 2 left
    h.discharge_patient(1)      # 3 left
    h.admit_patient(4, "D", 50) # 2 left
    assert h.available_beds() == 2