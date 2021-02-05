# Grocery-stimulation-using-python
The purpose of this program is to collect statistical data during the simulation and printout the final statistics at the end of the simulation. In this model, customers enter the store by random inter-arrival times and then start picking up the grocery items, which takes a random amount of time. After picking up the grocery items, a customer gets in the checkout line to pay for his/her items. The duration of the time spent in the checkout line is also random.

All random numbers in simulation have integer values and the time unit for the simulation clock is in minutes. Before starting to generate random numbers, call the function
seed ( ) with the argument SEED = 1 to initialize the RNG.

To capture the data values of a customer as a single unit we define a dictionary with keys: ‘atime, ‘ptime’, ‘wtime’ and ‘dtime’, where ‘atime’ is the arrival time, ‘ptime’ is the time of completion of picking up the grocery items and then entering the checkout line, ‘wtime’ is the waiting time in the checkout line, and ‘dtime’ is the departing time from the store of a customer.

For customers who are in the process of picking up the grocery items we define a list of dictionaries, where each element of the list corresponds to a customer.

 To capture the statistical values as a single unit we define a dictionary with keys: ‘num’, ‘pick’, ‘wait’, ‘serv’ and ‘shop’, where ‘num’ is total number of customers departed from the store, ‘pick’ is the accumulated grocery picking times, ‘wait’ is the accumulated waiting times, ‘serv’ is the accumulated service times, and ‘shop’ is the accumulated time spent in the store over all customers.
