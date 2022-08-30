import random

time = random.randrange(5, 51)
customer = range(1,51)
count = 0

for i in customer:
  time = random.randrange(5, 51)
  if 5 <= time <= 15: 
    print(f'[0] {i}번째 손님 (소요시간: {time}분) ')
    count+=1
  else:
    print(f'[] {i}번째 손님 (소요시간: {time}분) ')
  i+=1
print('\n')
print(f'총 탑승 승객: {count}')
