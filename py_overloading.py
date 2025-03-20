from typing import Any, Callable

def overload(f: Callable[..., Any], overloads: dict[str, Callable[..., Any]] = dict()):

    tp_names = [tp.__name__ for tp in list(f.__annotations__.values())[:-1]]
    overloads['_'.join([f.__name__, *tp_names])] = f

    def indirect_f(*args, **kwargs):

        arg_tp_names = [type(arg).__name__ for arg in [*args, *kwargs.values()]]
        if specific_f := overloads.get('_'.join([f.__name__, *arg_tp_names])):
            return specific_f(*args, **kwargs)

        raise TypeError(f'No overload found for {f.__name__}({', '.join(arg_tp_names)})')

    indirect_f.__name__ = f.__name__

    return indirect_f

