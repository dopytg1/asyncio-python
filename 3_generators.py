def gen1(s):
    for i in s:
        yield i


def gen2(n):
    for i in range(n):
        yield i


g1 = gen1("tima")
g2 = gen2(4)

gens = [g2, g1]

while gens:
    task = gens.pop(0)

    try:
        print(next(task))
        gens.append(task)
    except StopIteration:
        pass
