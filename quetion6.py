orders = [] #stack
pderiveries = [] #queue
groceries = [] #list

#add groceries
def addGroceries(grocery):
    groceries.append(grocery)
addGroceries('burger')
print("the available groceries are:")
print(groceries)
def pendingDeriveries(user,grocery):
    delivery = {
        "user" : user,
        "grocery": grocery
    }
    if grocery in groceries:
        pderiveries.append(delivery)
    else:
        print('the grocery was not found')
pendingDeriveries('kellen','burger')
print("pending deliveries are:")
print(pderiveries)
def returnOrder():
    if pderiveries:
        order = pderiveries.pop(0)
        orders.append(order)
returnOrder()
print("returned orders are:")
print(orders)

def terminateOrder():
    if orders:
        orders.pop()
terminateOrder()
print("returned orders are:")
print(orders)


