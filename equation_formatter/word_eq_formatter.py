from .eq_formatter import EqFormatter


class WordEqFormatter(EqFormatter):
    """
    Tzuri will implement
    """

    @classmethod
    def eq(cls, *args: str) -> str:
        pass

    @classmethod
    def subscript(cls, base: str, sub) -> str:
        pass

    @classmethod
    def add(cls, *args: str) -> str:
        pass

    @classmethod
    def sub(cls, *args: str) -> str:
        pass

    @classmethod
    def mul(cls, *args: str) -> str:
        pass

    @classmethod
    def div(cls, numi: str, denom: str) -> str:
        pass

    @classmethod
    def pow(cls, base: str, expo: str) -> str:
        pass

    @classmethod
    def parenthesis(cls, expr: str) -> str:
        pass

    @classmethod
    def sqrt(cls, expr: str) -> str:
        pass

    @classmethod
    def nroot(cls, expr: str, n: int) -> str:
        pass

    @classmethod
    def warp_as_line(cls, s: str, *args, **kwargs) -> str:
        pass

    @classmethod
    def comma(cls, *args: str, sep=', ') -> str:
        pass
