# Copyright (c) 2026 Ville Heikkiniemi, Luka Hietala, Luukas Kola
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

"""
Task G: Class-based implementation
Refactoring from list-based to object-based data structure
"""

from datetime import datetime


class Reservation:
    """Represents a single reservation"""

    def __init__(self, reservation_id: int, name: str, email: str, phone: str,
                 date, time, duration: int, price: float,
                 confirmed: bool, resource: str, created):
        self.reservation_id = reservation_id
        self.name = name
        self.email = email
        self.phone = phone
        self.date = date
        self.time = time
        self.duration = duration
        self.price = price
        self.confirmed = confirmed
        self.resource = resource
        self.created = created

    def is_confirmed(self) -> bool:
        """Check if reservation is confirmed"""
        return self.confirmed

    def is_long(self) -> bool:
        """Check if reservation is 3+ hours"""
        return self.duration >= 3

    def total_price(self) -> float:
        """Calculate total price (duration * price)"""
        return self.duration * self.price


def convert_reservation(data: list[str]) -> Reservation:
    """
    Convert reservation data from list to Reservation object

    Parameters:
     data (list[str]): Raw reservation data fields

    Returns:
     Reservation: Reservation object with proper types
    """
    return Reservation(
        reservation_id=int(data[0]),
        name=data[1],
        email=data[2],
        phone=data[3],
        date=datetime.strptime(data[4], "%Y-%m-%d").date(),
        time=datetime.strptime(data[5], "%H:%M").time(),
        duration=int(data[6]),
        price=float(data[7]),
        confirmed=True if data[8].strip() == 'True' else False,
        resource=data[9],
        created=datetime.strptime(data[10].strip(), "%Y-%m-%d %H:%M:%S"),
    )


def fetch_reservations(reservation_file: str) -> list[Reservation]:
    """
    Read reservations from file

    Parameters:
     reservation_file (str): Path to reservations file

    Returns:
     list[Reservation]: List of Reservation objects (no header row)
    """
    reservations: list[Reservation] = []
    with open(reservation_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                fields = line.split("|")
                reservations.append(convert_reservation(fields))
    return reservations


def confirmed_reservations(reservations: list[Reservation]) -> None:
    """Print confirmed reservations"""
    for reservation in reservations:
        if reservation.is_confirmed():
            print(f'- {reservation.name}, {reservation.resource}, {reservation.date.strftime("%d.%m.%Y")} at {reservation.time.strftime("%H.%M")}')


def long_reservations(reservations: list[Reservation]) -> None:
    """Print long reservations (3+ hours)"""
    for reservation in reservations:
        if reservation.is_long():
            print(f'- {reservation.name}, {reservation.date.strftime("%d.%m.%Y")} at {reservation.time.strftime("%H.%M")}, duration {reservation.duration} h, {reservation.resource}')


def confirmation_statuses(reservations: list[Reservation]) -> None:
    """Print confirmation status for each reservation"""
    for reservation in reservations:
        status = "Confirmed" if reservation.is_confirmed() else "NOT Confirmed"
        print(f'{reservation.name} → {status}')


def confirmation_summary(reservations: list[Reservation]) -> None:
    """Print summary of confirmed vs not confirmed"""
    confirmed_count = sum(1 for r in reservations if r.is_confirmed())
    not_confirmed_count = len(reservations) - confirmed_count
    print(f'- Confirmed reservations: {confirmed_count} pcs\n- Not confirmed reservations: {not_confirmed_count} pcs')


def total_revenue(reservations: list[Reservation]) -> None:
    """Print total revenue from confirmed reservations"""
    revenue = sum(r.total_price() for r in reservations if r.is_confirmed())
    print(f'Total revenue from confirmed reservations: {revenue:.2f} €'.replace('.', ','))


def main() -> None:
    """Main program"""
    reservations = fetch_reservations("reservations.txt")
    print("1) Confirmed Reservations")
    confirmed_reservations(reservations)
    print("2) Long Reservations (≥ 3 h)")
    long_reservations(reservations)
    print("3) Reservation Confirmation Status")
    confirmation_statuses(reservations)
    print("4) Confirmation Summary")
    confirmation_summary(reservations)
    print("5) Total Revenue from Confirmed Reservations")
    total_revenue(reservations)


if __name__ == "__main__":
    main()
