from functools import reduce


print(reduce(lambda x, y: x * y,
      map(lambda x: int(x)**5, 
          open('input.txt', 'r', encoding='utf8').readline().split())))
