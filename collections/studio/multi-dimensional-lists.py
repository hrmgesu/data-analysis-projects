food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.

food_list = sorted(food.split(","))
equipment_list = sorted(equipment.split(","))
pets_list = sorted(pets.split(","))
sleep_aids_list = sorted(sleep_aids.split(","))

# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.

cargo_hold = [food_list, equipment_list, pets_list, sleep_aids_list]
print(cargo_hold)
    
# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
cabinet_index = int(input("Select a cabinet (0-3): "))



# d) Use bracket notation and format to display the contents of the se  lected cabinet. If the user entered an invalid number, print an error message.

if 0 <= cabinet_index < len(cargo_hold):
    selected_cabinet = cargo_hold[cabinet_index]
    print(f"Cabinet {cabinet_index} contains: {', '.join(selected_cabinet)}")  
else:
    print("Error: Invalid cabinet number.")
             
 
# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
item = input("Enter an item to search for: ")
if 0 <= cabinet_index < len(cargo_hold):
    selected_cabinet = cargo_hold[cabinet_index]
    if item in selected_cabinet:
        print(f"Cabinet {cabinet_index} DOES contain {item}.")
    else:
        print(f"Cabinet {cabinet_index} DOES NOT contain {item}.") 
