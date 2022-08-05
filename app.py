import priceList
# import pandas as pd
# df = pd.read_json('data.json')
# print(df.to_string())



price_list = priceList.juice_regular_json

def print_cli():
    print("---------------------------------------------Juice Bar---------------------------------------------------------------------")
    print("options :")
    print("::           1. Order an item")
    print("::           2. aintain price list")
    print("::           0. close Juice Bar")

def print_itemCategory_cli():
    print("--------------------------------------------Select an Items--------------------------------------------------------------------")
    print("::             1. Regular Juice")
    print("::             2. Vegi Juice")
    print("::             3. Milkshakes")
    print("::             4. Smoothies")
    print("::             5. Other items")

def print_items_cli():
    print("ane")

def app():
    end=True;
    while(end):
        print_cli()
        x = int(input())
        match x:
            case 1:
                print_itemCategory_cli();
                y = int(input())
                order_item(y);
            case 2:
                maintain_pricelist();
            case 0:
                show_total_sales()
                end=False
            case default:
                print("something went wrong")


def change_availability(juice_name,availability):
    price_list[juice_name][1]=availability;

def maintain_pricelist():
    print("maintain")

def add_item():
    print("added an intem")

def remove_item():
    print("removed an item")

def order_item():
    print("transaction")

def print_bill():
    print("bill")

def show_total_sales():
    print("total sales")


app();