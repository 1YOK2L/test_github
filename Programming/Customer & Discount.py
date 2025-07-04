from datetime import date

class DiscountRate:
    SERVICE_GOLD = 20
    SERVICE_SILVER = 15
    PRODUCT_GOLD = 10
    PRODUCT_SILVER = 10

    @staticmethod
    def get_service_discount(member_type: str):
        if member_type == "gold":
            return DiscountRate.SERVICE_GOLD
        elif member_type == "silver":
            return DiscountRate.SERVICE_SILVER
        return 0

    @staticmethod
    def get_product_discount(member_type: str):
        if member_type in ["gold", "silver"]:
            return DiscountRate.PRODUCT_GOLD
        return 0

class Customer:
    TYPE_GOLD = "gold"
    TYPE_SILVER = "silver"
    TYPE_NONE = "none"

    def __init__(self, name: str, member_type: str = None):
        self.name = name
        self.is_member = member_type is not None
        self.member_type = member_type or Customer.TYPE_NONE

    def __repr__(self):
        return f"[{self.member_type}] {self.name}"

class Visit:
    def __init__(self, customer: Customer, visit_date: date):
        self.customer = customer
        self.visit_date = visit_date
        self.service_expense = 0
        self.product_expense = 0

    def add_service_expense(self, amount: int):
        self.service_expense += amount

    def add_product_expense(self, amount: int):
        self.product_expense += amount

    def total_price(self):
        return self.service_expense + self.product_expense

    def gross_price(self):
        return self.total_price()

    def total_discount(self):
        service_discount = DiscountRate.get_service_discount(self.customer.member_type)
        product_discount = DiscountRate.get_product_discount(self.customer.member_type)
        
        service_discount_amount = (self.service_expense * service_discount) / 100
        product_discount_amount = (self.product_expense * product_discount) / 100
        
        total_discount = service_discount_amount + product_discount_amount
        return total_discount

    def __repr__(self):
        visit_date_str = self.visit_date.strftime("%d/%m/%Y")
        
        discount = self.total_discount()
        payment = self.gross_price() - discount
        
        return f"{self.customer} - visited on {visit_date_str}, bought {self.total_price()} with a discount of {discount:.1f}, payment {payment:.1f}"

if __name__ == "__main__":
    john = Customer("John", Customer.TYPE_GOLD)

    john_visit = Visit(john, date(2023, 8, 1))
    john_visit.add_product_expense(1000)
    john_visit.add_service_expense(500)

    print(john_visit)