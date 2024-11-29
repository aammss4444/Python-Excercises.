# We have following information on countries and their population (population is in crores),
# Country	Population
# China	143
# India	136
# USA	32
# Pakistan	21
# Using above create a dictionary of countries and its population
# Write a program that asks user for three type of inputs,
# print: if user enter print then it should print all countries with their population in this format,
# china==>143
# india==>136
# usa==>32
# pakistan==>21
# add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
# remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
# query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.

population = {
  "China": 143,
  "India": 136,
  "Usa": 32,
  "Pakistan": 21
}

def add():
    country=input("Enter country name to add:")
    country=country.lower()
    if country in population:
        print("Country already exist in our dataset. Terminating")
        return
    p=input(f"Enter population for {country}")
    p=float(p)
    population[country] = p # Adds new key value pair to dictionary
    print_all()

def remove():
  country = input("Enter country name to remove:")
  country = country.lower()
  if country not in population:
      print("Country doesn't exist in our dataset. Terminating")
      return
  del population[country]
  print_all()

def query():
  country = input("Enter country name to query:")
  country = country.lower()
  if country not in population:
      print("Country doesn't exist in our dataset. Terminating")
      return
  print(f"Population of {country} is: {population[country]} crore")

def print_all():
  for country, p in population.items():
      print(f"{country}==>{p}")

def main():
  op=input("Enter operation (add, remove, query or print):")
  if op.lower() == 'add':
      add()
  elif op.lower() == 'remove':
      remove()
  elif op.lower() == 'query':
      query()
  elif op.lower() == 'print':
      print_all()

if __name__ == '__main__':
  main()

#2. Write a program that asks user for operation. Value of operations could be,
# a. print: When user enters print it should print following,
# info ==> [600, 630, 620] ==> avg:  616.67
# ril ==> [1430, 1490, 1567] ==> avg:  1495.67
# mtl ==> [234, 180, 160] ==> avg:  191.33
# b. add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will append the price to the list. Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.

import statistics

stocks = {"info":[600,630,620], "ril":[1430,1490,1567], "mtl":[234,180,160]}

def print_all():
  for stock, price_list in stocks.items():
    avg = statistics.mean(price_list)
    print(f"{stock} ==> {price_list} ==> avg: {avg:.2f}")
    
def add():
  a = input("Enter the stock ticker:")
  b = input("Enter the stock price:")
  b = float(b)
  if a in stocks:
     stocks[a].append(b)
  else:
    stocks[a] = [b]
  print_all()

def main():
  output = input("Enter the operation(print, add or amemd):")
  if output.lower() == 'print':
    print_all()
  elif output.lower() == 'add':
    add()
  else:
    print("Unsupported operation:",output)

if __name__ == '__main__':
  main()

# 3. Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and returns area, circumference and diameter. You should get these values in your main program by calling circle_calc function and then print them

import math 

def circle_calc(radius):
  area = math.pi*(radius**2)
  circumference = 2*math.pi*radius
  diameter = 2*radius
  return area, circumference, diameter

if __name__ == "__main__":
   x = input("Enter the radius:")
   x = float(x)
   a, d, c = circle_calc(x)
   print(f"The area is {a}, circumferenc is {c}, and diameteris {d} of circle.")
  
  
  
  


  
    



                    
    

  
  