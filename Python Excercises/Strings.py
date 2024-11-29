#  1. Create 3 variables to store street, city and country, now create address variable tostore entire address. Use two ways of creating this variable, one using + operator and the other using f-string.Now Print the address in such a way that the street, city and country prints in a separate line
street = "13 patli gali"
city = "New Delhi"
country = "India"

address = street + '\n' + city + '\n' + country
print("Address using + operator:",address)

address = f'{street} \n {city} \n {country}'
print("Address using f-string:",address)

# 2. Create a variable to store the string "Earth revolves around the sun"
#     i Print "revolves" using slice operator
#     ii Print "sun" using negative index

a = "Earth revolves around the sun"
print(a[6:14])
print(a[26:29])

# 3. Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.

x = 5
y = 10

print(f" I eat {x} veggies and {y} fruits daily")

# 4. I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original string with new ones and print the new string. Also try to do this in one line.

s = 'maine 200 banana khaye'
print(s.replace('200 banana', '10 samosa'))