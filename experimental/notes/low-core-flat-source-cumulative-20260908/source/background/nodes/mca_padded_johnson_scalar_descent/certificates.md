# Seven exact Johnson certificates

Here R=1048576, d=67472. For a row indexed by L, put
N=R+L, M=d+L, D=L-1 and sigma=2t+1. The required theorem has
the exact gate

```text
4*t^2*M^2 >= sigma^2*N*D.
```

Use the following integer upper quantities:

```text
X=ceil(sqrt(sigma^2*N*D/4)),
Y=ceil(sqrt(sigma^2*N/(4D))),
Z=max(Y,ceil(sigma^2*N/(12D))),
J=2*X*Y^2*Z+(N-M+1)*Y+Z.
```

All operations are integer ceilings or exact integer products. X is
the theorem's lifting length; Y and Z only round its real upper
quantities upward. Each row is a full-source bound at that ONE degree L.
Padding, not unproved monotonicity of optimized Johnson expressions,
extends it to every K<=L.

| s | L | t | X | Y | Z | J |
| --- | --- | --- | --- | --- | --- | --- |
| 5 | 2000 | 1 | 68741 | 35 | 395 | 66558441820 |
| 6 | 3500 | 3 | 212356 | 61 | 1228 | 1940733764889 |
| 7 | 4100 | 6 | 426973 | 105 | 3617 | 34053270588692 |
| 8 | 4500 | 11 | 791564 | 176 | 10319 | 506033334328831 |
| 9 | 4700 | 20 | 1442208 | 307 | 31400 | 8536194661768235 |
| 10 | 4800 | 31 | 2239638 | 467 | 72600 | 70921548248995035 |
| 11 | 4850 | 42 | 3037506 | 627 | 130801 | 312387240623954584 |

The scalar endpoint E_s=floor((R+L+1)*V_(s-1)/(d+L+1)) and
the final cap including every zero-removal exception are:

| s | E_s | R-L | V_s |
| --- | --- | --- | --- |
| 5 | 231037282833 | 1046576 | 231038329409 |
| 6 | 3424825109402 | 1045076 | 3424826154478 |
| 7 | 50371449035494 | 1044476 | 50371450079970 |
| 8 | 737012706652002 | 1044076 | 737012707696078 |
| 9 | 10755802498496694 | 1043876 | 10755802499540570 |
| 10 | 156765527507624520 | 1043776 | 156765527508668296 |
| 11 | 2283382040939589301 | 1043726 | 2283382040940633027 |

Each E_s exceeds J and V_(s-1). No optimality of these convenient
cutoffs is claimed. No search output is a premise of the proof.

## Existing consumers

On the original KoalaBear row, the rank-eleven error gauge followed by
V_10 and the original near add-back gives

```text
V_10+134944 =156765527508803240,
B-(V_10+134944)=118215200602591847.
```

For the existing rank-twelve two-anchor theorem use V_9 and K-g>=255000.
At that endpoint, s=11, its two exact factors are

```text
F_bal   =383277578467/15718615477,
F_spike =11153988094749115/438581833089399 > F_bal.
floor(V_9*F_spike)=273540953997732057.
```

The conservative original zero-exception allowance R and near add-back
2d give 273540953998915577, with slack 1439774112479510 below B.
Thus the existing small-common-core branch extends from g<=623576 to
g<=793576. Its large-common-core branch remains g>=1043776.
The remaining rank-twelve residual is 4801<=K-g<=254999.

The single L=4800 Johnson certificate above, together with padding,
also replaces the old 4799-row scan proving the existing large-core
cap 10^17. Its theorem and original core cancellation are unchanged.
