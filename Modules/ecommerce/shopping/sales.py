# from ecommerce.customer import contact 
# # best practice to use 'Absolute import'
# print("Sales initialize", __name__)

def calc_tax():
    print("Calculating Tax")

def calc_shipping():
    print("Calculating Shipping")


if __name__ == "__main__":
    print("Sales started")
    calc_tax()