fruits = ["사과", "바나나", "오렌지"]
numbers = [1, 2, 3, 4, 5]

print(type(fruits))
print(fruits)

print(f"과일의 첫 번째 : {fruits[0]}")
print(f"과일의 두 번째 : {fruits[1]}")
print(f"과일의 세 번째 : {fruits[2]}")

for fruit in fruits :
    print(f"과일 : {fruit}")

for i in range(3) :
    print(f"과일 : {fruits[i]}")

for i in range(len(fruits)) :
    print(f"과일 : {fruits[i]}")

for i in range(len(fruits)) :
    print(f"{i+1}번째 과일 : {fruits[i]}")

for i, fruit in enumerate(fruits):
    print(f"{i+1}번째 과일 : {fruit}")