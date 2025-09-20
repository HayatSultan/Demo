class Product:
    """Represents a product with a name, price, and stock."""
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        """Returns a string representation of the product."""
        return f"{self.name} | Price: ${self.price:.2f} | Stock: {self.stock} units"

    def update_stock(self, quantity):
        """Updates the product's stock by a given quantity."""
        self.stock += quantity

class Customer:
    """Represents a customer with a name and an ID."""
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

    def __str__(self):
        """Returns a string representation of the customer."""
        return f"Customer: {self.name} (ID: {self.customer_id})"

class ShoppingCart:
    """Represents a shopping cart for a customer, managing products and quantities."""
    def __init__(self, customer):
        self.customer = customer
        self.items = {}  # Dictionary to store products and their quantities

    def add_item(self, product, quantity):
        """Adds a product to the cart with a specified quantity."""
        if product.stock >= quantity:
            if product.name in self.items:
                self.items[product.name]['quantity'] += quantity
            else:
                self.items[product.name] = {'product': product, 'quantity': quantity}
            product.update_stock(-quantity)  # Decrease the stock
            print(f"✅ Added {quantity} of {product.name} to the cart.")
        else:
            print(f"❌ Error: Not enough stock for {product.name}. Available: {product.stock}")

    def remove_item(self, product, quantity):
        """Removes a product from the cart."""
        if product.name in self.items:
            current_quantity = self.items[product.name]['quantity']
            if quantity >= current_quantity:
                del self.items[product.name]
                product.update_stock(current_quantity)
                print(f"❌ Removed all {product.name} from the cart.")
            else:
                self.items[product.name]['quantity'] -= quantity
                product.update_stock(quantity)
                print(f"❌ Removed {quantity} of {product.name} from the cart.")
        else:
            print(f"ℹ️ {product.name} is not in the cart.")


# --- Main Program Execution ---
if __name__ == "__main__":
    # 1. Create objects (instances) of the Product and Customer classes
    print("--- Creating Products and Customer ---")
    laptop = Product("Laptop", 1200.00, 10)
    keyboard = Product("Mechanical Keyboard", 85.50, 25)
    mouse = Product("Gaming Mouse", 50.00, 15)

    customer1 = Customer("Alice", "CUST-001")
    print(f"Created: {laptop}")
    print(f"Created: {keyboard}")
    print(f"Created: {mouse}")
    print(f"Created: {customer1}")
    print("------------------------------------\n")

    # 2. Create a ShoppingCart object for the customer
    alice_cart = ShoppingCart(customer1)
    
    # 3. Use the ShoppingCart object's methods to add and remove items
    print("--- Adding and Removing Items ---")
    alice_cart.add_item(laptop, 1)
    alice_cart.add_item(keyboard, 2)
    alice_cart.add_item(mouse, 10)

    # 4. View the cart contents
    alice_cart.view_cart()

    # 5. Try to add more items than available stock
    print("--- Attempting to over-purchase ---")
    alice_cart.add_item(laptop, 15)

    # 6. Remove some items
    alice_cart.remove_item(keyboard, 1)

    # 7. View the final cart and remaining stock
    alice_cart.view_cart()
    print("--- Final Product Stock ---")
    print(f"Updated Stock: {laptop}")
    print(f"Updated Stock: {keyboard}")
    print(f"Updated Stock: {mouse}")
    print("------------------------------------\n")
