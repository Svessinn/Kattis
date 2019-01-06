h, v = map(int, input().split())
import math
c = h*math.sin(math.radians(90))/math.sin(math.radians(v))
print(math.ceil(c))
