# 🏥 Hospital Patient Priority Queue System

> **Data Structures — Semester 1 Project**
> A hospital consultation ordering system built using a custom **Min-Heap Priority Queue** and **Merge Sort**, implemented entirely in Python.

---

## 📌 About the Project

In a hospital, patients must be attended to based on clinical urgency — not arrival order. This project implements a **triage and consultation ordering system** using two fundamental data structure algorithms:

- **Min-Heap (Priority Queue)** — selects the next patient to be consulted based on urgency
- **Merge Sort** — sorts patients for administrative reports by any field (name, admission date, etc.)
- **Synthetic Dataset Generator** — generates realistic patient data for testing using the `Faker` library

---

## 🎯 Objective

To demonstrate how classic data structure algorithms can solve a real-world hospital workflow problem — ensuring doctors always attend to the most critical patient first.

---

## ⚙️ How the Priority System Works

| Priority | Clinical Status |
|---|---|
| 1 (Highest) | Emergency |
| 2 | Awaiting Surgery |
| 3 | Under Observation |
| 4 (Lowest) | Waiting to be Discharged |

The Min-Heap always ensures the **lowest priority number** (most critical patient) is served first.

---

## 🗂️ File Structure

```
hospital-priority-queue-python/
│
├── Executable_file.ipynb          # 🔑 Main notebook — run this to see the full system
├── Dataset_Creation.py            # Generates synthetic hospital patient dataset
├── Dataset_Creation.ipynb         # Notebook version of dataset creation
├── heap_sort.py                   # Custom Min-Heap (heap_push & heap_pop) implementation
├── heap_sort.ipynb                # Notebook version of heap sort
├── Merge_Sort.py                  # Recursive Merge Sort implementation
└── Full_Hospital_Priority_Queue_Documentation_AnilaM.docx  # Full project documentation
```

---

## 🛠️ Tools & Technologies

- **Language:** Python 3.8+
- **Libraries:** `pandas`, `faker`, `datetime`, `random`
- **Environment:** Jupyter Notebook

---

## 📊 Dataset Columns

The generated patient dataset contains 7 columns:

| Column | Description |
|---|---|
| `patient ID` | Unique patient identifier (e.g., C2024001) |
| `patient Name` | Faker-generated full name |
| `Priority` | Integer 1–4 (mapped from Current Status) |
| `Department` | Hospital department (Cardiac, Ortho, Pediatrics, etc.) |
| `Date of Admission` | Auto-calculated based on status |
| `Days Admitted` | Length of stay in hospital |
| `Current Status` | Emergency / Awaiting Surgery / Under Observation / Waiting to be Discharged |

---

## 🔍 Algorithms Implemented

### 1. Min-Heap Priority Queue (`heap_sort.py`)
- `heap_push(heap, item)` — Inserts a patient and performs **sift-up** to maintain heap order
- `heap_pop(heap)` — Removes the highest-priority patient (root) and performs **sift-down**
- **Time Complexity:** O(log n) per operation

### 2. Merge Sort (`Merge_Sort.py`)
- `merge_sort(arr, key_index)` — Recursively sorts a list of patient tuples by any key
- `merge(left, right, key_index)` — Merges two sorted halves
- **Time Complexity:** O(n log n) | **Space Complexity:** O(n)

---

## ▶️ How to Run

**1. Install dependencies:**
```bash
pip install pandas faker jupyter
```

**2. Clone this repository:**
```bash
git clone https://github.com/YOUR_USERNAME/hospital-priority-queue-python.git
cd hospital-priority-queue-python
```

**3. Open the main notebook:**
```bash
jupyter notebook Executable_file.ipynb
```

**4. Run all cells in order** — the notebook will:
- Generate a patient dataset
- Load patients into the Min-Heap
- Simulate doctor consultations (popping patients by priority)
- Sort and display reports using Merge Sort

---

## 📈 Sample Output

```
--- Patients Dataset ---
| patient ID | patient Name   | Priority | Department | Current Status           |
|------------|----------------|----------|------------|--------------------------|
| C2024001   | Kevin Steele   | 1        | Dentist    | Emergency                |
| C2024005   | April Duarte   | 1        | Dentist    | Emergency                |
| C2024003   | Andrew Wood    | 2        | Dentist    | Awaiting Surgery         |
| C2024004   | Jeffrey Graham | 3        | Oncology   | Under Observation        |
| C2024002   | Kaitlyn Mann   | 4        | Gynecology | Waiting to be Discharged |

--- Processing Top Priority Patients ---
✔ Next patient: Kevin Steele [EMERGENCY]
✔ Next patient: April Duarte [EMERGENCY]
...
```

---

## 📄 Documentation

Full project documentation (abstract, algorithm analysis, complexity analysis, test cases, and future improvements) is available in:
📎 `Full_Hospital_Priority_Queue_Documentation_AnilaM.docx`

---

## 🚀 Possible Extensions

- Integrate with a real database for persistence
- Add a web dashboard for clinicians
- Implement O(n) heapify for bulk patient loading
- Add real-time priority updates based on vitals

---

*Submitted as part of the Data Structures course —  MSc Applied Statistics with Data Analytics*
