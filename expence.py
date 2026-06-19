import json
print("1.add expense \n 2.show expense \n 3.total expence")
store = []
#add expense
#show expense
#total expence
def add_expense(val):
    
    store.append(val)
    print(f"you is added to file{val}")
def show_expense():
    print(f"this is your expence {store}")
def total_expense():
    a = 0
    for x in store :
        a = a + x
    print(f"your total value is {a} ")
 
 
off = True
while off :
    task  = input("enter the number of you chose task :")
    if task == "1":
        val = int(input("enter your expence amount :"))
        add_expense(val)
    elif task == "2":
        show_expense()
    elif task == "3":
        total_expense()
    else :
        off  = False

