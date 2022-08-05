import priceList

price_list = priceList.prieList



def change_availability(juice_name,availability):
    price_list[juice_name][1]=availability;

def add_item():
    print("added an intem")

def remove_item():
    print("removed an item")

def print_bill():
    print("bill")

def show_total_sales():
    print("total sales")



print("prieList",priceList.prieList)
change_availability("Mango Juice",1)
print("prieList",priceList.prieList)
print("prieList",priceList.prieList)