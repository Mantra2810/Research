counter = 10000
def staff_info():
    global counter
    date = input("Enter the date: ")
    staff_id = input("Enter the staff ID: ")
    staff_name = input("Enter the name: ")
    requisition_id = counter + 1
    counter += 1
    return date, staff_id, staff_name, requisition_id

def requisitions_total():
    date, staff_id, staff_name, requisition_id = staff_info()
    total = 0
    total += int(input("Phone: 200$ (Enter quantity): ")) * 200
    total += int(input("Mouse: 100$ (Enter quantity): ")) * 100
    total += int(input("Laptop: 50$ (Enter quantity): ")) * 50
    return date, staff_id, staff_name, requisition_id, total

def requisition_approval():
    date, staff_id, staff_name, requisition_id, total = requisitions_total()
    status = "Approved" if total < 500 else "Pending"
    approval_ref_number = f"{staff_id}{str(requisition_id)[-3:]}" if total < 500 else ""
    display_requisitions(date, staff_id, staff_name, requisition_id, total, status, approval_ref_number)

def display_requisitions(date, staff_id, staff_name, requisition_id, total, status, approval_ref_number=""):
    print("\nPrinting Requisitions:\n")
    print(f"Date: {date}")
    print(f"Requisition ID: {requisition_id}")
    print(f"Staff ID: {staff_id}")
    print(f"Staff Name: {staff_name}")
    print(f"Total: ${total}")
    print(f"Status: {status}")
    if approval_ref_number:print(f"Approval Reference Number: {approval_ref_number}")

requisition_approval()