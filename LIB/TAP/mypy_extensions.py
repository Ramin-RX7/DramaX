"""
https://github.com/python/mypy_extensions
"""

"""Defines experimental extensions to the standard "typing" module that are
supported by the mypy typechecker.

Example usage:
    from mypy_extensions import TypedDict
"""

from typing import Any

import sys
# _type_check is NOT a part of public typing API, it is used here only to mimic
# the (convenient) behavior of types provided by typing module.
from typing import _type_check  # type: ignore


def _check_fails(cls, other):
    try:
        if sys._getframe(1).f_globals['__name__'] not in ['abc', 'functools', 'typing']:
            # Typed dicts are only for static structural subtyping.
            raise TypeError('TypedDict does not support instance and class checks')
    except (AttributeError, ValueError):
        pass
    return False


def _dict_new(cls, *args, **kwargs):
    return dict(*args, **kwargs)


def _typeddict_new(cls, _typename, _fields=None, **kwargs):
    total = kwargs.pop('total', True)
    if _fields is None:
        _fields = kwargs
    elif kwargs:
        raise TypeError("TypedDict takes either a dict or keyword arguments,"
                        " but not both")

    ns = {'__annotations__': dict(_fields), '__total__': total}
    try:
        # Setting correct module is necessary to make typed dict classes pickleable.
        ns['__module__'] = sys._getframe(1).f_globals.get('__name__', '__main__')
    except (AttributeError, ValueError):
        pass

    return _TypedDictMeta(_typename, (), ns)


class _TypedDictMeta(type):
    def __new__(cls, name, bases, ns, total=True):
        # Create new typed dict class object.
        # This method is called directly when TypedDict is subclassed,
        # or via _typeddict_new when TypedDict is instantiated. This way
        # TypedDict supports all three syntaxes described in its docstring.
        # Subclasses and instances of TypedDict return actual dictionaries
        # via _dict_new.
        ns['__new__'] = _typeddict_new if name == 'TypedDict' else _dict_new
        tp_dict = super(_TypedDictMeta, cls).__new__(cls, name, (dict,), ns)

        anns = ns.get('__annotations__', {})
        msg = "TypedDict('Name', {f0: t0, f1: t1, ...}); each t must be a type"
        anns = {n: _type_check(tp, msg) for n, tp in anns.items()}
        for base in bases:
            anns.update(base.__dict__.get('__annotations__', {}))
        tp_dict.__annotations__ = anns
        if not hasattr(tp_dict, '__total__'):
            tp_dict.__total__ = total
        return tp_dict

    __instancecheck__ = __subclasscheck__ = _check_fails


TypedDict = _TypedDictMeta('TypedDict', (dict,), {})
TypedDict.__module__ = __name__
TypedDict.__doc__ = \
    """A simple typed name space. At runtime it is equivalent to a plain dict.

    TypedDict creates a dictionary type that expects all of its
    instances to have a certain set of keys, with each key
    associated with a value of a consistent type. This expectation
    is not checked at runtime but is only enforced by typecheckers.
    Usage::

        Point2D = TypedDict('Point2D', {'x': int, 'y': int, 'label': str})
        a: Point2D = {'x': 1, 'y': 2, 'label': 'good'}  # OK
        b: Point2D = {'z': 3, 'label': 'bad'}           # Fails type check
        assert Point2D(x=1, y=2, label='first') == dict(x=1, y=2, label='first')

    The type info could be accessed via Point2D.__annotations__. TypedDict
    supports two additional equivalent forms::

        Point2D = TypedDict('Point2D', x=int, y=int, label=str)

        class Point2D(TypedDict):
            x: int
            y: int
            label: str

    The latter syntax is only supported in Python 3.6+, while two other
    syntax forms work for 3.2+
    """

# Argument constructors for making more-detailed Callables. These all just
# return their type argument, to make them complete noops in terms of the
# `typing` module.


def Arg(type=Any, name=None):
    """A normal positional argument"""
    return type


def DefaultArg(type=Any, name=None):
    """A positional argument with a default value"""
    return type


def NamedArg(type=Any, name=None):
    """A keyword-only argument"""
    return type


def DefaultNamedArg(type=Any, name=None):
    """A keyword-only argument with a default value"""
    return type


def VarArg(type=Any):
    """A *args-style variadic positional argument"""
    return type


def KwArg(type=Any):
    """A **kwargs-style variadic keyword argument"""
    return type


# Return type that indicates a function does not return
class NoReturn: pass


def trait(cls):
    return cls


def mypyc_attr(*attrs, **kwattrs):
    return lambda x: x


# TODO: We may want to try to properly apply this to any type
# variables left over...
class _FlexibleAliasClsApplied:
    def __init__(self, val):
        self.val = val

    def __getitem__(self, args):
        return self.val


class _FlexibleAliasCls:
    def __getitem__(self, args):
        return _FlexibleAliasClsApplied(args[-1])


FlexibleAlias = _FlexibleAliasCls()


class _NativeIntMeta(type):
    def __instancecheck__(cls, inst):
        return isinstance(inst, int)


_sentinel = object()


class i64(metaclass=_NativeIntMeta):
    def __new__(cls, x=0, base=_sentinel):
        if base is not _sentinel:
            return int(x, base)
        return int(x)


class i32(metaclass=_NativeIntMeta):
    def __new__(cls, x=0, base=_sentinel):
        if base is not _sentinel:
            return int(x, base)
        return int(x)


class i16(metaclass=_NativeIntMeta):
    def __new__(cls, x=0, base=_sentinel):
        if base is not _sentinel:
            return int(x, base)
        return int(x)


class u8(metaclass=_NativeIntMeta):
    def __new__(cls, x=0, base=_sentinel):
        if base is not _sentinel:
            return int(x, base)
        return int(x)


for _int_type in i64, i32, i16, u8:
    _int_type.__doc__ = \
        """A native fixed-width integer type when used with mypyc.

        In code not compiled with mypyc, behaves like the 'int' type in these
        runtime contexts:

        * {name}(x[, base=n]) converts a number or string to 'int'
        * isinstance(x, {name}) is the same as isinstance(x, int)
        """.format(name=_int_type.__name__)
del _int_type