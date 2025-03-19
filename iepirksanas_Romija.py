#A - izveidota klase ar norādītajiem atribūtiem
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    #B - metode, kas nosaka pirkuma kopējo cenu, balstoties uz cenu un daudzumu
    def get_total_price(self):
        total_price = self.price*self.quantity
        print("Kopējā cena ir: ",total_price)

#C - izveidoti 2 objekti, kuriem aprēķina pirkuma summu
produkts1 = Product("Šokolāde", 2, 3)
produkts1.get_total_price()

produkts2 = Product("Pulkstenis", 200, 1)
produkts2.get_total_price()

#D - izveidota klase, kas imitē iepirkuma grozu
class ShoppingCart(Product):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        
    #E - izveidotas metodes šai klasei
    def add_product_to_cart(self):
        pass

    def remove_product_from_cart(self):
        pass

    def get_total_price(self):
        total_price = self.price*self.quantity
        print("Kopējā cena ir: ",total_price)

#H - definēta klase SystemUser
class SystemUser:
    def __init__(self, username, password, email): #I - izveidoti attiecīgie atribūti
        self.username = username
        self.password = password
        self.email = email

    #J - izveidotas attiecīgās metodes
    def set_user_info(self):
        pass

    def get_user_info(self):
        pass

#L - klase, kas manto no SystemUser
class Customer(SystemUser):
    def __init__(self, username, password, email, customer_id, purchase_history, membership_status): #M - pievienoti jauni lauki
        super().__init__(username, password, email)
        self.customer_id = customer_id
        self.purchase_history = purchase_history
        self.membership_status = membership_status
