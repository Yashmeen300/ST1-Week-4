class Patient:
    def __init__(self, patient_id: str, name: str) -> None:
        if not patient_id.strip():
            raise ValueError("Patient ID cannot be empty.")

        if not name.strip():
            raise ValueError("Patient name cannot be empty.")

        self.patient_id = patient_id
        self.name = name

    def __repr__(self) -> str:
        return f"Patient(patient_id='{self.patient_id}', name='{self.name}')"
