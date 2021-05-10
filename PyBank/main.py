#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 22:54:25 2021

@author: matt.rentner
"""
print("Financial Analysis")
print("--------")
import os
import csv

budget_data_csv = os.path.join(".","Resources","budget_data.csv")


#open and read csv

with open(budget_data_csv) as df:
    csv_reader = csv.reader(df, delimiter=",")

  # Read the header row first (skip this part if there is no header)
    csv_header = next(df)
    #print(f"Header: {csv_header}")

    profit_list=[] #create empty list
    Total_Profit=0
    months=0
    for row in csv_reader:
        months += 1
        Total_Profit += int(row[1])
        profit_list.append(int(row[1])) #appending each item the second column to the list
    print("Total Months: ",months)
    print('Total Profit =',"${:,}". format(Total_Profit))
    
    Diff = [profit_list[i+1]-profit_list[i] for i in range(len(profit_list)-1)]
    increase = max(Diff)
    decrease = min(Diff)

    print('Avg. Change: ',"{:,.2f}".format(sum(Diff)/len(Diff)))

    print('Greatest Increase: ',"{:,}".format(increase))
    print('Greatest Decrease: ',"{:,}".format(decrease))
    
    
    

    



