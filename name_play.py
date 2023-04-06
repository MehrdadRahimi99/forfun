name = input("enter your name: ")

re_name = "".join(list(reversed(name)))

big_name = re_name + name

x = int(len(big_name)/2) - 1
y = x + 1
print(" "*int(x), big_name[x:y+1])
x -= 1
y += 1

for i in big_name:
    print(" "*int(x), big_name[x], " "*int(y-(x+1)-2), big_name[y])
    x -= 1
    y += 1
    if x < 0 or y >= len(big_name):
        
        break
x = 0
y = len(big_name) - 1

for i in big_name:
    print(" "*int(x), big_name[x], " "*int(y-(x+1)-2), big_name[y])
    x += 1
    y -= 1
    if x == y == len(big_name)//2:
        break

print(" "*int(x), big_name[x]*2)
