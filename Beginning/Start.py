def food(Fo="Nothing!"):
    print("You like eating", Fo)
food()
eat = input("What is your favourite food?").strip()
food(eat)



def main():
    name = input("What is your name?")
    hello(name)

def hello(to="World"):
    print("hello",to)


main()