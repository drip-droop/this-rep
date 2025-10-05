# Made by Hitesh



# import the necessary package



import pandas as pd

import matplotlib.pyplot as pyplot

import numpy as np

import random







# home screen

print("--------------------------------------------------------------")

print("UNIFIED PUBLIC TRANSPORT INFORMATION & TICKET RETRIEVAL SYSTEM")

print("--------------------------------------------------------------")

print("\n")

print("Welcome to Unified Public Transport Information & Ticket Retrieval System")

print("\n")



# user options

print("Please select your mode of transport")

print("1. Bus")

print("2. Train")

print("3. Metro")

print("\n")

print("h Help")

print("q Quit")

print("\n")



#ask for user input

myuser_input = eval(input(">> "))



# if user selects 1

if myuser_input == "1" or "1.":



# Then open the Bus Information Menu

    print("Please select the type of information you want to retrieve")

    print("\n")

    print("1. Bus Routes")

    print("q Quit")

    print("\n")

# Ask for user input inside Bus Information Menu

    this_cmd = input(">>> ")



    # If user selects "1. Bus Routes" as option

    if this_cmd == "1":



        #then make a dataframe out of "routes.csv" file

        

        bus_routes = pd.read_csv("routes.csv")

        print(bus_routes)



        # take 3 variables

        # category: user specified column name

        # value: the criteria to match or compare to

        # div: operation to be performed filter by comparison using > or fetch specific type of values that match the criteria using =

        # split the input string into 3 variables by space character

        category, div, value = input("GET: ").split()



        # if the operation is to find specific values, using =

        if div == "=":

            user_bus_route_query = bus_routes[bus_routes[category] == value]

            print(user_bus_route_query)



        # else if the operator is > then convert the specified value to a integer and print the filtered output

        else:

            if div == ">":

                user_bus_route_query = bus_routes[bus_routes[category] > int(value)]

                print(user_bus_route_query)



    # if user selects q on Bus Information Menu then exit the program

    else:

        if this_cmd == "q" or "Q":

            print("Exiting...")

            

else:

    if my_user_input == "h" or "H":

        print("Welcome to  Unified Public Transport Information & Ticket Retrieval System's Help Section")

        print("The commands in the 'GET: ' input section in any table should be in the form of ColumnName Operator Filter-value for eg:")

        print(" 'RouteID = 10B' fetches the details for Route 10B, similiarly,")

        print(" 'RouteLength(KM) > 10 fetches the details of all those routes whose route length is greater than 10 km")

