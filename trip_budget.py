


# PRETTY ART TO INTRO 

print("###############################")
print("###############################")
print("###      Welcome to         ###")
print("###   Family Trip Budget    ###")
print("###############################") 
print("###############################")
print("\n\n")
# Input questions 

BUDGET = 6000

budget_total = print("Your current budget is: 6,000$")

airfare_cost = float(input("Please enter the airfare cost, per person: $ "))

day_total = float(input("Please enter the amount of days you'll be staying: "))

food_daily = float(input("Please enter the daily food budget estimate: $ "))

souvenir_budget = float(input("Please enter the desired souvenir budget estimate: $ "))

excursion_cost = float(input("Please enter the desired excursion cost estimate: $ "))

# If statement with MATH 


# total_cost = airfare_cost * 4 + food_daily * 4 * day_total + souvenir_budget + excursion_cost 


# if total_cost >= 6000: 
#     print("Be wary! That exceeds the budget!")
# elif total_cost == 6000: 
#     print("That is your exact budget, be careful.")
# else: 
#     print("You are all good!!")

# Reference 


added_summary = (airfare_cost * 4) + (food_daily * 4 * day_total) + souvenir_budget + excursion_cost


if added_summary >= BUDGET: 
    cut_cost = added_summary - BUDGET
    print("That exceeds your budget!" ,added_summary, "You should cut your cost by," ,cut_cost, )
elif added_summary == BUDGET: 
    print("That is the exact price... tread cautiously.")
elif added_summary < BUDGET:
    left_over = added_summary * -1 - BUDGET 
    print("You have $" ,left_over, "left for other things!")
else: 
    print("Wuh oh." )




