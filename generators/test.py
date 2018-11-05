def rainbow():
  colors = ['red','orange','yellow','green', 'blue', 'purple']
  for color in colors:
    print(color)
    yield color


for r in rainbow():
  print(r)




