# LOW 101 and HIGH 1200 on the same completed-basis resource

Status: PROVED on this consumer's unchanged canonical normalized source,
4801<=J<=169999. Write LOW_101 for the records whose existing raw
minimum is 1..101. No support or minimizing explanation is reselected.
Let L be the number of their original finite labels. Then

    |Gamma|+134944 <=floor((C+1189*L)/1200)+134944,
    C=23067643444721720934.                            (A101)

Indeed the required completed-basis resource gives total weight <=C.
Each record has weight >=12*67472/67483>11. For raw >=1200 its
truncated weight is >=1200. For 102<=r<=1200, the logarithmic
derivative of the completed weight is >=1/r-11/(67473-r)>0.
Its least allowed agreement parameter is >=67472+11, and Bernoulli's
product inequality gives

    b(102)>=1224*(1-1122/67473)>1200,
    1224*(67473-1122)-1200*67473=246024>0.

Thus 11*L+1200*(|Gamma|-L)<=C, proving (A101). Dropping the LOW
contribution would lose useful reserve. This is a new exact discount
from the same resource, not reuse of a /501 gain under a different base.

A represented LOW_101 pair has at least J+67371 complete joint
agreements. Distinct finite labels have disjoint defects outside its own
core, so there are at most 981205 such labels per pair. A curve with at
most M rich pairs and <=64 off-curve pairs therefore pays

    P(M)=floor((C+1189*981205*(M+64))/1200)+134944.     (P101)

The component supplier's `cutoff101.md` counts all d=7 cubic pairs at
601<=h<=4381 on 8656..8763 by M<=255040048958, so this class
pays P(M)=267175680601112099. The general weighted supplier at
h<=600 gives M<=262988722817 and P(M)=274903465748372176.
No other curve group's labels are silently classified HIGH.

The full-kernel child supplies exhaustive curve coverage at this cutoff,
and owns its new whole-interval theorem. This accounting proof neither
requires that child nor assumes a cover of an arbitrary source. Original
field, complete cores, defects, scalar labels and near are unchanged.
