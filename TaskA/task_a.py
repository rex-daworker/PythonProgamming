from datetime import datetime
# Imports the datetime class so we can convert date and time strings into real date/time objects.


def main():
    reservations = "reservations.txt"
    # This sets the filename we want to read, in the same folder as task_a.py.

    # Open the file and read its content
    with open(reservations, "r", encoding="utf-8") as f:
        reservation = f.read().strip()
        # Opens the file, reads the entire line, removes extra spaces/newlines.

    # Print the reservation to the console
    #print(reservation)
    # This would show the raw line from the file, but it's commented out.

    # Try these
    #print(reservation.split('|'))
    # This would show the list created by splitting the line at each '|'.

    reservationId = int(reservation.split('|')[0])
    # Takes the first field (index 0), converts it to an integer.
    print(f"Reservation number: {reservationId}")
    # Prints the reservation number.

    booker = reservation.split('|')[1]
    # Takes the second field (index 1), the booker's name.
    print(f"Booker: {booker}")
    # Prints the booker's name.
    

    day = datetime.strptime(reservation.split('|')[2], "%Y-%m-%d").date()
    # Takes the third field (index 2), converts the string "YYYY-MM-DD" into a real date object.
    finnish_day = day.strftime("%d.%m.%Y")
    # Formats the date into Finnish style: DD.MM.YYYY
    print(f"Date: {finnish_day}")
    # Prints the formatted date.

    time = datetime.strptime(reservation.split('|')[3], "%H:%M").time()
    # Takes the fourth field (index 3), converts "HH:MM" into a real time object.
    finnish_time = time.strftime("%H.%M")
    # Formats the time into Finnish style: HH.MM
    print(f"Start time: {finnish_time}")
    # Prints the formatted time.

    number_of_hours = int(reservation.split('|')[4])
    # Takes the fifth field (index 4), converts it to an integer.
    print(f"Number of hours: {number_of_hours}")
    # Prints the number of hours.

    hourly_price = float(reservation.split('|')[5])
    # Takes the sixth field (index 5), converts it to a float.
    print(f"Hourly price: {hourly_price:.2f} €".replace('.', ','))
    # Formats the price to 2 decimals and replaces '.' with ',' for Finnish formatting.

    total_price = hourly_price * number_of_hours
    # Calculates total price by multiplying hours × hourly price.
    print(f"Total price: {total_price:.2f} €".replace('.', ','))
    # Prints the total price in Finnish format.

    paid = reservation.split('|')[6]
    # Takes the seventh field (index 6), which is "True" or "False".
    print(f"Paid: {'Yes' if paid == 'True' else 'No'}")
    # Prints Yes if True, No if False.

    resource = reservation.split('|')[7]
    # Takes the eighth field (index 7), the location or resource name.
    print(f"Location: {resource}")
    # Prints the location.

    phone = reservation.split('|')[8]
    # Takes the ninth field (index 8), the phone number.
    print(f"Phone: {phone}")
    # Prints the phone number.

    email = reservation.split('|')[9]
    # Takes the tenth field (index 9), the email address.
    print(f"Email: {email}")
    # Prints the email.


if __name__ == "__main__":
    main()
# This ensures the main() function runs when you execute the script.
