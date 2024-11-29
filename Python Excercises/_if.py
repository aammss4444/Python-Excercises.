# # 1. Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
# Write a program that asks user to enter a city name and it should tell which country the city belongs to
# Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"

India = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
city = input("Enter the city name:")
if city in India:
  print("The city belongs to India.")

elif city in pakistan:
  print("The city belongs to pakistan.")

else:
  print("The city belongs to bangladesh.")

# 2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
# Ask user to enter his fasting sugar level 
# If it is below 80 to 100 range then print that sugar is low
# If it is above 100 then print that it is high otherwise print that it is normal

sugar_lvl = input("Enter your suger level:")
sugar_lvl = float(sugar_lvl)
if sugar_lvl<80:
  print("Your sugar level is low.")

elif sugar_lvl<101:
  print("Your sugar level is normal.")

else:
  print("Your sugar level is high.")
  
