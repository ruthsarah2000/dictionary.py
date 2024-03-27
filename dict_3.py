'''
3. Python Programming Challenges for Customer Service Data Handling
Task 1: Customer Service Ticket Tracker
Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

Problem Statement:
Develop a program that:

Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
Implement functions to:
Open a new service ticket.
Update the status of an existing ticket.
Display all tickets or filter by status.
Initialize with some sample tickets and include functionality for additional ticket entry.
Example ticket structure:
'''
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(customer, issue):
    ticket_id = f"Ticket{len(service_tickets) + 1:03d}"
    service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
    print(f"New ticket opened: {ticket_id}")

def update_ticket_status(ticket_id, status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = status
        print(f"Ticket {ticket_id} status updated to: {status}")
    else:
        print(f"Ticket {ticket_id} not found.")

def display_tickets(status=None):
    if status:
        filtered_tickets = {ticket_id: ticket_info for ticket_id, ticket_info in service_tickets.items() if ticket_info["Status"] == status}
        if filtered_tickets:
            print(f"Tickets with status '{status}':")
            for ticket_id, ticket_info in filtered_tickets.items():
                print(f"Ticket ID: {ticket_id}, Customer: {ticket_info['Customer']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}")
        else:
            print(f"No tickets found with status '{status}'.")
    else:
        print("All tickets:")
        for ticket_id, ticket_info in service_tickets.items():
            print(f"Ticket ID: {ticket_id}, Customer: {ticket_info['Customer']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}")


open_ticket("Charlie", "Technical support")
update_ticket_status("Ticket001", "closed")
display_tickets("open")
display_tickets("closed")
