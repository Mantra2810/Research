counter = 10000

class RequisitionSystem:
    def __init__(self):
        global counter
        self.requisition_id = counter
        counter += 1

        self.staff_data = self.staff_info()
        self.staff_id = self.staff_data["staff_id"]
        self.staff_name = self.staff_data["staff_name"]

        self.items = []
        self.total = 0
        self.status = ""
        self.approval_ref_number = ""

    def staff_info(self):
        date = input("Enter the date (DD/MM/YYYY): ")
        staff_id = input("Enter the Staff ID: ")
        staff_name = input("Enter the Staff Name: ")
        return {
            "date": date,
            "staff_id": staff_id,
            "staff_name": staff_name,
        }

    def requisitions_details(self):
        for i in range(1, 4):
            item = input(f"Enter the name of item {i}: ")
            try:
                cost = float(input(f"Enter a price for {item}: "))
            except ValueError:
                print("Invalid input, defaulting cost to 0.")
                cost = 0.0
            self.items.append((item, cost))
            self.total += cost

    def requisition_approval(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_ref_number = f"{self.staff_id}{str(self.requisition_id)[-3:]}"
        elif self.total < 1000:
            self.status = "Pending"
            self.approval_ref_number = "Not available"
        else:
            self.status = "Not approved"
            self.approval_ref_number = "Not available"

    def display_requisitions(self):
        print(f"\nDate: {self.staff_data['date']}")
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Total: ${int(self.total)}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.approval_ref_number}")

all_requisitions = []

for i in range(4):
    print(f"\n=== Requisition {i+1} ===")
    req = RequisitionSystem()
    req.requisitions_details()
    req.requisition_approval()
    all_requisitions.append(req)

print("\n\nPrinting Requisitions:")
for req in all_requisitions:
    req.display_requisitions()

total_approved = sum(1 for r in all_requisitions if r.status == "Approved")
total_pending = sum(1 for r in all_requisitions if r.status == "Pending")
total_not_approved = sum(1 for r in all_requisitions if r.status == "Not approved")

print("\n\nStatistics:\n")
print("Displaying the Requisition Statistics\n")
print(f"The total number of requisitions submitted: {len(all_requisitions)}")
print(f"The total number of approved requisitions: {total_approved}")
print(f"The total number of pending requisitions: {total_pending}")
print(f"The total number of not approved requisitions: {total_not_approved}")
