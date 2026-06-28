#code edited by Saphira & Berdaline

class Customer:
    """Customer entity in the bookstore."""

    def __init__(self, customer_id, name, email, phone=None, address=None):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.cart = None  # customer's cart, linked later

    def __repr__(self):
        return f"Customer({self.customer_id}, {self.name}, {self.email})"


class Book:
    """Book entity in the bookstore."""

    def __init__(self, book_id, title, author, price, stock=0):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"{self.title} by {self.author} - {self.price:.2f} HTG"


class CartItem:
    """A line item in the cart (a book + quantity)."""

    def __init__(self, book: Book, quantity: int = 1):
        self.book = book
        self.quantity = quantity

    @property
    def subtotal(self):
        return self.book.price * self.quantity

    def __repr__(self):
        return f"{self.book.title} x{self.quantity} = {self.subtotal:.2f} HTG"


class Cart:
    """Cart entity - manages the list of books a customer wants to buy."""

    def __init__(self, customer: "Customer" = None):
        self.customer = customer
        self.items = []  # list of CartItem objects
        if customer is not None:
            customer.cart = self  # link the cart to the customer

    def add_book(self, book: Book, quantity: int = 1):
        """Add a book to the cart. If it's already there, increase the quantity."""
        for item in self.items:
            if item.book.book_id == book.book_id:
                item.quantity += quantity
                return
        self.items.append(CartItem(book, quantity))

    def remove_book(self, book_id):
        """Remove a book completely from the cart."""
        self.items = [i for i in self.items if i.book.book_id != book_id]

    def update_quantity(self, book_id, new_quantity):
        """Change the quantity of a book already in the cart."""
        for item in self.items:
            if item.book.book_id == book_id:
                if new_quantity <= 0:
                    self.remove_book(book_id)
                else:
                    item.quantity = new_quantity
                return

    def clear_cart(self):
        """Remove all books from the cart."""
        self.items = []

    @property
    def total_price(self):
        return sum(item.subtotal for item in self.items)

    @property
    def total_items(self):
        return sum(item.quantity for item in self.items)

    def display_cart(self):
        """Display the cart's content in the terminal."""
        if not self.items:
            print("Cart is empty.")
            return
        print("----- Cart Content -----")
        for item in self.items:
            print(item)
        print("-------------------------")
        print(f"Total items: {self.total_items}")
        print(f"Total price: {self.total_price:.2f} HTG")


# ---------- Usage example ----------
if __name__ == "__main__":
    # Create some books
    b1 = Book(1, "Gouverneurs de la rosée", "Jacques Roumain", 850.00, stock=10)
    b2 = Book(2, "Amour, colère et folie", "Marie Vieux-Chauvet", 950.00, stock=5)
    b3 = Book(3, "Compère Général Soleil", "Jacques-Stephen Alexis", 700.00, stock=8)

    # Create a customer
    customer = Customer(
        customer_id="CLI001",
        name="Jean Pierre",
        email="jean.pierre@email.com",
        phone="+509-1234-5678",
        address="Port-au-Prince, Haiti",
    )

    # Create a cart for the customer (the cart auto-links to customer.cart)
    cart = Cart(customer=customer)

    # Add books to the cart
    cart.add_book(b1, 2)
    cart.add_book(b2, 1)
    cart.add_book(b3, 3)

    # Display customer info
    print(customer)
    print()

    # Display the cart
    cart.display_cart()

    # Update a quantity
    cart.update_quantity(1, 5)

    # Remove a book
    cart.remove_book(2)

    print("\nAfter changes:")
    cart.display_cart()