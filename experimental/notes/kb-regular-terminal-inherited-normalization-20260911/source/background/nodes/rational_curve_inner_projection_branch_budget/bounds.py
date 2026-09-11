"""Exact branch-weighted high-degree inner-centre bounds."""
from math import comb


def coordinate_bound(d,r,nu,h):
    if r<3 or d<r or nu<1 or h<2:
        raise ValueError("geometric degree parameters")
    maximum_branch = d-h*(r-1)
    if maximum_branch<1:
        return 0
    branch = min(maximum_branch,max(1,h-2))
    genus = comb(d-r+1,2)
    charge = comb(branch+h-1,2)
    return nu*(genus*branch//charge)
