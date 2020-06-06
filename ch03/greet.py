def greet(name):
    print("hello, {}!".format(name))
    greet2(name)
    print("getting ready to say bye...")
    bye()

def greet2(name):
    print("how are you, {}?".format(name))

def bye():
    print("ok bye!")

greet("mingda")
