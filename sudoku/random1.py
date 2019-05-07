import random
target="871264395923758461465319278716435829594826137382971654657142983248593716139687542"
predicted="958723444712538675643484764464446637454558436494435439475444592238683446456574573"

p = 0
r = 0

for x in range(len(target)):
    if target[x] == predicted[x]:
        p += 1
    if str(random.randint(1,10)) == target[x]:
        r += 1

print("p:" + str(p))
print("r:" + str(r))
