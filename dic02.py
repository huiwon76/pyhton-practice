#커피 주문 프로그램
#메뉴 선택하고 -> 돈을 입력하면 -> 거스름돈 계산

menus = {"아메리카노" : 4000, "카페라떼" : 4500, "카푸치노" : 5000}

print("=====메뉴판=====")

for menu, price in menus.items():
    print(f"{menu} : {price}원")

selected_menu = input("메뉴를 선택하세요.")
money = int(input("금액을 입력하세요."))

changes = money - menus.get(selected_menu)
print(f"거스름돈은 {changes}원 입니다.")