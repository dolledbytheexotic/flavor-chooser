import re

print("Here is a list of chicken flavors choose which is your favorite:")

Flavors={
  "Flavor 1":"Mango Habenara",
  "Flavor 2":"Buffalo",
  "Flavor 3":"BBQ",
}
print(Flavors)

chicken_wing_flavors1=["BBQ","Buffalo","Mango Habenara"]
while True:
    flavor_Choice=input("Whats your favorite flavor: ")

  

    joiner="^(" + "|".join(chicken_wing_flavors1)+")$"

    match=re.match(joiner,flavor_Choice)

    if match:
      
      print("Good choice")

    else: 
      
      print("Try again ")
      
      satisfaction=input("Do you want to try again: (yes/no):")
      
      if satisfaction=="no":
        
        break 









