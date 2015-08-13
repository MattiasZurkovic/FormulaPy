import math

def pythag(a, b, c):
    if c == 'x':
        return math.sqrt((a * a) + (b * b))
    if a == 'x':
        return math.sqrt((c * c) - (b * b))
    if b == 'x':
        return math.sqrt((c * c) - (a * a))



print(pythag('x', -3, -5))