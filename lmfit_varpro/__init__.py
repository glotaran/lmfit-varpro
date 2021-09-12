"""Top-level package for lmfit-varpro."""

__author__ = """Joris Snellenburg, Stefan Schuetz, Joern Weissenborn"""
__email__ = 'j.snellenburg@gmail.com, YamiNoKeshin@gmail.com, joern.weissenborn@gmail.com'
__version__ = '0.0.5'

from lmfit_varpro import constraints, result, separable_model

SeparableModel = separable_model.SeparableModel

SeparableModelResult = result.SeparableModelResult


CompartmentEqualityConstraint = constraints.CompartmentEqualityConstraint
