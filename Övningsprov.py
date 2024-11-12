def numbers_between (tal1, tal2):
    for i in range(tal1+1, tal2):
        print(i)
numbers_between(12, 20)	

    
def is_alive(health):
    if health > 0:
        return True
    else:
        return False
    
print(is_alive(12))	# skriver ut True
print(is_alive(0))	# skriver ut False
print(is_alive(-3))	# skriver ut False

for i in range(101):
    if i % 3 == 0:
        print("Fizz")
    if i % 5 == 0:
        print("Buzz")
    if not (i % 3 == 0 or i % 5 ==0):
        print(i)
