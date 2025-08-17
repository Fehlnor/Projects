# You have 250 euro, you go shopping and you can buy 
# flour (8euro / kg)
# honey (22euro / kg)
# sugar (6euro / kg)
# milk (4euro / l)
# bread (15euro / kg) 
# water (12euro / l)
# The program should read how much you want to buy of each item and then print the total amount to pay. 
# If the total exceeds the amount of money you have, the program should print that.

""" 
1. Just make it - Dont over program from the start. Write the simplest version that produces correct output, even if it's not pretty.
2. Clean it up - Once it works, clean up the code (better variable names, functions, structure, error handling).
3. Optimize - Only after correctness and cleaning worry about performance.
"""

"""             Step by step thinking process / lets break it down

    1. Understanding the problem 
        -(What am I given?): I'm given a budget (random amount) and items (random amount), each of the items are selling for a certain price 
        -(What do I need to find?): Calculate if the number of items are affordable or not from the given budget
        -(Are there special cases?): If I do not have a budget of the cheapest item, I cannot buy anything, Budget cannot be less then 0, 
        we are going with whole numbers no decimals, but it could be 5 euro 40 cent in other cases
 
    2. Decide how to represent the data
        -I need to represent the budget and item costs in variable mostly integers
        -I need to represent the amount the user is buying (need to prompt the user)
        userBudget int, flourPrice int, honeyPrice int, sugarPrice int, milkPrice int, breadPrice int, waterPrice int, fullCost int

    3. Calculation
        - The calculation for the items | itemsPrice * userPiece
        - The calculation for adding the items | fullCost = fullCost + (itemsPrice * userPiece)
        - The calculation for the budget | userBudget - fullCost  )) or ((   if userBudget >= fullCost

"""