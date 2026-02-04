# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 18:29:49 2026

@author: Johnd
"""

import numpy as np

np.set_printoptions(suppress=True)

userChoice = -1

rows = int(input("How many rows in your matrix?\n"))
cols = int(input("How many cols in your martix?\n"))

mat = np.zeros((rows,cols), dtype=float)

for i in range(rows):
    inputs = input(
        f"Enter the values in row {i+1} of your matrix (separated by spaces):\n"
    )
    try:
        values = list(map(float, inputs.split()))
        if len(values) != cols:
            raise ValueError
        mat[i] = values
    except ValueError:
        print("Please enter exactly ", cols, " numeric values.")
        i -= 2  


def get_row(prompt, rows):
    while True:
        try:
            r = int(input(prompt)) - 1
            if r < 0 or r >= rows:
                raise ValueError
            return r
        except ValueError:
            print(f"Please enter a row number between 1 and {rows}.")

def get_nonzero_float(prompt):
    while True:
        try:
            x = float(input(prompt))
            if x == 0:
                raise ValueError
            return x
        except ValueError:
            print("Please enter a non-zero numeric value.")

while(userChoice != 4):
    
    print
    
    userChoice = input("Choose a row Operation \n 1. Switch two rows \n 2. Scale a row \n 3. Add or Subtract a scaled row \n 4. Exit\n")
    
    match userChoice:
        case "1":
            r1 = get_row("What is the first row you'd like to switch?\n", rows)
            r2 = get_row("What is the second row you'd like to switch?\n", rows)
            
            mat[[r1,r2]] = mat[[r2,r1]]
            
        case "2":
            r1 = get_row("What is the row you'd like to scale?\n", rows)
            sf = get_nonzero_float("What factor would you like to scale by?\n")
            
            mat[r1] = sf*mat[r1]
            
        
        case "3":
            r1 = get_row("What is the row you'd like to change?\n", rows)
            r2 = get_row("What is the row you'd like to add or subtract from the first row?\n", rows)
            sf = get_nonzero_float("What factor would you like to scale the addition by?\n")
            
            mat[r1] = mat[r1] + sf*mat[r2]
        
        case "4":
            
            print(f" \n {mat}\n")
            break
        
    print(f" \n {mat}\n")