import pandas as pd
from faker import Faker
import datetime
import random

def create_patient_dataset(num_patients=10):
    """
    Generates a realistic patient dataset as a pandas DataFrame.
    Priority is now based on 'Current Status' as requested.
    'Admitted' and 'Discharged' statuses have been removed.
    """
    
    fake = Faker()
    
    # --- New Status-based Priority System ---
    # We use your new 4-item list
    statuses = [
        "Emergency", 
        "Awaiting Surgery", 
        "Under Observation", 
        "Waiting to be Discharged"
    ]
    
    # Map status strings to numeric priorities (for our min-heap)
    priority_map = {
        "Emergency": 1,
        "Awaiting Surgery": 2,
        "Under Observation": 3,
        "Waiting to be Discharged": 4
    }
    
    # --- Base Data Generation ---
    # --- Base Data Generation ---
    patient_ids = [f"P{2024000 + i}" for i in range(1, num_patients+ 1)]
    patient_names = [fake.name() for _ in range(num_patients)]
    
    departments = ["Cardiac", "Ortho", "Pediatrics", "Gynecology", "Dentist", "Neurology", "Oncology"]
    
    # --- Logic for Dates and Status-based Priority ---
    today = datetime.date.today()
    
    priorities = []
    dates_of_admission = []
    days_admitted = []
    current_statuses = []
    patient_departments = []
    
    for _ in range(num_patients):
        # 1. Determine Status first
        # Updated weights for the new 4-status list
        status = random.choices(statuses, weights=[15, 25, 40, 35], k=1)[0]
        current_statuses.append(status)
        
        # 2. Determine Priority based on Status
        priority = priority_map[status]
        priorities.append(priority)

        if status == "Emergency":
        # Rule: Less than 2 days
            days = random.randint(0, 1) 
        elif status == "Awaiting Surgery":
            # Rule: Less than 15 days
            days = random.randint(0, 14) 
        elif status == "Under Observation":
            # Given a logical range (e.g., up to 30 days)
            days = random.randint(1, 30)
        elif status == "Waiting to be Discharged":
            # Can be any length, but implies they've been here a while
            days = random.randint(2, 60) # e.g., 2 to 60 days
        else:
            # Fallback (should not be reached)
            days = random.randint(0, 60)
        
        # Logic for "Discharged" is now removed.
        days_ago = days # Admitted 'days' ago
        
        admission_date = today - datetime.timedelta(days=days_ago)
        dates_of_admission.append(admission_date)
        days_admitted.append(days) # This is now 'length of stay'
        
        # 4. Assign Department
        patient_departments.append(random.choice(departments))

    # --- Create DataFrame with specific column order ---

    data = {
        "patient ID": patient_ids,
        "patient Name": patient_names,
        "Priority": priorities,
        "Department": patient_departments,
        "Date of Admission": dates_of_admission,
        "Days Admitted": days_admitted,
        "Current Status": current_statuses
    }
    
    # Define the column order explicitly (7 columns)

    columns_order = [
        "patient ID", "patient Name", "Priority", "Department", 
        "Date of Admission", "Days Admitted", "Current Status"
    ]
    
    patient_df = pd.DataFrame(data, columns=columns_order)
    return patient_df
