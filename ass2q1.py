
from typing import List, Dict

RATES = {
    "car": 5.0,   
    "bike": 2.0,  
}

Record = Dict[str, object]  


def calculate_fee(record: Record) -> float:
    vtype = str(record.get("type", "")).lower()
    hours = float(record.get("hours", 0))
    rate = RATES.get(vtype)
    if rate is None:
        raise ValueError(f"Unknown vehicle type: {record.get('type')}")
    return hours * rate


def total_revenue(records: List[Record]) -> float:
    return sum(calculate_fee(r) for r in records)


def vehicle_with_highest_fee(records: List[Record]) -> Record:
    if not records:
        return None
    return max(records, key=calculate_fee)


def vehicles_parked_more_than(records: List[Record], threshold_hours: float) -> List[Record]:
    return [r for r in records if float(r.get("hours", 0)) > threshold_hours]


def sort_by_fee_desc(records: List[Record]) -> List[Record]:
    return sorted(records, key=calculate_fee, reverse=True)


def pretty_print_record(record: Record) -> str:
    fee = calculate_fee(record)
    return f"{record['number']:15} | {record['type']:4} | {record['hours']:>5} hrs | ${fee:,.2f}"


def main():
   
    records: List[Record] = [
        {"number": "AP01AB1234", "type": "car", "hours": 3},
        {"number": "AP02XY9999", "type": "bike", "hours": 6},
        {"number": "AP03CD4321", "type": "car", "hours": 8.5},
        {"number": "AP04EF1111", "type": "bike", "hours": 2},
        {"number": "AP05GH2222", "type": "car", "hours": 5.5},
    ]

    print("All records (with fees):")
    for r in records:
        print(" ", pretty_print_record(r))

    total = total_revenue(records)
    print("\nTotal revenue: ${:,.2f}".format(total))

    top = vehicle_with_highest_fee(records)
    if top:
        print("\nVehicle with highest parking fee:")
        print(" ", pretty_print_record(top))

    more_than_5 = vehicles_parked_more_than(records, 5)
    print("\nVehicles parked for more than 5 hours:")
    if more_than_5:
        for r in more_than_5:
            print(" ", pretty_print_record(r))
    else:
        print("  None")

    sorted_records = sort_by_fee_desc(records)
    print("\nRecords sorted by parking fee (descending):")
    for r in sorted_records:
        print(" ", pretty_print_record(r))


if __name__ == "__main__":
    main()
