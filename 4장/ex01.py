# 조건문의 실습(if - else 구문)

score = 60
# 관계식 다음의 콜론(:) 기호는 인터프리터에게 아직 문장이 끝나지 않음을 알리는 기호
# if - else 구문은 각각 50%의 확률을 가짐
if score >= 60:
    print("축하합니다. 합격입니다.")
else:
    print("불합격입니다. 다음에는 좋은 결과가 있길 바랍니다.")

age = int(input("나이를 입력하세요. >> "))

if age >= 19:
    print("주류 구입이 가능한 연령입니다.")
else:
    print("미성년자는 주류 구입이 어렵습니다.")