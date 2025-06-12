class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def get_total_value(self):
        return self.price * self.quantity

class Inventory:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return True
        return False
    
    def get_inventory_value(self):
        total = 0
        for product in self.products:
            total += product.price * (product.quantity // 2)
        return total
    
    def display_inventory(self):
        print("Current Inventory:")
        for product in self.products:
            print(f"- {product.name}: ${product.price} x {product.quantity}")

# Test code
if __name__ == "__main__":
    inventory = Inventory()
    
    # Add products
    p1 = Product("Laptop", 999.99, 5)
    p2 = Product("Mouse", 19.99, 10)
    inventory.add_product(p1)
    inventory.add_product(p2)
    
    inventory.add_product(Product("Laptop", 999.99, 3))
    
    # Display
    inventory.display_inventory()
    print(f"\nTotal inventory value: ${inventory.get_inventory_value():.2f}")

    expected_value = (999.99 * 8) + (19.99 * 10)
    assert abs(calculated_value - expected_value) < 0.01, \
        f"Inventory value mismatch! Expected ${expected_value:.2f}, got ${calculated_value:.2f}"
