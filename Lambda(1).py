"""
x = lambda hello, world, wolo: hello + world + wolo
print(x(4, 5, 7))
"""
def hellolam(num):
    return lambda x: num * x

sum = hellolam(5)
print(sum(6))