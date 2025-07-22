def main(): 
    name = input("What's you name? ").capitalize()
    hello(name)
    
def hello(to="world"):
    print("hello,", to)

main()


