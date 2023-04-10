#Define a function to find prime numbers

def Is_Prime(num):
    Prime = True
    for a in range(2, int(num**0.5)+1):
            if num % a == 0:
                Prime = False
                break
    return Prime

#Place the function in the desired range
prime_count = 0

for a in range(1,101):
    if Is_Prime(a):
        prime_count += 1
        print(a, end=" ")
        
#Display the final result
print("")
print("we have", prime_count , "prime number")