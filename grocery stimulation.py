#!/usr/bin/python3
from random import seed, randrange
from header6 import *
N = 10 # Setting the vale of N as 10

def rnd(low, high): 
    '''
    It Generates random numbers
    :param : low,high
    :return: The random number in the range low,high
    '''
    return randrange(low, high + 1) # returns the random number in the range low and high


def arrival(clock, picking):
    '''
    It is used to calculate the arrival time of the customer
    :param:clock,picking
    :return: The next arrival time and the next pick of the customer
    '''
    next_arr_time = clock + rnd(MIN_INT_ARR, MAX_INT_ARR) # The next arrival time is calculated by adding the clock with the rnd of minimum interarrival time and max interarrival
    if N > 0: # Customer has arrived, calculate the time it takes to pick
        print("Arriving to Store:    " + str(clock)) # Printing the arriving to store time
    customer = {
            "atime": clock,  # Arrival time
            "ptime": clock + rnd(MIN_PICK, MAX_PICK),  # Finish pick time
            "wtime": 0, # waiting time in checkout line
            "dtime": 0 # departing time from store of a customer
    } # Dictionary of the customer to capture the data values of customer as a single unit

    picking.append(customer) # Append the customer to the picking
    
    # Find the minimum pick time from the list of pickers
    next_pick = None # The next pick is intially None

    for customer in picking: # for loop for the customers in picking
        if next_pick is None or customer["ptime"] < next_pick: # If the value of next pick is none or the customer[ptime] is greater than next pick
            next_pick = customer["ptime"] # If the if statemnt is satisfied then next pick is equals to customer[ptime]

    return next_arr_time, next_pick # Return the value of next arrival time and next pick time

def shopping(clock, picking, checkout):
    '''
    Move customers who have finished picking and add it to the check out
    Next customer is the customer that has the lowest value
    :param:clock,picking,checkout: It is the checkout time and picking time of customer
    :return:the next pick and the checkout time
    '''
    finished_picking_customer = None # The value of finished picking customer is None
    for customer in picking: #for loop for customers in picking
        if customer["ptime"] == clock: #If the cutomer ptime is equal to the clock
            if N > 0: # If the value of N is greater than 0
                print("Picking Grocery Done: " + str(clock)) # Print the picking is done and the time

            finished_picking_customer = customer # Updating the customers who have finished picking
            break
    picking.remove(finished_picking_customer) # Remove the customers from picking who are done with their picking

    # If the checkout is busy with someone else then the person will have to
    # go to the line. The person's departure time is dependent on the last person
    # in check out
    if len(checkout) == 0: # If the length of the checkout is zero than 
        finished_picking_customer["dtime"] = clock + rnd(MIN_SERV, MAX_SERV) #The departing time of the customers who have finished picking is calculated with the given formula above
    checkout.append(finished_picking_customer) # Update the checkout list with the customers who have finished picking items

    # Find the minimum pick time from the list of pickers
    next_pick = None # The value of next pick is None
    for customer in picking: # For loop for customer in picking
        if next_pick is None or customer["ptime"] < next_pick: # If the next pick is none or the customer picking time completion is greater than next pick
            next_pick = customer["ptime"] # The value of next pick is the customer  time of completion of picking up the grocery items
    return next_pick, checkout[0]["dtime"] # It returns the next pick value and the checkout time of departing time

def update_stat(cust, total):
    '''
    Update the stats
    :param:customer,total
    '''
    total["num"] += 1 # Total is calculated as the total[num]+1
    total["pick"] += cust["ptime"] - cust["atime"] # The total pick time is calculated as the customer picking completion time minus the customer arrival time

    serv_time = cust["dtime"] - cust["ptime"] # The service time is calculated as the customer departure time minus the customer picking completion time
    if cust["wtime"] > 0: # If the customer waiting time is greater than zero
        wait_time = cust["wtime"] - cust["ptime"] # waiting time is the customer wait time ninus the customer picking time completion
        total["wait"] += wait_time # total wait time is calculated as the taotal wait time plus the wait time
        serv_time = cust["dtime"] - cust["wtime"] # The serving time is the customer departing time minus the customer wait time

    total["serv"] += serv_time # Total serving time is the total serv time plus the serving time
    total["shop"] += cust["dtime"] - cust["atime"] #Total shoping time is the customer departing time minus the customer arrival time

def print_stat(total):
    '''
    printing the stats
    :param:total
    '''
    num_shopped = "{:,}".format(total["num"])# The total number of shopped customer is calculated
    avg_pick = "{:,.3f}".format(total["pick"] / total["num"]) # The average pick tme is calculated
    avg_shop = "{:,.3f}".format(total["shop"] / total["num"]) # The average shop time is calculated
    avg_wait = "{:,.3f}".format(total["wait"] / total["num"]) # The average wait time is clculated
    avg_serv = "{:,.3f}".format(total["serv"] / total["num"]) # The average serving time is calculated

    spacing = len(num_shopped) # The spacing is calculated as the length of the number of customers shopped

    if len(avg_pick) > spacing: # If the lengh of average pick is greater than than the spacing
        spacing = len(avg_pick) # The value of spacing is set as the length of the average pick

    if len(avg_shop) > spacing: # If the length of average shoppe is greater than spacing
        spacing = len(avg_shop) # spacing is the value of length of average shoppe

    if len(avg_wait) > spacing: # If the length of average is greater than spacing
        spacing = len(avg_wait) # The value of spacing is length of average wait time

    print("Num of customers shopped  = " + num_shopped.rjust(spacing)) # Printing the customer shoppe
    print("Avg grocery pick time     = " + avg_pick.rjust(spacing)) # Printing the Average grocery pick time
    print("Avg wait time in checkout = " + avg_wait.rjust(spacing)) # Printing the average wait time in checkout
    print("Avg serv time in checkout = " + avg_serv.rjust(spacing)) # Printing the average serve time in checkout
    print("Avg time in store         = " + avg_shop.rjust(spacing)) # Printing the Average time in store

def departure(clock, checkout, total):
    '''
    The departure of the customer is calculated 
    :param: clock,checkout,total
    '''
    global N
    # Depart the next customer
    cust = checkout.pop(0)

    if N > 0: # If the value of N is greater than 0
        print("Departing from Store: " + str(clock)) # Print the Departing from store time
        print('\n') # Including the spaces
        

    N -= 1 # The value of N is calculated as N minus 1

    update_stat(cust, total) # The stats is updated with the customer and total value

    if len(checkout) > 0: # If the length of checkout is greater than 
        checkout[0]["wtime"] = clock # The checkout of cust at zero wait time is the value of clock
        checkout[0]["dtime"] = clock + rnd(MIN_SERV, MAX_SERV) # The checkout of customer o depart time is calculated using the above formula
        return checkout[0]["dtime"] # The Checkout of customer o depart time is returned if the length of checkout is greater than zero
    
    return None # Return the None value

def update_clock(next_arr, next_pick, next_dept):
    '''
    The clock time is updated
    :param:next_arr,next_pick,next_dept: The value of clock is updated based on the parameters
    :return:the next clock value
    '''
    # Find the smallest clock time
    next_clock = next_arr
    
    if next_pick is not None and next_pick < next_clock: # If the next pick is not none and next pic is greater than next clock
        next_clock = next_pick # The next clock is set as the value of next pick
    
    if next_dept is not None and next_dept < next_clock: # If the next dept is not None and the next dept is greater than next clcck
        next_clock = next_dept # The next clock value is the value of next departure value

    return next_clock # Return the value of next clock

def main():
    '''
    Entry point in the program
    '''
    seed(SEED) # Before generating the random number we call the SEED function
    clock = 0 # Intialize the clock
    
    # Initialize events
    next_arr = 0        # arrival time of the next customer
    next_pick = None    # time of a customer who is next to finish picking up the grocery items
    next_serv = None    # the time of a customer who is next to be served in the checkout line
    next_dept = None    # the departing time of a next customer from the store.
    
    # Initialize the statistical values
    total = {
            "num": 0,   # total number of customers departed from the store
            "pick": 0,  # accumulated grocery picking times
            "wait": 0,  # accumulated waiting times
            "serv": 0,  # accumulated service times
            "shop": 0   # accumulated time spent in the store over all customers
    }

    picking = [] # List of Picking 
    checkout = [] # List of Checkout 

    while clock < SIMTIME: # if the value of clock is greater than SIMTIME
        if clock == next_arr: # If the value of clock is equals to the next arrival time
            next_arr, next_pick = arrival(clock, picking) # The next arrival and next pick time is set using the clock and picking values
        elif clock == next_pick: # If the value of clock is equals to the next pick value
            next_pick, next_dept = shopping(clock, picking, checkout) # It is calculated as the shopping using clock.picking and the picking
        elif clock == next_dept: #If the clock value is equals to the next departure then
            next_dept = departure(clock, checkout, total) # Departure is calculated as the clock,checkout and the total
        
        clock = update_clock(next_arr, next_pick, next_dept) # The valueof clock is updated using the next arrival time,next pick  and next departure time
    
    print() # Calling the print fucntion
    print_stat(total) # Printing the stats using the the total 

main() # Calling the main function

