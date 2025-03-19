class Product(): #A
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self): #B
        total_price = self.price*self.quantity
        return total_price

#C
siers = Product("Holandes",4,3)
print("Produkts 1: ",siers.get_total_price())

maize = Product("Rudzu",2,2)
print("Produkts 2: ",maize.get_total_price())

#2.uzd - iepirkumu grozs
class ShoppingCart(): #D
    def add_product_to_cart(self, product):
        print("Produkts: ",product.name,"pievienots grozam.")

    def remove_product_from_cart(self, product):
        print("Produkts: ",product.name,"noņemts no groza.")

    def get_total_price(self, product):
        print("Kopējā summa: ",product.get_total_price())

#objekti shopping cart klasei
iepirkumu_grozs = ShoppingCart()
iepirkumu_grozs.add_product_to_cart(siers)
iepirkumu_grozs.get_total_price(siers)
iepirkumu_grozs.remove_product_from_cart(siers)

class SystemUser():
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    #nomainīt eksistējošos atribūtus
    def set_user_info(self, newusername, newpassword, newemail):
        self.username =newusername
        self.password=newpassword
        self.email = newemail
        print("Informācija ir nomainīta")

    def get_user_info(self):
        print("Informācija par lietotāju-----")
        print("Lietotājs: ",self.username)
        print("Parole: ",self.password)
        print("Email: ",self.email)

#K
Liene = SystemUser("Liene", "123456", "liene@gmail.com")
#nomainīt info un parādīt
Liene.set_user_info("Liene Saule","123","lienesaule@gmail.com") #uzstāda jaunu info
Liene.get_user_info() #parāda nomainītos datus

class Customer(SystemUser):
    def __init__(self, username, password, email, customer_id, purchase_history, membership_status):
        super().__init__(username, password, email)
        #N pievieno atribūtus
        self.customer_id = customer_id
        self.purchase_history = purchase_history
        self.membership_status = membership_status
    #M
    def set_user_info(self, newusername, newpassword, newemail,new_customer_id, new_purchase_history, new_membership_status):
        #izsaukt bāzes metodi +3jauni atribūti
        super().set_user_info(newusername, newpassword, newemail)
        self.customer_id=new_customer_id
        self.purchase_history=new_purchase_history
        self.membership_status = new_membership_status

    def get_user_info(self):
        super().get_user_info()
        print("Informācija par lietotāju-----")
        print("Customer ID: ",self.customer_id)
        print("Purchase history: ",self.purchase_history)
        print("Membership statuss: ",self.membership_status)

#O - klienta objekts ar atjauninātu info
Karlis = Customer("karlis4","1234","karlis@svg.lv",13,"","") #tukšas jo nav pirkumu vesture un memberships
#atjaunināt info
Karlis.set_user_info("karlis5","123456","karlis@gmail.com",13,"Āboli","Zelta klients")
Karlis.get_user_info()