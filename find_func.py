import argparse
import numpy as np
from numbers import Real
from typing import Tuple, Type
from equation_formatter.eq_formatter import EqFormatter
from equation_formatter.word_eq_formatter import WordEqFormatter
from equation_formatter.libre_eq_formatter import LibreEqFormatter


class MathHelper(object):

    def __init__(self, formatter: Type[EqFormatter] = LibreEqFormatter, verbose=True):
        super().__init__()
        self.formatter = formatter
        self.verbose = verbose

    def print(self, s, add_newline=True):
        if self.verbose:
            print(self.formatter.warp_as_line(s, add_newline=add_newline), end='')

    def find_function(self, coefficients: Tuple[Real, Real], value1: Tuple[int, Real], value2: Tuple[int, Real]):
        """
        on an recursive ratio like:
        a_n = x a_{n-1} + y a_{n-2}

        and a pair of known bases are:
        a_n1 = z1
        a_n2 = z2

        :param coefficients: (x, y)
        :param value1: a tuple of (n1, z1)
        :param value2: a tuple of (n2, z2)
        """
        fmt = self.formatter.format
        fmtr = self.formatter
        c1, c2 = coefficients
        recursive = self._fmt_recursive_rat(c1, c2)
        self.print('"find exact formula for for " ' + recursive)
        characteristic = self._fmt_char_func(c1, c2)
        self.print(f'"characteristic equation is " ' + characteristic)
        roots = tuple((np.roots([1, -c1, -c2])))
        r1, r2 = roots
        self.print(self._fmt_trinom(-r1, -r2))
        self.print(fmtr.comma(
            fmtr.eq(fmtr.subscript('t', '1'), fmt(r1)),
            fmtr.eq(fmtr.subscript('t', '2'), fmt(r2))
        ))
        n1, v1 = value1
        n2, v2 = value2
        self.print(self._fmt_a_b_eq(n1, r1, r2, v1))
        self.print(self._fmt_a_b_eq(n2, r1, r2, v2))
        a, b = self._plug_with_values(roots, value1, value2)
        self.print(fmtr.eq('A', fmt(a)))
        self.print(fmtr.eq('B', fmt(b)))
        self.print(self._fmt_final_formula(a, b, r1, r2), False)
        print()
        return fmt(a), fmt(b)

    def _fmt_final_formula(self, a, b, r1, r2):
        fmtr = self.formatter
        fmt = self.formatter.format
        return fmtr.eq(
            fmtr.subscript('a', 'n'),
            fmtr.add(
                fmtr.mul(fmt(a), fmtr.pow(fmt(r1), 'n')),
                fmtr.mul(fmt(b), fmtr.pow(fmt(r2), 'n'))
            )
        )

    def _fmt_trinom(self, root_a, root_b):
        fmtr = self.formatter
        fmt = self.formatter.format
        return fmtr.eq(
            fmtr.parenthesis(fmtr.add('t', fmt(root_a))) +
            fmtr.parenthesis(fmtr.add('t', fmt(root_b))),
            '0'
        )

    def _fmt_a_b_eq(self, n, r1, r2, v):
        fmtr = self.formatter
        fmt = self.formatter.format
        return fmtr.eq(
            fmtr.subscript('a', fmt(n)),
            fmtr.add(
                'A ' + fmtr.pow(fmt(r1), fmt(n)),
                'B ' + fmtr.pow(fmt(r2), fmt(n)),
            ),
            fmt(v)
        )

    def _fmt_char_func(self, c1, c2):
        fmtr = self.formatter
        fmt = self.formatter.format
        characteristic = fmtr.eq(
            fmtr.add(
                fmtr.pow('t', '2'),
                f'-{fmt(c1)}t',
                f'-{fmt(c2)}'
            ),
            '0'
        )
        return characteristic

    def _fmt_recursive_rat(self, c1, c2):
        fmt = self.formatter.format
        fmtr = self.formatter
        return fmtr.eq(
            fmtr.subscript('a', 'n'),
            fmtr.add(
                fmt(c1) + fmtr.subscript('a', 'n-1'),
                fmt(c2) + fmtr.subscript('a', 'n-2')
            )
        )

    def _plug_with_values(self, char_eq_roots: Tuple[Real, Real], value1: Tuple[int, Real], value2: Tuple[int, Real]):
        """
        if `a_n = z` than value1 and value2 are a specific tuple of (n, z)
        """
        r1, r2 = char_eq_roots
        n1, v1 = value1
        n2, v2 = value2
        return tuple((x for x in np.linalg.inv([[r1**n1, r2**n1], [r1**n2, r2**n2]]).dot([v1, v2])))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("c1", help="coefficient of a_n-1",
                        type=float)
    parser.add_argument("c2", help="coefficient of a_n-2",
                        type=float)
    parser.add_argument("n1", help="index of a specific a_n",
                        type=float)
    parser.add_argument("a_n1", help="value of a specific a_n",
                        type=float)
    parser.add_argument("n2", help="index of a specific a_n",
                        type=float)
    parser.add_argument("a_n2", help="value of a specific a_n",
                        type=float)
    parser.add_argument("-t", "--type", choices=('word', 'libre'), default='word')
    args = parser.parse_args()
    MathHelper(formatter=WordEqFormatter if args.type == 'word' else LibreEqFormatter).find_function(
        (args.c1, args.c2),
        (args.n1, args.a_n1),
        (args.n2, args.a_n2)
    )


if __name__ == '__main__':
    main()
