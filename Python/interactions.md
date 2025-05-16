def loop(i: int) -> float:
  d: int = 2
  x: int = 0
  for i in range (0,i):
    x += (i+d)
    d -= 1
  return x

print("O interaction:", loop(0))
print("1 interaction:", loop(1))
print("2 interaction:", loop(2))
print("3 interaction:", loop(3))
