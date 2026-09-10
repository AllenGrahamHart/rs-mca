# Whole-Source Gates And Hereditary Weighted Pencil Bounds

Set R=1048576,d=67472,E=21499,S=R+1. For every full primitive
polynomial pencil take the union of COMPLETE cores of ALL its actual
P43 pairs. Its complement is e. The inherited constant gate e<=567500
pays the whole source by261996525491320703.

For nonconstant height h, retain the inherited ON/OFF argument, but insert
the improved all-original W44=581590844909990298. Its whole-source base is

    BASE=W44/44+R+E+134944
            +(43/44)*S^11*10^10/[11^11*(d-42)^10].

Every OFF pair costs at most(43/44)*981147 from its OWN complete core.
The on-pencil union complement is not a valid off-pair charge. In a band
ell<=h<=u and e<=g, complement padding gives auxiliary LIST parameters

    (r,w,Kmax,dimension)=(g-E,d-42-u-E,E,11).

The gate certificate covers108 consecutive height bands of width200,
through21498. Its recorded integer g in every band has a legal11-step
LIST cap L and exact price ceil(BASE+(43/44)*981147*L)<=270000000000000000.
There is no claim that these selected gates are largest possible. The
search that generated them is not a proof input; chosen-step legality is.

Suppose all large-pencil alternatives are absent. For any actual P_t
pencil subfamily with t=1 or2, its own core union is a subset of the full
P43 union, hence its complement is at least567501 if constant, or g+1
in the corresponding nonconstant band. It is also at most R-d+t.

Let C_(t,v),P_(t,v) denote RAW-WEIGHT caps for a dimension-v pencil
section, not scalar pair counts. The weighted-pencil supplier gives

    constant: t+e*((S-e)/(d+1-t))^v,
    nonconstant: t*(n-e)+e*((S+h-e)/(d+1-t+h))^v.

For v1..5 the constant expression is maximized at e=567501, since
S/(v+1)<=567501. Thus C=t+567501*(481076/(d+1-t))^v.

For a nonconstant band, put e_min=g+1. For fixed e<=R-d+t the scalar
ratio decreases with h, so replacing h by ell only increases it.
The function e*(S+ell-e)^v increases to (S+ell)/(v+1), then decreases.
The exact rational e*=max(e_min,(S+ell)/(v+1)) lies in the permitted
interval, as checked for every t,v,band. Therefore a valid band cap is

    t*(R+E-e_min)+e* *((S+ell-e*)/(d+1-t+ell))^v.

P_(t,v) is the maximum over all108 bands. These bounds persist through
every affine section and anchor division: original complete cores, raw
weights and finite labels are unchanged; only auxiliary pair differences
are divided. Extra bands with h>=J are harmless overestimates. The
zero-dimensional cap is separately R-d+t, requiring no pencil direction.
