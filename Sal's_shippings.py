weight = 1.5
cost_gs = 0

#Ground Shipping 
#price per pound
if  weight <= 2:
  cost_gs = 1.50
elif weight <= 6:
  cost_gs = 3.00
elif weight <= 10:
  cost_gs = 4.00
elif weight > 10:
  cost_gs = 4.75
else:
  print("We need know the product's weight.") 

#The total price for Ground Shipping
cost_total_gs = weight*cost_gs+20
print("GROUND SHIPPING --- Total Cost: ${}".format(round(float(cost_total_gs), 2)))

#Ground Shipping Premium
cost_total_gsp = weight*cost_gs+125
print("\nGROUND SHIPPING PREMIUM --- Total Cost: ${}".format(round(float(cost_total_gsp), 2)))

#Drone Shipping
#price per pound
cost_ds = 0
if  weight <= 2:
  cost_ds = 4.50
elif weight <= 6:
  cost_ds = 9.00
elif weight <= 10:
  cost_ds = 12.00
elif weight > 10:
  cost_ds = 14.75
else:
  print("We need know the product's weight.") 

#The total cost for Drone Shipping
cost_total_ds = weight*cost_ds
print("\nDRONE SHIPPING --- Total Cost: ${}".format(round(float(cost_total_ds), 2)))