def main():
        x = int(input("Qual o valor de x? "))
        print("x squared is", square(x) )

def square(n):
        #return n * n
        #return n ** 2
        return pow (n, 2)
        
main()
