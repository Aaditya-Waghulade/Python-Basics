indian = ["dal","Shev Bhaji"]
italian = ["Pasta","Pizza"]
dish = input("Enter dish name: ")
if (dish in indian):
    print("The dish is indian")
elif (dish in italian):
    print("The dish is Italian")
else:
    print("The dish is Not in the list")