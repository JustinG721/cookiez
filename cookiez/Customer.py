from cookiez.models import Customer

#because tim timtam is the only dude that exists currently

def insertCustomer():
    customer = Customer(firstname="tim", lastname="timtam")
    customer.save()

def retrieveCustomer():
    customer = Customer.objects.get(custid=1)
    return customer
