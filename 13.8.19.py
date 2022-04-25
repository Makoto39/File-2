n = int(input())

sum = 0

for i in range(n):
  age = int(input())
  if age < 18:
    sum = sum + 0
  elif 18 < age < 25:
    sum = sum + 990
  else:
    sum = sum + 1390

if n > 3:
  sum = sum * 0.9

print(sum)