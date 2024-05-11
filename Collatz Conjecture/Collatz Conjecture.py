#import
import matplotlib.pyplot as plt
import random

#variable
random_or_user = None

how_many = None

numbers = None

result = []



#function
def generate_collatz_sequence(x):  # x is the number
    """Generate the Collatz sequence for the given number"""
    while x > 1:
        if x % 2 == 0:
            # Divide x by 2
            x = x / 2
            result.append(x)
        else:
            # Multiply x by 3 and add 1
            x = 3 * x + 1
            result.append(x)


#intro
print("Welcome to the Collatz Conjecture Generator")
print("This program will generate the Collatz Conjecture sequence for any number")
numbers = int(input("Enter a number: "))
        

#main
generate_collatz_sequence(int(numbers))


#print result
for i in list(zip(range(len(result)), result)):
    plt.text(i[0], i[1], f"{i[1]}")

plt.plot(range(len(result)), result, marker='o', label='Collatz Sequence')
plt.xlabel('Iteration')
plt.ylabel('Value')
plt.title('Collatz Sequence')
plt.grid(True)
plt.legend()
plt.show()