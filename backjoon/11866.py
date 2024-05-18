#입력
# N, K  = map(int, input("입력해: ").split())
N, K = (7,3)

#구현
result_list = []

start = 0

peo = [i for i in range(1, 7)]

for _ in range(N):
  start += K - 1
  start %= len(peo)
  result_list.append(peo.pop(start))

# print(f'<{",".join(map(str, result_list))}>')
  print()