class Product:
    def __init__(self, id, name, description, price, stock):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

class User:
    def __init__(self, username):
        self.username = username
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def view_cart(self):
        total_price = 0
        print("Items in Cart:")
        for product in self.cart:
            print(f"ID: {product.id}, Name: {product.name}, Price: ${product.price}")
            total_price += product.price
        return total_price

def load_products():
    products_data = [
        {
            "id": "1",
            "name": "Laptop",
            "description": "A powerful laptop with high performance",
            "price": 999.99,
            "stock": 10
        },
        {
            "id": "2",
            "name": "Smartphone",
            "description": "A feature-packed smartphone with a sleek design",
            "price": 699.99,
            "stock": 20
        },
        {
            "id": "3",
            "name": "Headphones",
            "description": "High-quality headphones for an immersive audio experience",
            "price": 149.99,
            "stock": 15
        },
        {
            "id": "4",
            "name": "Smartwatch",
            "description": "A stylish smartwatch with fitness tracking features",
            "price": 199.99,
            "stock": 25
        }
    ]
    products = []
    for product_data in products_data:
        product = Product(product_data["id"], product_data["name"], product_data["description"], product_data["price"], product_data["stock"])
        products.append(product)
    return products

def display_products(products):
    print("Available Products:")
    for product in products:
        print(f"ID: {product.id}, Name: {product.name}, Price: ${product.price}")

def main():
    products = load_products()
    display_products(products)
    print("Welcome to the E-commerce System!")
    username = input("Enter your username: ")
    user = User(username)
    while True:
        print("\nAvailable Actions:")
        print("1. Add Product to Cart")
        print("2. View Cart")
        print("3. Purchase")
        print("4. Exit")
        print("5 Another user") 
        choice = input("Enter your choice: ")
        if choice == "1":
            product_id = input("Enter the ID of the product you want to add to cart: ")
            for product in products:
                if product.id == product_id:
                    user.add_to_cart(product)
                    print("Product added to cart!")
                    break
            else:
                print("Product not found!")
        elif choice == "2":
            user.view_cart()
  
        elif choice == "3":
            hello=user.view_cart()
            if hello!=0:
                print("Thank you for your purchase!\n")
                print(f"your total bill is {hello}")
            else:
                print("you didn't purchase anything and your cart is empty")
    
        elif choice == "4":
            print("Exiting...")
            break
        elif choice =="5":
            if __name__ == "__main__":
                main()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
