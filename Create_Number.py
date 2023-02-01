# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

def create_number(a):
    # For converting array into a string
    string =  ''.join(str(x) for x in a)
    return f"({string[0:3]}) {string[3:6]}-{string[6:len(string)]}"
print(create_number([1,2,3,4,5,6,7,8,9,0]))