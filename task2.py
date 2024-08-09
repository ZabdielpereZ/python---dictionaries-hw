from  helper import clear
# 2. Python Programming Challenges for Customer Service Data Handling

# Objective: This assignment is designed to test and enhance your Python programming skills, focusing on real-world applications in customer service data management. You will practice correcting code, organizing customer data, and implementing a feedback system using Python dictionaries.

# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket  to "closed".
# Display all tickets.
# (Bonus) filter by status
# Initialize with some sample tickets and include functionality for additional ticket entry.
# Example ticket structure:

service_tickets = {
    1: {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    2: {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def next_id(): # return an ID I can use to make a new service ticket
    last_id = 0
    for id in service_tickets.keys():
        if id > last_id:
            last_id = id
    return last_id + 1

def new_ticket(): # function for creating a new ticket
    new_id = next_id()
    while True:
        customer = input("Please enter the customer name: \n")
        issue = input("Please state the issue: \n")
        print(f"Customer: {customer}, Issue: {issue}")
        correct = input("Is this information correct? (y/n)").lower()
        if correct == 'y': # create a new ticket
            service_tickets[new_id] = {'Customer': customer, 'Issue': issue, 'Status': 'open'}
            break
        else:
            clear()
            continue


def main():
    while True:
        ans = input('''

                                   d8,                            d8,        d8b                                                                                                
                                  `8P                      d8P   `8P         ?88                 d8P                                                                            
                                                        d888888P              88b             d888888P                                                                          
 .d888b, d8888b  88bd88b?88   d8P  88b d8888b d8888b      ?88'    88b d8888b  888  d88' d8888b  ?88'        88bd8b,d88b  d888b8b    88bd88b  d888b8b   d888b8b   d8888b  88bd88b
 ?8b,   d8b_,dP  88P'  `d88  d8P'  88Pd8P' `Pd8b_,dP      88P     88Pd8P' `P  888bd8P' d8b_,dP  88P         88P'`?8P'?8bd8P' ?88    88P' ?8bd8P' ?88  d8P' ?88  d8b_,dP  88P'  `
   `?8b 88b     d88     ?8b ,88'  d88 88b    88b          88b    d88 88b     d88888b   88b      88b        d88  d88  88P88b  ,88b  d88   88P88b  ,88b 88b  ,88b 88b     d88     
`?888P' `?888P'd88'     `?888P'  d88' `?888P'`?888P'      `?8b  d88' `?888P'd88' `?88b,`?888P'  `?8b      d88' d88'  88b`?88P'`88bd88'   88b`?88P'`88b`?88P'`88b`?888P'd88'     
                                                                                                                                                             )88                
                                                                                                                                                            ,88P                
                                                                                                                                                        `?8888P                 
Enter the corresponding number for the action you'd like to take:
    1 - Open a new service ticket.
    2 - Update a service ticket.
    3 - Display all service tickets.
    4 - Quit
''')
        if ans == '1':
            clear()
            new_ticket()
        elif ans == '2':
            update_service(service_tickets) #argument   # function to update a ticket
        elif ans == '3':
            print(service_tickets) # function to display all tickets
        elif ans == '4':
            print("Thanks for making service tickets and stuff like that. Have a great day!")
            break
        else:
            print("Enter the right number fool!")


def update_service(tickets): # Parameter
    ticket_id = int(input(" Enter the ticket ID to update: ").strip())
    if ticket_id in tickets:
        new_status = input("Enter new status open or closed ? ").strip()
        tickets[ticket_id] = new_status
        print(f"Ticket {ticket_id} updated successfully.")
    else:
        print(f"Ticket '{ticket_id}' not found.")

main()