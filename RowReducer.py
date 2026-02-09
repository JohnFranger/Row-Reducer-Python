# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 18:29:49 2026

@author: Johnd
"""

import numpy as np

np.set_printoptions(suppress=True)

userChoice = -1

inverse = input("Are you trying to compute an inverse matrix? (yes/no): \n").strip().lower()
purpose = inverse in ("y", "yes", "true", "t", "1")

if purpose:
    while True:
        try:
            rows = int(input("How many rows/cols in the square matrix you'd like to find the inverse of?\n"))
            cols = rows
        except ValueError:
            print("Please enter whole numbers.")
            continue

        if rows <= 0:
            print("Please enter a positive integer.")
            continue
        break

    mat = np.zeros((rows, rows), dtype=float)
    identity = np.eye(rows, dtype=float)
    #print("Identity matrix:\n", identity)

else:
    while True:
        try:
            rows = int(input("How many rows in your matrix?\n"))
            cols = int(input("How many cols in your matrix?\n"))
        except ValueError:
            print("Please enter whole numbers.")
            continue
        if rows <= 0 or cols <= 0:
            print("Please enter positive integers.")
            continue
        break

    mat = np.zeros((rows, cols), dtype=float)
    #print("Zero matrix:\n", mat)



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

def get_nonzero_float(prompt, mord):
    while True:
        try:
            x = float(input(prompt))
            if x == 0:
                raise ValueError
            if mord == "d":
                x = 1/x
            return x
        except ValueError:
            print("Please enter a non-zero numeric value.")

while(userChoice != 4):
    
    print(mat)
    
    userChoice = input("Choose a row Operation \n 1. Switch two rows \n 2. Scale a row \n 3. Add or Subtract a scaled row \n 4. Exit (View Inverse)\n")
    
    match userChoice:
        case "1":
            r1 = get_row("What is the first row you'd like to switch?\n", rows)
            r2 = get_row("What is the second row you'd like to switch?\n", rows)
            
            mat[[r1,r2]] = mat[[r2,r1]]
            if purpose:
                identity[[r1,r2]] = identity[[r2,r1]]
            
        case "2":
            r1 = get_row("What is the row you'd like to scale?\n", rows)
            mord = "q"
            while mord not in ("m", "d"):
                mord = input("Would you like to multiply or divide? (enter m or d)\n")
            if mord == "d":
                sf = get_nonzero_float("What factor would you like to divide by?\n", mord)
            elif mord == "m":
                sf = get_nonzero_float("What factor would you like to multiply by?\n", mord)
            
            mat[r1] = sf*mat[r1]
            if purpose:
                identity[r1] = sf*identity[r1]
            
        
        case "3":
            r1 = get_row("What is the row you'd like to change?\n", rows)
            r2 = get_row("What is the row you'd like to add or subtract from the first row?\n", rows)
            mord = "q"
            while mord not in ("m", "d"):
                mord = input(f"Would you like to multiply or divide row {r2+1}? (enter m or d)\n")
            sf = get_nonzero_float("What factor would you like to scale the addition by?\n", mord)
            
            mat[r1] = mat[r1] + sf*mat[r2]
            if purpose:
                identity[r1] = identity[r1] + sf*identity[r2]
        
        case "4":
            
            if purpose:
                print("This is the inverse matrix!\n")
                print(identity)
            break
        
    #print(f" \n {mat}\n")