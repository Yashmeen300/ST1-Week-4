#F)

if __name__ == "__main__":

    print("=== SmartCare Manual Behaviour Checks ===")

    # TEST 1 - Create valid objects
    print("\nTEST 1: Create valid objects")

    patient = Patient("P001", "Sarah Smith")

    practitioner = Practitioner(
        "PR001",
        "Dr John Lee",
        "General Practice"
    )

    appointment = Appointment(
        "A001",
        patient,
        practitioner,
        datetime(2026, 10, 10, 10, 30)
    )

    print("Patient created:", patient.patient_id, patient.name)
    print(
        "Practitioner created:",
        practitioner.practitioner_id,
        practitioner.name,
        practitioner.specialty
    )
    print("Appointment created:", appointment.appointment_id)
    print("Initial status:", appointment.status.value)

    # TEST 2 - Invalid patient input
    print("\nTEST 2: Invalid patient input")

    try:
        Patient("", "Sarah Smith")
    except ValueError as error:
        print("PASS - Invalid input rejected:", error)

    # TEST 3 - Cancel a scheduled appointment
    print("\nTEST 3: Cancel scheduled appointment")

    appointment.cancel()

    print("PASS - Appointment cancelled")
    print("New status:", appointment.status.value)

    # TEST 4 - Attempt illegal repeated cancellation
    print("\nTEST 4: Cancel appointment again")

    try:
        appointment.cancel()
    except ValueError as error:
        print("PASS - Repeated cancellation rejected:", error)

    print("\n=== Testing Complete ===")
