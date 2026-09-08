"""Separate decimal replay of the nine-step certificate printed in proof.md."""

from decimal import Decimal, localcontext
from pathlib import Path


def main():
    printed = {}
    for line in Path(__file__).with_name('proof.md').read_text().splitlines():
        fields = line.split()
        if len(fields) == 2 and all(field.isdigit() for field in fields):
            printed[int(fields[0])] = int(fields[1])
    with localcontext() as ctx:
        ctx.prec = 100
        u, values = Decimal(4070947), {1: 4070947}
        for s in range(2, 12):
            numerator, denominator = Decimal(1048576 + s) * u, Decimal(67472 + s)
            v = Decimal(int(numerator / denominator))
            # These products of small integers are exact at this precision.
            assert denominator * v <= numerator < denominator * (v + 1)
            u, values[s] = v, int(v)
        assert printed == values
        total = Decimal(values[10]) + 134944
        assert total == 215108323408324109
        assert Decimal(274980728111395087) - total == 59872404703070978
        assert values[11] > 274980728111395087
    print('PASS: independent decimal certificate matches the printed table; '
          'rank-eleven total 215108323408324109; next rank over budget')


if __name__ == '__main__':
    main()
