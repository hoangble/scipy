# This file is not meant for public use and will be removed in SciPy v2.0.0.
# Use the `scipy.sparse.linalg` namespace for importing the functions
# included below.

from scipy._lib.deprecation import _sub_module_deprecation


__all__ = [  # noqa: F822
    'MatrixRankWarning', 'SuperLU', 'factorized',
    'spilu', 'splu', 'spsolve',
    'spsolve_triangular', 'use_solver', 'linsolve', 'test'
]

dsolve_modules = ['linsolve']


def __dir__():
    return __all__


def __getattr__(name):
    # if name not in __all__ and name not in dsolve_modules:
    #     raise AttributeError(
    #         "scipy.sparse.linalg.dsolve is deprecated and has no attribute "
    #         f"{name}. Try looking in scipy.sparse.linalg instead.")

    # if name in dsolve_modules:
    #     msg = (f'The module `scipy.sparse.linalg.dsolve.{name}` is '
    #            'deprecated. All public names must be imported directly from '
    #            'the `scipy.sparse.linalg` namespace.')
    # else:
    #     msg = (f"Please use `{name}` from the `scipy.sparse.linalg` namespace,"
    #            " the `scipy.sparse.linalg.eigen` namespace is deprecated.")

    # warnings.warn(msg, category=DeprecationWarning, stacklevel=2)

    # return getattr(_dsolve, name)
    return _sub_module_deprecation(sub_package="sparse.linalg", module="dsolve",
                                private_modules=["_dsolve"], all=__all__,
                                attribute=name)
