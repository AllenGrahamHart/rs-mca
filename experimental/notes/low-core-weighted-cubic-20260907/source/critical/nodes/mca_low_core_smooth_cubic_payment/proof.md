# Proof with original-coordinate degree accounting

Base-extend the CONSTANT field to k=algebraic closure of F for the
dimension proof. The original rational slope labels remain over F.

## 1. Dimension and degree

The required elliptic-section theorem bounds every reduced component
of the polynomial-pair locus by dimension one, or zero under the
nonconstant-j/singular-fiber condition. Intersect with the given affine
coefficient spaces; that cannot increase dimension.

In the 2s original pair coordinates, clearing a fixed denominator
from Q(a,b)=0 gives finitely many coefficient equations of degree <=3.
The required homogeneous-level supplier in turn requires the graph
supplier's `algebraic_list_bound.md`. Its section 3 covers a locus of
dimension <=r in affine 2s-space by a reduced pure r-dimensional
variety of degree <=3^(2s-r). Use r=1 or r=0 respectively. This
counts ALL coefficient components, not just a preferred elliptic
section or a chosen divisor class.

Section 4 of that same algebraic LIST lemma gives

    M_t <= Delta*((n-K+1)/(m-t-K+1))^r.

This proves (1) and (2). For r=0 it just counts the points of a
zero-dimensional variety; no LIST ratio or field-size multiplier is
needed. The Weierstrass transformation in the dimension supplier is
not used for coefficient degree or for agreement counting. All
domain coordinates, including denominator and discriminant zeros,
remain in the original joint-agreement count.

## 2. Original LOW label ownership

The homogeneous-level supplier's proof section 4 uses only the
complete-core and assigned-support identities, not its special product
curve. For a fixed pair f with core H_f, the raw mismatches supplied
by distinct finite labels are disjoint outside H_f. For cumulative
raw<=t the total raw per represented pair is at most n-m+t.
Thus the group cumulative raw is at most (n-m+t)*M_t.
Telescoping 1-r/(T+1)=sum_(t=r)^T r/(t*(t+1)) gives (3).

In dimension zero there are at most 3^(2s) possible pairs in total.
Every selected label has at least one mismatch outside its own
complete core, hence a represented LOW pair has at most n-m+T
labels. Each label's gain is <=1. This proves the simpler bound
3^(2s)*(n-m+T), without a cubic-specific ownership assumption.

## 3. Finite group constants

On the normalized parameters, (1) and (3) give

    G <= 3^21 * sum_(t=1)^500
         (981104+t)*1048577/((67473-t)*t*(t+1)).        (4)

The exact ceiling of (4) is 159185671413625180. Under the
zero-dimensional condition, the simpler bound gives

    G <= 3^22*981604 = 30803773636432836 < 3W.         (5)

The two verifiers compute (4) independently, using rational addition
and an integer common denominator, and check (5). These constants
are independent of J; applying an inherited resource bound on a
J interval remains the finite consumer's responsibility. No reverse
dependency or source-coverage conjecture is introduced here.
