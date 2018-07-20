#Hours in a year. How many hours are in a year?
hrs = 24
days = 365
hrs = days*hrs
print("the number of hours in a year are",hrs)

# Minutes in a decade. How many minutes are in a decade?
minutes = 60
hrs = 24
days = 365
decade = 10 *days*hrs*minutes
print("the number of minutes in a decade are", decade)

#Your age in seconds. How many seconds old are you?
print("Enter your age")
years = int(input("years: "))

print("Enter the number of months since youre birthday")
months = int(input("months: "))

print("and finally enter the number of days into the current month")
days = int(input("days: "))

days = ((years * 12 + months) * 30) + days
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print("you have been alive for" , days, "days" , hours , "hours" , minutes , "minutes" , seconds , "seconds" , )

#Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name.

First = input("Enter your first name:")
Middle = input("Enter your middle name:")
Last = input("Enter your last name:")
greeting = "Hello there, %s %s %s"
print (greeting % (First, Middle,Last))

#Write a program that asks for a person’s favorite number. Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number.
#fav = input("what is your favorite number")
#newfav = int(fav) +1
#print("a bigger and better favorite number",newfav)

#Angry boss
#input("what do you want?")
#if ans ==("I WANT A RAISE?!")
#print("YOU'RE FIRED!!")

# Write a program that prints out the lyrics to that beloved classic, “99 Bottles of Beer on the Wall.”
for counter in reversed(range(1, 100)):
    print (counter, 'bottles of coke on the wall,',counter,' bottles of coke.')
    print ('Take one down and pass it around,', counter-1,' bottles of coke on the wall.')
