appointments = []

def add_appointment():
    print("\nProvide appointment details:")
    patient = input("Patient's name: ")
    doctor = input("Doctor's name: ")
    date = input("Date (DD-MM-YYYY): ")
    time = input("Time (HH:MM): ")
    reason = input("Reason for visit: ")

    for a in appointments:
        if a["doctor"].lower() == doctor.lower() and a["date"] == date and a["time"] == time:
            print("The doctor already has an appointment at that time.")
            return

    appt = {"patient": patient, "doctor": doctor, "date": date, "time": time, "reason": reason}
    appointments.append(appt)
    print("Appointment is booked successfully.")

def list_appointments():
    if not appointments:
        print("\nNo appointment is scheduled.")
        return
    print("\nAll appointments:")
    for i, a in enumerate(appointments, start=1):
        print(f"{i}. {a['date']} {a['time']} | Dr. {a['doctor']} with {a['patient']} | {a['reason']}")

def list_appointments_by_date():
    if not appointments:
        print("\nNo appointments scheduled.")
        return
    date = input("Enter date (DD-MM-YYYY): ")
    found = [a for a in appointments if a["date"] == date]
    if not found:
        print("\nNo appointments on this date.")
        return
    print(f"\nAppointments on {date}:")
    for i, a in enumerate(found, start=1):
        print(f"{i}. {a['date']} {a['time']} | Dr. {a['doctor']} with {a['patient']} | {a['reason']}")

def cancel_appointment():
    if not appointments:
        print("\nNo appointments to cancel.")
        return
    list_appointments()
    try:
        n = int(input("Enter appointment number to cancel: "))
    except ValueError:
        print("Please enter a number.")
        return
    if n < 1 or n > len(appointments):
        print("Invalid appointment number.")
        return
    removed = appointments.pop(n - 1)
    print(f"Cancelled: {removed['date']} {removed['time']} | Dr. {removed['doctor']} with {removed['patient']}")

def main():
    while True:
        print("\n=== Hospital Appointment Scheduler ===")
        print("1. Add appointment")
        print("2. View all appointments")
        print("3. View appointments by date")
        print("4. Cancel appointment")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_appointment()
        elif choice == "2":
            list_appointments()
        elif choice == "3":
            list_appointments_by_date()
        elif choice == "4":
            cancel_appointment()
        elif choice == "5":
            print("Bye.")
            break
        else:
            print("Not a valid choice.")

if __name__ == "__main__":

main()

    main()
