import numpy as np


class CompartmentEqualityConstraint:
    """
    An CompartmentEqualityConstraint adds a penalty to the residual if 2
    compartments of the e matrix differ more than by just a scaling parameter
    in the sum over a given range. It calculates as:
    ``penalty = weight * (parameter * sum(c[range, i]) - c[range, j])``

    """

    def __init__(self, weight, i, j, parameter, erange, crange):
        """Initialize a CompartmentEqualityConstraint

        Parameters
        ----------
        weight : [type]
            Weight factor of the penalty
        i : [type]
            Index of the first compartment
        j : [type]
            Index of the second compartment
        parameter : [type]
            Index of the parameter
        erange : [type]
            The range on the e matrix axis the constraint is applied on
        crange : [type]
            The range on the c matrix axis the constraint is applied on
        """

        self.weight = weight
        self.i = i
        self.j = j
        self.parameter = parameter
        self.erange = erange
        self.crange = crange

    def calculate(self, e_matrix, parameter):
        p = parameter[self.parameter].value
        return self.weight * (p * np.sum(e_matrix[self.i] - e_matrix[self.j]))
