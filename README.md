README - Requisition System
============================

Description:
------------
This is a simple Python-based Requisition System that simulates a staff requisition process. 
It allows users to enter requisition details, calculates total costs, and determines the 
approval status based on predefined rules.

How It Works:
-------------
- The system prompts for staff details and item requisitions.
- For each requisition, the user inputs:
  - Date
  - Staff ID
  - Staff Name
  - Three items with their prices
- Based on the total cost of the items, the system automatically assigns an approval status.

Approval Rules:
---------------
- If the total cost is **less than $500**:
  - Status: Approved
  - Approval Reference Number: Generated using Staff ID and part of Requisition ID
- If the total cost is **between $500 and $999.99**:
  - Status: Pending
  - Approval Reference Number: Not available
- If the total cost is **$1000 or more**:
  - Status: Not approved
  - Approval Reference Number: Not available

Program Output:
---------------
- Displays details of each requisition including:
  - Date
  - Requisition ID
  - Staff ID and Name
  - Total cost
  - Approval status
  - Approval reference number (if applicable)
- Prints overall statistics:
  - Total number of requisitions
  - Number of approved, pending, and not approved requisitions

Running the Program:
--------------------
1. Make sure you have Python installed.
2. Save the code in a file named `redeem.py`.
3. Open a terminal and run:
   python redeem.py
4. Follow the prompts to input requisition data.

Author:
-------
Your Name Here

Note:
-----
- This is a command-line-based prototype.
- No data is saved permanently; all entries are stored in memory during execution only.

