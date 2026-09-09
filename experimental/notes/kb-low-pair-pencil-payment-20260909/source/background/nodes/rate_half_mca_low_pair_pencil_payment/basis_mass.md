# A Core-Sixteen Record Cost Funds Every Raw Value

Put d=67472,D=d-16=67456,E=21499,X=5000 and
P_r=product_(i=1)^(r-1)(D+i). The required raw-mass supplier credits the
universal polynomial-basis contraction theorem. As in its earlier finite
applications, use fixed quadratic lower certificates q_r(K)=a_r+b_r*K+c*K^2.

Set c=1/[2(D+2)], a_3=D(2D+1)c, b_3=(3D+1)c. For r=4,...,11,
with a,b the preceding coefficients, define

    H=D+r-1, alpha=(r-2)/(r-1), delta=1/(r-1),
    f=a+b*(r-1)+c*(r-1)^2,
    s1=b-2c+f/H, s0=a-b+c-(r-1)f/H,
    u3=c*alpha^2/H,
    u2=(b*alpha+2c*alpha*delta+D*c*alpha^2)/H,
    u1=(a+b*delta+c*delta^2+D*(b*alpha+2c*alpha*delta))/H,
    u0=D*(a+b*delta+c*delta^2)/H,
    t1=u1+2(u2-c)X+3u3*X^2,
    t0=u0-(u2-c)X^2-2u3*X^3,
    eta=max(0,t0+t1*r-s0-s1*r,t0+t1*E-s0-s1*E),
    a_r=t0-eta, b_r=t1.                                (REC)

All eight exact steps have b>=D*c, u2>=c, u3>=0 and positive next
coefficients with b_r>=D*c. The spike branch s0+s1*K+c*K^2 dominates
q_r at r and E, hence throughout that interval. The other branch obeys

    (D+K)q_(r-1)(alpha*K+delta)/H - q_r(K)
      =eta+(K-X)^2*((u2-c)+u3*(K+2X))>=0.               (SQ)

The required contraction theorem therefore proves at least P_r*q_r(K)
ordered bases for every nonzero rank-r evaluation family of degree<K on
D+K coordinates, r<=K<=E. This is a universal theorem with eight fixed
rational certificates, not a scan over sources. The independent audit
reconstructs (SQ) by polynomial convolution.

Write q=q_11,P=P_11,P_d=product_(i=1)^10(d+i) and beta(J)=12*P*q(J).
For raw<=16, any minimizing joint core has a nonzero rank-eleven subset
of m-16=D+J points. The raw-mass insertion proof gives raw*beta(J)
independent tuples per record.

For raw>=17, the completed-basis supplier gives at least

    11*min(raw,500)*m*P_d >=187*m*P_d

independent tuples on the SAME resource. Its all-raw inequality includes
raw>500 and raw>d. The exact gate is

    187*(d+J)*P_d >=3*beta(J).                          (HIGH)

Since d*b>=a, q(J)/(d+J) increases; checking (HIGH) at E proves it
throughout the actual interval. Thus EVERY record owns at least
beta(J)*min(raw,3) independent tuples. The coarser baseline17*m*P_d
is not substituted for187*m*P_d.

Put L=9965 and n_L=1048576+L. The exact derivative certificate is

    (b+2cL)*(n_L-11)>12*q(E).

It implies that

    R(J)=(1048576+J)_falling_12 / beta(J)

decreases on the entire real interval[L,E]. Let R0=R(L), kept as its
EXACT rational value throughout the coupled proof. Its floor is

    floor R0=613022127444579907.                        (R0)

The floor alone must not be multiplied by a fractional refund. The
certificate and both verifiers retain the numerator and denominator of R0.
