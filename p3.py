def out(s: str) -> None:
    print(s, end='')


def show(vals: list[bool]) -> None:
    def hline(fill: int) -> None:
        out(' ---- \n' if vals[fill] else '\n')

    def vlines(left: int, right: int) -> None:
        w1 = '|' if vals[left] else ' '
        w2 = '|' if vals[right] else ' '
        out(f'{w1}    {w2}\n' * 2)

    a, b, c, d, e, f, g, dt = range(8)

    hline(a)
    vlines(f, b)
    hline(g)
    vlines(e, c)
    hline(d)
    out('      o\n' if vals[dt] else '\n')


def get_bits(a: bool, b: bool, c: bool, d: bool) -> list[bool]:
    return [
        # a
        c & (b | (not a & d))
        | (not c) & ((a & (not b & d)) | (not b | d))
        | (not a) & b & d,

        # b
        (not (a | (b & (c ^ d))))
        | a & ((not (b | d)) | (not c) & d),

        # c
        (not a) & ((not c) | d)
        | (not c) & d
        | (a ^ b),

        # d
        a & (not c)
        | b & (c ^ d)
        | (not b) & c & d
        | (not a | b | d),

        # e
        a & (b | c)
        | c & (not d)
        | (not c | b | d),

        # f
        a & ((not b) | c)
        | (not c | d & (a | (not b)))
        | b & c & (not d),

        # g
        a & ((not b) | b & d)
        | c & (not d & (a | b))
        | (not a) & b & (not c),

        False,
    ]


for i in range(16):
    brepr: str = bin(i)[2:].rjust(4, '0')
    bits = get_bits(*map(bool, (map(int, brepr))))
    print(str(i).rjust(2), brepr,  ''.join(map(lambda x: str(int(x)), bits)))
    show(bits)
