import math
#This allows for the python to use math
priceList = {
    '1' : 7.35, #Vandas
    '2' : 9.80, #Miltonia
    '3' : 8.50 #Cattleya
}
#This is the dictionary of the prices of the flowers
print("welcome to Olivia's flower emporium, this is a price checker that checks the price of flowers, for a specified amount")

while True:
    member = input('are you a member ? [y] or [n] >')
    if member.lower() == 'y':
        member = True
        break
    elif member.lower() == 'n':
        member = False
        break
    else:
        print('Please enter [y] or [n]')
#This loop asks the user whether or not they are a user, if an invalid entry is entered
#it will automatically start again

flowerChoice = input("what flower would you like [1] Vandas, [2] Miltonia, [3] Cattleya")
#User enters a number, functionality can be added
quantity = int(input("how many flowers would you like"))
flowerPrice = priceList[flowerChoice] * quantity
#The square brackets are what the user inputs, it goes to the dictionary and finds the right flower
print ("Price of the flowers without discount comes to", round(flowerPrice, 2))

if member == True:
    flowerPrice = flowerPrice * 0.9

if quantity >= 5: 
    flowerPrice = flowerPrice * 0.95

#These two if statements check if discounts are to be applied


print("your price comes to", round(flowerPrice, 2))
#This prints the discounted price
       