# SmartCare Stage 1 Prototype

# Create an empty list to store appointments
appointments = []


# Function used to create an appointment
def book_appointment(patient_name, practitioner_name, appointment_time):

    # Check that a patient name has been entered
    if not patient_name:
        raise ValueError("Patient name cannot be empty")

    # Controlled improvement:
    # Check that an appointment time has been entered
    if not appointment_time:
        raise ValueError("Appointment time cannot be empty")

    # Store the appointment information in a dictionary
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    # Add the appointment to the appointments list
    appointments.append(appointment)


# Function used to display all appointments
def display_appointments():

    # Check whether there are any appointments
    if not appointments:
        print("No appointments recorded.")
        return

    # Display each appointment
    for appointment in appointments:
        print(
            f"Patient: {appointment['patient']} | "
            f"Practitioner: {appointment['practitioner']} | "
            f"Time: {appointment['time']}"
        )


# Display welcome message for users
print("Welcome to SmartCare: Community Clinic Appointment Booking System!")


# First appointment
book_appointment(
    "Alice Smith",
    "Dr. John Doe",
    "2024-07-20 10:00 AM"
)


# Second appointment
book_appointment(
    "Bob Johnson",
    "Dr. Jane Roe",
    "2024-07-20 11:30 AM"
)


# Display the appointments
display_appointments()
