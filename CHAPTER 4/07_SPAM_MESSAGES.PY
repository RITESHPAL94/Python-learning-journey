phrase1 = "Make a lot of money"
phrase2 = "buy now"
phrase3 = "subscribe this"
phrase4 = "click this"

message = input("Enter your comment: ")

if ((phrase1 in message) or (phrase2 in message) or (phrase3 in message) or (phrase4 in message)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")