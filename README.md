Features of this appointment scheduler:
It can add new appointments like patient name, date and time and reason for visit.
Can display complete list of all scheduled appointments, they are also sorted automatically.
It can be filtered by dates.
Can also remove the exisiting appointment.
Execution of the code:
Save the code as.py
Run the script: Execute the file using the python interpreter.
Key functions:
main(): The primary function that runs the infinite menu loop and handles user input (the main control flow).
add_appointment(): Collects appointment data and performs the crucial schedule conflict check.
list_appoitments(): Displays all appointments, utilizing a sorted() function to organize the output by physician.
list_appointments_by_date(): Takes a date input from the user and uses list comprehension to find and display matching appointments.
cancel_appointment(): Handles the cancellation process, ensuring the user provides a valid appointment number before using the .pop() method
