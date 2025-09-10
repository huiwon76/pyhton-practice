#while 반복 while True 사용
#메뉴를 선택한다. (여러개의 메뉴를 선택 한다.)
#구매한 메뉴를 리스트로 보관도 해야 한다.
#현금을 넣는다.
#구매한후에 거스름돈을 받는다.
#구매했던 리스트와 총 구매가격? 출력!!!

menus = {"아메리카노":4000, "카페라떼": 4500, "카푸치노": 5000}

order_list = []
total_price = 0

print("=====메뉴판=====")

for menu, price in menus.items():
    print(f"{menu} : {price}원")

while True :
    selected_menu = input("주문할 메뉴를 입력하세요.")
    price = menus.get(selected_menu,0)

    if price != 0 :
        order_list.append(selected_menu)
        total_price = total_price + price
    elif selected_menu =="q" :
        print("주문 완료")
        break
    else:
        print("메뉴가 없습니다.")

print(f"선택한 메뉴 : {order_list}")

money = int(input("금액을 입력하세요."))
change = money - total_price
if change >= 0 :
    print(f"총 금액은 {total_price}원입니다. 거스름돈은 {change}원 입니다.")
else:
    print("돈이 부족합니다.")