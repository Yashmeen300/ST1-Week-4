#B)
#AI OFF
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


#C)
#AI OFF
class Practitioner:
    def __init__(
        self,
        practitioner_id: str,
        name: str,
        specialty: str
    ) -> None:

        if not practitioner_id.strip():
            raise ValueError("Practitioner ID cannot be empty.")

        if not name.strip():
            raise ValueError("Practitioner name cannot be empty.")

        if not specialty.strip():
            raise ValueError("Specialty cannot be empty.")

        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty

    def __repr__(self) -> str:
        return (
            f"Practitioner(practitioner_id='{self.practitioner_id}', "
            f"name='{self.name}', specialty='{self.specialty}')"
        )


#D)
#AI ON
from datetime import datetime
from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    CANCELLED = "Cancelled"


class Appointment:
    def __init__(
        self,
        appointment_id: str,
        patient: Patient,
        practitioner: Practitioner,
        date_time: datetime
    ) -> None:

        if not appointment_id.strip():
            raise ValueError("Appointment ID cannot be empty.")

        if not isinstance(patient, Patient):
            raise TypeError("patient must be a Patient object.")

        if not isinstance(practitioner, Practitioner):
            raise TypeError("practitioner must be a Practitioner object.")

        if not isinstance(date_time, datetime):
            raise TypeError("date_time must be a datetime object.")

        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date_time = date_time

        self._status = AppointmentStatus.SCHEDULED

    @property
    def status(self) -> AppointmentStatus:
        return self._status

    def cancel(self) -> None:
        if self._status == AppointmentStatus.CANCELLED:
            raise ValueError("Appointment is already cancelled.")

        self._status = AppointmentStatus.CANCELLED

    def __repr__(self) -> str:
        return (
            f"Appointment(appointment_id='{self.appointment_id}', "
            f"patient={self.patient.name}, "
            f"practitioner={self.practitioner.name}, "
            f"date_time={self.date_time}, "
            f"status='{self._status.value}')"
        )
