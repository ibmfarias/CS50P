def main(): 
    name = input("What's you name? ").title()
    hello(name)
    
def hello(to="world"):
    print("hello,", to)

main()


