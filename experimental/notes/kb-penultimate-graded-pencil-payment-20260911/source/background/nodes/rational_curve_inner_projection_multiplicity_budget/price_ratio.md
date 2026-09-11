# A Uniform Price For Each Inner-Image Degree

For m>=1, mu>=2, eta>=2 set d=m+mu*eta. It is enough to prove

    (eta-1)*d*(m+mu-1)*(m+mu-2)-m*(d-2)*(d-3)>=0.

Put h=eta-2 and d0=m+2mu. The left side is F0+h*F1+h^2*F2, where

    F0=d0*(mu-1)*(mu-2)+2m*(d0-3),
    F1=m^3+3m^2*(mu-1)+m*(3mu-1)*(mu-2)
       +3mu*(mu-1)*(mu-2),
    F2=mu*(m*(m-1)+(mu-2)*(m+mu-1)).

Every displayed term is nonnegative. Division by the positive denominator
and multiplication by nu proves

    nu*m*G/charge <= (eta-1)*nu*d,
    G=binom(d-2,2), charge=binom(m+mu-1,2).

The factor eta-1 cannot simply be deleted from this pointwise price:
m=1,mu=2,eta=3 gives G*m/charge=10>d=7. The full multiplicity in the
charge is also load-bearing; the unibranch control in controls.md
has m=5,b=1,mu=2 and the branch-only denominator gives105>d=9.
