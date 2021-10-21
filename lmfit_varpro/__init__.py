"""Top-level package for lmfit-varpro."""

__author__ = """Jörn Weißenborn, Stefan Schütz, Joris Snellenburg"""
__email__ = "joern.weissenborn@gmail.com, stefanschuetz.fd@gmail.com, j.snellenburg@gmail.com"
__version__ = "0.0.5.post1"

from lmfit_varpro import constraints
from lmfit_varpro import result
from lmfit_varpro import separable_model

SeparableModel = separable_model.SeparableModel
SeparableModelResult = result.SeparableModelResult
CompartmentEqualityConstraint = constraints.CompartmentEqualityConstraint
