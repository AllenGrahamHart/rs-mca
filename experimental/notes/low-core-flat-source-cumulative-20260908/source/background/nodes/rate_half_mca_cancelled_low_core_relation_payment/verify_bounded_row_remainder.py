"""Exact finite margin certificate; no deployed-domain enumeration."""

import importlib.util
from fractions import Fraction
from math import comb
from pathlib import Path


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify():
    parent = load("cancelled_payment", Path(__file__).with_name("verify.py"))
    parent.verify()
    # Independent binomial expression for both falling-product endpoints.
    values = []
    for j in (4801, 254999):
        value = Fraction(132*comb(1048576+j, 12),
                         (67472+j)*comb(67482, 10))
        assert value == parent.resource(j)
        values.append(parent.ceil(value))
    assert values == [13195104981505077258, 38153096234616609717]
    resource = max(values)
    budget = 2130706433**6 // 2**128
    assert budget == 274980728111395087
    total = resource//139 + 134944
    assert total == 274482706723995445 < budget
    assert budget-total == 498021387399642
    assert resource//138 + 134944 > budget
    assert (500-139+1) == 362
    assert resource//500 + 134944 == 76306192469368163 < budget
    print("PASS: margin 139 payment", total, "reserve", budget-total)
    print("PASS: margin 138 uniform recipe rejected; 362 new remainder degrees")


if __name__ == "__main__":
    verify()
