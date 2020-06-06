def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i-1)

# the following code leads to an infinite loop.
# def countdown(i):
#     print(i)
#     countdown(i-1)