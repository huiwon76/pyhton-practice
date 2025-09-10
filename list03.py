# 아래는 5명의 학생들의 성적을 입력 받아서
# 최고값, 최소값, 평균값, 90점 이상의 count 프로그램
# 5명의 학생들의 성적을 입력 -> list [] 에 저장

STUDENTS = 5
lst = []
count = 0

for i in range(STUDENTS):
    value = int(input(f"{i+1}번째 학생의 성적을 입력하세요."))
    lst.append(value)

print(f"최대 점수 : {max(lst)}")
print(f"최소 점수 : {min(lst)}")
print(f"평균 점수 : {sum(lst)/len(lst)}")

for score in lst:
    if score >= 80:
        count +=1   # 이것은 count = count + 1 과 동일

print(f"80점 이상 학생 {count}명입니다.")
