# Couple Original Raw Mass Across The Actual Terminal Fibres

Put S=R+1,E=21499. For t=1,2, keep each actual pair's weight omega_t
equal to the SUM of the original raw values of its assigned labels with
raw<=t. Write M_t for the total of these weights. They are not pair
counts or counts of auxiliary anchor histories.

For every positive integer raw,

    1=min(raw,3)/3 + (raw*1_(raw<=1))/2
                         + (raw*1_(raw<=2))/6.                (ID)

The required minimum-envelope resource gives, on each J box with lower
endpoint j0, sum min(raw,3)<=sum min(raw,9)<=W(j0), where
W(j0)=floor((R+j0)_12/beta_9(j0)). The resource quotient is decreasing.
Hence original bad slopes are bounded by

    floor(W(j0)/3 + M_1/2 + M_2/6)+134944.                    (SOURCE)

No larger-raw record is deleted by using this identity.

## Eliminate Whole-Source Large-Pencil Alternatives

The [pencil gate proof](pencil_gates.md) pays every source possessing a
large complete P43 pencil-core union, by at most270000000000000000.
The old constant-direction alternative costs261996525491320703.
Hereafter suppose no such pencil exists. Both original resources remain
unrefunded; the alternative whole-source totals are maximized, not added.

If P2 is empty, (SOURCE) has M_1=M_2=0 and already pays. Otherwise,
for rank<=17 enlarge its direction enclosure to17 inside V x V, with an
actual pair as offset. For rank<=18 on the upper interval one may similarly
use an18-dimensional enclosure. Only ACTUAL pairs and labels are counted.

## Exhaustive Terminal Geometry And Payment

The [weighted recursion](source_recursion.md) bounds M_1 and M_2 after
five anchors at rank17 or SIX at rank18. Each populated terminal lies in
a shared carrier of dimension6 or5 and has direction dimension7 or6.
The Pluecker theorem gives exactly the sparse or compression alternatives.
All rank-two descendants are retained in the sparse bound. The
[compression proof](compression_boxes.md) uses one shifted-core mass
budget and charges its common preferred finite slope only once.

The exact source certificate covers all58 consecutive J boxes of width200.
Using the worst allowed terminal cap for each cutoff gives these maxima,
before maximization with the separate large-pencil source alternatives:

    full17:       238873511194752109;
    sparse18:     274462040894062110;
    sparse or actual-fibre-span<=4 compression18:
                  274462040894062110;
    unrestricted full18:311022340713143637 (NOT PAID on all J).

On J14165..21499 the full18 maximum is273715780528023745. These
numbers and their reserves give the statement after taking whole-source
MAXIMA. The tail endpoint14165 is certified, not claimed optimal.

For (SP4), P1 is a subfamily of the same P2 terminals/fibres, so its actual
scalar span also has dimension<=4 wherever that condition is used.
Contraposition yields the declared rank bounds and full-span5 compression
obstruction. It does not imply that all surviving hull points are actual
explanations, nor that P2 has generically full projection.
