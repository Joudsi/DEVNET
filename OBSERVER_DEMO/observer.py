# two types of customers -- business and consumerGrade

class BusinessCustomer:
    def __init__(self, acct_id, money_owed):
        """
        Constructor
        """
        self.acct_id = acct_id
        self.money_owed = money_owed

    def update(self):
        if self.money_owed > 0 :
            print(f"{self.acct_id}: Call the company's finance department")
        else:
            print(f"{self.acct_id}: Corprate balance paid")

class ConsumerCustomer:
    def __init__(self, acct_id, money_owed):
        """
        Constructor
        """
        self.acct_id = acct_id
        self.money_owed = money_owed
    # this update method is different than the one in the business class
    def update(self):
        if self.money_owed > 0 :
            print(f"{self.acct_id}: Send a polite reminder e-mail")
        else:
            print(f"{self.acct_id}: Individual balance paid")

class AccountingSystem:
    def __init__(self):
        """
        this constructor doesn't take any parameter and initializes a variable called customers to an empty set.
        """
        self.customers = set() # when a customer is registered it is added to the set

    def register(self, customer):
        self.customers.add(customer)

    def unregister(self,customer):
        self.customers.remove(customer)

    def notify(self):
        """
        this method loops over the customers set and invokes it's update method
        """
        for customer in self.customers:
            customer.update()


def main():
    """
    execution starts here.
    """

    # create a mix of business and consumer customers with varying balances
    cust1 = BusinessCustomer("ACCT100", 10)
    cust2 = BusinessCustomer("ACCT200", 0)
    cust3 = BusinessCustomer("ACCT300", -10)
    cust4 = BusinessCustomer("ACCT400", 20)

    # create the account system (subject) and register our new customers
    accounting_sys = AccountingSystem()
    accounting_sys.register(cust1)
    accounting_sys.register(cust2)
    accounting_sys.register(cust3)
    accounting_sys.register(cust4)

    # some event occured; notify all subscribers about their bills
    accounting_sys.notify()

    # one customer has cancelled their account
    print("** cust2 has cancelled their account")
    accounting_sys.unregister(cust2)

    # event occured again and norice how cust2 is not displayed
    accounting_sys.notify()

if __name__ == "__main__":
    main()

