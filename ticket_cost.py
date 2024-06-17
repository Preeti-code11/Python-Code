#lex_auth_01269361601342668881
def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    adult_ticket_cost=37550
    child_ticket_cost=37550/3
    ticket_amount=(no_of_adults*adult_ticket_cost)+(no_of_children*child_ticket_cost)
    service_tax=ticket_amount*(7/100)
    discount=(ticket_amount+service_tax)*(.10)
    total_ticket_cost=ticket_amount+service_tax-discount

    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(3,1)
print("Total Ticket Cost:",total_ticket_cost)