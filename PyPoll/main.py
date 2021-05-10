#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 12:25:47 2021

@author: matt.rentner
"""
print("Election Results")
print("--------")
import os
import csv

election_data_csv = os.path.join(".","Resources","election_data.csv")


#open and read csv

with open(election_data_csv) as df:
    csv_reader = csv.reader(df, delimiter=",")

  # Read the header row first (skip this part if there is no header)
    csv_header = next(df)
    #print(f"Header: {csv_header}")
   
        
    tally = {}
    total = []
    for ID, county, candidates in csv_reader:
        total.append(str(ID))
        if candidates not in tally:
            tally[candidates]=0
        tally[candidates] +=1

    
    print('Total Votes: ',len(total))
    print("--------")
    for candidates, votes in sorted(tally.items(), key=lambda kv: kv[1],reverse=True):
       percent = votes/len(total)
       percent = "{:0.1%}".format(percent)
       print(candidates, ': ',percent,"(",votes,")")
    max_key = max(tally,key=tally.get)
    print("--------")
    print('Winner: ',max_key)

 

        #print(candidates,max(votes))

    

    
    