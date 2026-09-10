# Pay A Weaker Low-Pair Rank Premise With The Stronger Original Resource

Set R=1048576,d=67472,E=21499,W9=578501226347492453.
The new unconditional resource gives sum min(raw,9)<=W9, hence also
sum min(raw,3)<=W9, over every original label. Near134944 is separate.
If P2 is empty, every raw>=3, so floor(W9/3)+near pays the source.

The [pencil-section proof](nonconstant_sections.md) pays whole sources
with large complete P43 core unions by at most261996525491320703.
It uses the OLD resource in that alternative only. We henceforth work in
the complement of those paid source classes, on the unchanged original
source, using the unrefunded NEW W9 resource. The two resources are not added.

## 1. Hereditary Sections And Both Terminal Types

Every affine pencil section of dimension v now has actual P2 count at
most C^v for a constant direction or P^v for either direction, with

    C=481076/67471, P=35/4.

For A=m-2, the hereditary joint-incidence determinant factor satisfies

    H(J)=(n-2J+2)/(A-2J+2)=(R-J+2)/(d-J)
         <=H(E)=1027079/45973<=P^2.

The denominator stays positive and H increases with J since R+2>d.
The pencil-section theorem therefore bounds each function-field-rank-two
affine v-space by H(E)*P^(v-2). Its lower-dimensional children may be
pencils; they need not remain rank two.

## 2. Five Guarded Anchors

Assume P2 is nonempty and its actual affine rank is at most16. Enlarge
only this auxiliary direction space inside V x V to dimension16, keeping
an actual pair as offset. The counted subset need not span the enclosure.
Apply shared-carrier anchors at pair/shared dimensions

    16/11,14/10,12/9,10/8,8/7 ->6/6.

At each stage s<r<=2s; at most J+s-r coordinates have joint-evaluation
rank<2, INCLUDING prior anchors which are common carrier zeros. Every
good section has dimensions r-2,s-1, with the original degree and
agreement threshold unchanged. With c=r-s, its factor is

    (n-J-s+r)/(A-J-s+r)=(R+c)/(d-2+c), c=5,4,3,2,1.

All agreement denominators are positive. Empty sections contribute zero.
At the equality terminal6/6, a function-field-rank-one direction must
be constant by full-carrier rigidity, costing C^6. Rank two costs
H(E)*P^4. Exact arithmetic proves C^6>H(E)*P^4, so the pair count is

    |P2|<=M=C^6*prod_(c=1)^5 (R+c)/(d-2+c),
    floor M=119106357701.

This retains BOTH terminal possibilities before choosing their maximum.

## 3. Return To Original Slopes Once

For one actual pair f, the selected defect sets of different assigned
labels are disjoint outside its complete joint core H_f. Since
|H_f|>=m-2, its total low raw is at most n-|H_f|<=R-d+2=981106.
Hence sum_(raw<=2) raw<=981106*M.

The exact truncated identity gives

    |Gamma|=(1/3)*sum min(raw,3)
                   +sum_(raw<=2)(1-raw/3)
             <=W9/3+(2/3)*981106*M.

Floor only this FINAL rational expression and add near134944 once:

    |Z_bad|<=270737716902276994.

This exceeds the alternative large-pencil caps, so it is also their
maximum. The reserve below B* is4243011209118093. Higher raw labels
were never dropped, and no original coordinates were cancelled afresh.

Contraposition forces actual P2 affine rank>=17 for every assignment on
an over-budget source. It gives no additional generic-projection claim
for P2 and closes no entire J value or original higher-rank source.
