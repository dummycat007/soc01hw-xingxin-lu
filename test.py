# calculate 1+2

print(1+2)
print(9/2)
print(2*3)
print(5-8)

print(5*(12-8)+ -15)
print(98 + (59872 / (13*8))* -51)

print(2**8)
print(1<<9)
print(10 %2)

hours = 365.25*24
print(hours)
minutes = 10*365.25*24*60
print(minutes)

print("Lets see how many days hours minutes and seconds youve been alive!")

print("please enter your name")
name = input("name: ")

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


print( name, "you have been alive for" , days, "days" , hours , "hours" , minutes , "minutes" , seconds , "seconds" , )
