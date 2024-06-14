locations = ["Garage","Hall","Bedroom","Swimming pool"]
searching = input("Enter the Locations: ")
for i in locations:
    if i==searching:
        print("Key founded in:-" , i)
        break
    else:
        print("Key doesnt founded!!")
