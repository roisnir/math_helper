from .eq_formatter import EqFormatter


class LibreEqFormatter(EqFormatter):
    @classmethod
    def subscript(cls, base: str, sub) -> str:
        return f'{base}_{{{sub}}}'

    @classmethod
    def eq(cls, *args: str) -> str:
        return ' `=` '.join(args)

    @classmethod
    def mul(cls, *args: str) -> str:
        return ' `cdot` '.join([
            cls.parenthesis(a) if a.lstrip().startswith('-') else a
            for a in args])

    @classmethod
    def add(cls, *args: str) -> str:
        s = args[0]
        for a in args[1:]:
            if a.lstrip().startswith('-'):
                s += a
            else:
                s += ' `+` ' + a
        return s

    @classmethod
    def sub(cls, *args: str) -> str:
        return ' `-` '.join(args)

    @classmethod
    def div(cls, numi: str, denom: str) -> str:
        return f'{{{numi}}} over {{{denom}}}'

    @classmethod
    def pow(cls, base: str, expo: str) -> str:
        base = cls.parenthesis(base) if base.lstrip().startswith('-') else base
        return f'{{{base}}}^{{{expo}}}'

    @classmethod
    def _is_tall(cls, expr: str) -> bool:
        return any((e in expr) for e in ('over', 'binom'))

    @classmethod
    def parenthesis(cls, expr: str) -> str:
        lp = 'left(' if cls._is_tall(expr) else '('
        rp = 'right)' if cls._is_tall(expr) else ')'
        return f'{lp} {expr} {rp}'

    @classmethod
    def sqrt(cls, expr: str) -> str:
        return f'sqrt{{ {expr} }}'

    @classmethod
    def nroot(cls, expr: str, n: int) -> str:
        return f'nroot {{{n}}} {{{expr}}}'

    @classmethod
    def warp_as_line(cls, s: str, add_newline=True) -> str:
        return f'alignl stack {{ alignc\r\n{s}\r\n}}' + (' newline ' if add_newline else '')

    @classmethod
    def comma(cls, *args, sep=',` ') -> str:
        return sep.join(args)

    @classmethod
    def big_comma(cls, *args: str, sep=',~ ') -> str:
        return f'{sep} '.join(args)
