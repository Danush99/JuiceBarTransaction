import priceList

price_list = priceList.prieList

def print_cli():
    print("----------Juice Bar------------")
    print("options :")
    print("1 -> transaction")
    print("2 -> maintain price list")
    print("-1 -> close the shop")

def app():
    end=True;
    while(end):
        print_cli()
        x = int(input())
        match x:
            case 1:
                transaction();
            case 2:
                maintain_pricelist();
            case -1:
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

def transaction():
    print("transaction")

def print_bill():
    print("bill")

def show_total_sales():
    print("total sales")


app();

# print("prieList",priceList.prieList)
# change_availability("Mango Juice",1)
# print("prieList",priceList.prieList)
# print("prieList",priceList.prieList)