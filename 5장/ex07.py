# 화씨 온도 - 섭씨 온도 변환 테이블 출력 프로그램
# for 문 사용, 실수로 나타내기
# 화씨 0도부터 100도까지 10도 단위로 증가시키며 대응되는 섭씨 온도를 출력
# 공식: C = (F - 32) * 5 / 9

for i in range(0, 101, 10):
    Cel = (i - 32) * 5 / 9
    print("화씨 온도가", i, "일 때, 섭씨 온도는 ", round(Cel, 2), "입니다.")

