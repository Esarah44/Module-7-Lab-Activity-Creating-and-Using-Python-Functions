# Create Python function SumOfFood
# Sara Hernandez
# 11/13/2022
# Sum the price of each food


foodDict = {'Pizza': 3.50, 'Sandwich': 5.30, 'Hamburger': 9.45, 'Spaghetti': 5.75}

def SumOfFood(foodDict):
    TotalCost = 0
    for price in foodDict.values():
        TotalCost=TotalCost+price
    return(TotalCost)

x= SumOfFood(foodDict)
print('Total cost of food is', x)