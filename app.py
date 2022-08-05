import priceList

price_list = priceList.prieList


def change_availability(juice_name,availability):
    price_list[juice_name][1]=availability;
    

print("prieList",priceList.prieList)
change_availability("Mango Juice",1)
print("prieList",priceList.prieList)