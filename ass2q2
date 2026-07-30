
vaccination_center.py

Interactive program to track vaccinated individuals and:
 - count fully vaccinated individuals
 - display senior citizens (age >= 60)
 - calculate percentage of fully vaccinated people
 - find the most used vaccine
 - display records sorted by age

Assumptions:
 - By default, vaccines require 2 doses to be 'fully vaccinated'.
 - Single-dose vaccines are recognized by name (J&J, Janssen, Johnson&Johnson).
"""

from dataclasses import dataclass, asdict
from collections import Counter
from typing import List, Dict

SINGLE_DOSE_VACCINES = {"j&j", "janssen", "johnson&johnson"}

@dataclass
class Record:
    name: str
    age: int
    vaccine: str
    doses: int

def is_fully_vaccinated(rec: Record, single_dose_set=SINGLE_DOSE_VACCINES) -> bool:
    v = rec.vaccine.strip().lower()
    required = 1 if v in single_dose_set else 2
    return rec.doses >= required

def count_fully_vaccinated(records: List[Record]) -> int:
    return sum(1 for r in records if is_fully_vaccinated(r))

def list_senior_citizens(records: List[Record], threshold: int = 60) -> List[Record]:
    return [r for r in records if r.age >= threshold]

def percentage_fully_vaccinated(records: List[Record]) -> float:
    n = len(records)
    if n == 0:
        return 0.0
    return 100.0 * count_fully_vaccinated(records) / n

def most_used_vaccine(records: List[Record]) -> List[str]:
    if not records:
        return []
    counter = Counter(r.vaccine.strip() for r in records)
    if not counter:
        return []
    max_count = max(counter.values())
    return sorted([v for v, c in counter.items() if c == max_count])

def records_sorted_by_age(records: List[Record], descending: bool = False) -> List[Record]:
    return sorted(records, key=lambda r: r.age, reverse=descending)

def print_record(r: Record) -> None:
    print(f"Name: {r.name}, Age: {r.age}, Vaccine: {r.vaccine}, Doses: {r.doses}")

def sample_data() -> List[Record]:
    return [
        Record("Alice", 34, "Pfizer", 2),
        Record("Bob", 68, "Moderna", 2),
        Record("Carol", 72, "J&J", 1),
        Record("Dave", 45, "AstraZeneca", 1),
        Record("Eve", 60, "Pfizer", 2),
        Record("Frank", 29, "Moderna", 1),
    ]

def main():
    print("Vaccination Center Records")
    records: List[Record] = []
    # start with sample data to make it easy to test; comment out next line if you want empty start
    records.extend(sample_data())

    while True:
        print("\nMenu:")
        print("1) Add record")
        print("2) Show all records")
        print("3) Count fully vaccinated")
        print("4) Show senior citizens (age >= 60)")
        print("5) Percentage fully vaccinated")
        print("6) Most used vaccine")
        print("7) Display records sorted by age (asc)")
        print("8) Display records sorted by age (desc)")
        print("9) Clear all records")
        print("0) Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                name = input("Name: ").strip()
                age = int(input("Age: ").strip())
                vaccine = input("Vaccine type: ").strip()
                doses = int(input("Number of doses: ").strip())
            except ValueError:
                print("Invalid input; please enter numeric values for age and doses.")
                continue
            records.append(Record(name, age, vaccine, doses))
            print("Record added.")

        elif choice == "2":
            if not records:
                print("No records.")
            else:
                for r in records:
                    print_record(r)

        elif choice == "3":
            cnt = count_fully_vaccinated(records)
            print(f"Fully vaccinated individuals: {cnt}")

        elif choice == "4":
            seniors = list_senior_citizens(records)
            if not seniors:
                print("No senior citizens found.")
            else:
                print(f"Senior citizens (age >= 60): ({len(seniors)})")
                for r in seniors:
                    print_record(r)

        elif choice == "5":
            pct = percentage_fully_vaccinated(records)
            print(f"Percentage fully vaccinated: {pct:.2f}%")

        elif choice == "6":
            top = most_used_vaccine(records)
            if not top:
                print("No vaccine data.")*
