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
    return _sub_module_deprecation(sub_package="sparse.linalg", module="dsolve",
                                private_modules=["_dsolve"], all=__all__,
                                attribute=name)
