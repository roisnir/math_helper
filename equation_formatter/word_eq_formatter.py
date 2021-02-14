from .eq_formatter import EqFormatter


class WordEqFormatter(EqFormatter):
    """
    """
    @classmethod
    def subscript(cls, base: str, sub) -> str:
        return f'{base}_({sub})'

    @classmethod
    def eq(cls, *args: str) -> str:
        return ' = '.join(args)

    @classmethod
    def mul(cls, *args: str) -> str:
        return r' \cdot '.join([
            cls.parenthesis(a) if a.lstrip().startswith('-') else a
            for a in args])

    @classmethod
    def add(cls, *args: str) -> str:
        s = args[0]
        for a in args[1:]:
            if a.lstrip().startswith('-'):
                s += a
            else:
                s += ' + ' + a
        return s

    @classmethod
    def sub(cls, *args: str) -> str:
        return ' - '.join(args)

    @classmethod
    def div(cls, numi: str, denom: str) -> str:
        return f'({numi})/({denom})'

    @classmethod
    def pow(cls, base: str, expo: str) -> str:
        base = cls.parenthesis(base) if base.lstrip().startswith('-') else base
        return f'({base})^({expo})'

    @classmethod
    def parenthesis(cls, expr: str) -> str:
        return f'({expr})'

    @classmethod
    def sqrt(cls, expr: str) -> str:
        return f'\\sqrt({expr})'

    @classmethod
    def nroot(cls, expr: str, n: int) -> str:
        return f'\\sqrt({n}&{expr})'

    @classmethod
    def warp_as_line(cls, s: str, add_newline=True) -> str:
        return s + ('\r\n' if add_newline else '')

    @classmethod
    def comma(cls, *args, sep=', ') -> str:
        return sep.join(args)

    @classmethod
    def big_comma(cls, *args: str, sep=', ') -> str:
        return f'{sep}'.join(args)
