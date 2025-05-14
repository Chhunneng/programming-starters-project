def loop(i: int) -> float:
  d: int = 2
  x: int = 0
  for i in range (0,i):
    x += (i+d)
    d -= 1
  return x

print("O interação:", loop(0))
print("1 interação:", loop(1))
print("2 interação:", loop(2))
print("3 interação:", loop(3))
