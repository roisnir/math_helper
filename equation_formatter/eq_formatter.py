from abc import ABC, abstractmethod
from typing import Union
from sympy import nsimplify
from sympy.core import Expr as SymPyExpr
from sympy.core import Pow, Mul, Rational, Integer, Number as SymPyNum
from numbers import Number


Expr = Union[SymPyExpr, Number, SymPyNum]


class EqFormatter(ABC):
    @classmethod
    def _format(cls, expr: Expr) -> str:
        fmt = cls.format
        if isinstance(expr, float):
            return cls.format(nsimplify(expr))
        if isinstance(expr, (Integer, int)):
            return str(expr)
        if isinstance(expr, Rational):
            return cls.div(expr.numerator(), expr.denominator())
        if isinstance(expr, Pow):
            if expr.exp < 1:
                if expr.exp == 1/2:
                    return cls.sqrt(fmt(expr.base))
                return cls.nroot(fmt(expr.base), expr.exp.denominator())
            return cls.pow(fmt(expr.base, True), expr.exp)
        if isinstance(expr, Mul):
            return cls.mul(*[fmt(a, True) for a in expr.args])
        raise ValueError("haven't thought it would get to here")

    @classmethod
    def format(cls, raw_expr: Expr, parenthesis_on_minus=False) -> str:
        expr = cls._format(raw_expr)
        if expr.lstrip().startswith('-') and parenthesis_on_minus:
            return cls.parenthesis(expr)
        return expr

    @classmethod
    @abstractmethod
    def eq(cls, *args: str) -> str:
        ...

    @classmethod
    @abstractmethod
    def subscript(cls, base: str, sub) -> str:
        """
        how to create a_n
        """
        ...

    @classmethod
    @abstractmethod
    def add(cls, *args: str) -> str:
        ...

    @classmethod
    @abstractmethod
    def sub(cls, *args: str) -> str:
        ...

    @classmethod
    @abstractmethod
    def mul(cls, *args: str) -> str:
        ...

    @classmethod
    @abstractmethod
    def div(cls, numi: str, denom: str) -> str:
        ...

    @classmethod
    @abstractmethod
    def pow(cls, base: str, expo: str) -> str:
        ...

    @classmethod
    @abstractmethod
    def parenthesis(cls, expr: str) -> str:
        ...

    @classmethod
    @abstractmethod
    def sqrt(cls, expr: str) -> str:
        ...

    @classmethod
    @abstractmethod
    def nroot(cls, expr: str, n: int) -> str:
        ...

    @classmethod
    @abstractmethod
    def warp_as_line(cls, s: str, *args, **kwargs) -> str:
        ...

    @classmethod
    @abstractmethod
    def comma(cls, *args: str, sep=', ') -> str:
        ...
