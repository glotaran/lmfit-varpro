"""Top-level package for lmfit-varpro."""

__author__ = """Jörn Weißenborn, Stefan Schütz, Joris Snellenburg"""
__email__ = (
    "joern.weissenborn@gmail.com, stefanschuetz.fd@gmail.com, j.snellenburg@gmail.com"
)
__version__ = "0.0.5-archive"

from lmfit_varpro import constraints, result, separable_model

SeparableModel = separable_model.SeparableModel
SeparableModelResult = result.SeparableModelResult
CompartmentEqualityConstraint = constraints.CompartmentEqualityConstraint
