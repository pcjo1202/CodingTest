# 문제 솔루션
# 1. 문제를 입력받는다.
# 2. 입력 받은 문제 "OOXXOXXOOO"을 리스트로 저장한다.
# 3. 반복문을 통해 해당 문제 리스트를 돌면서...
#     - if O 이면서 ... [index - 1]도 O이면 점수 ++, 아니면 점수 = 1
#     - if O이 아니면 continue
#     - 마지막까지 다 돌면, print(점수)
#
T = int(input())

quiz = input('문제:').split()

print(list(quiz))
