# Proof: Preserve Projection, Empty Core And Tuple Consumption

## 1. Projected Pair Separation

The polynomial annihilator W of F has dimension s-j. Restriction V -> F^A
has kernel W because A spans F. Thus two different pair restrictions
differ in at least one nonzero linear functional on F. Its zeros among
A lie in a hyperplane and number at most a-Delta. If both pairs agree
with the received pair at a point, their restrictions agree there. Hence
their complete joint cores inside A intersect in at most a-Delta points.

Two sets of size >a-Delta/2 would intersect in more than a-Delta, so
there is at most one heavy projected pair. Equality is insufficient.
For a maximum-density flat, every rank-(j-1) subspace has at most
(j-1)*a/j coordinates; this proves Delta=a/j. No assumption about
independence of individual points inside the flat is added.

If the heavy core C has size t, any other core has at most a-Delta
points in C and at most a-t outside C. Its size is therefore at most
b(t)=2a-Delta-t. For t>=a-Delta/2 this is <=a-Delta/2. These are
intersection bounds for actual receiver agreement sets, not disjoint colors.

## 2. Transport The Entire Heavy Group

Choose any pair (A_0,B_0) in (h_*+V) x V representing its restriction
on A. For every label in the group,

    h_gamma-A_0-gamma*B_0 in W.

All W-polynomials vanish on ALL A. The common-root-space bound gives
a<=K-(s-j), and division by the complete locator P_A has actual
dimension s-j and degree <K-a. Gauge the words by (A_0,B_0).
On C both words vanish. At each x in A minus C, the gauged scalar
agreement equation has at most one finite solution gamma. Charge the
union of those exceptional labels in this group, at most a-t.

Each remaining COMPLETE scalar agreement set meets A exactly in C.
Outside A, divide both gauged words and the explanations by P_A. A
degree-<K-a pair explaining a complete child agreement set would lift
by P_A and (A_0,B_0) to explain the entire original complete agreement
set, including C. This contradicts its full-code-bad selected subset.
As in the required complete-core transport, one-point exchanges give an
exact bad subset of size m-t. Overlaps have size m-t-1>=K-a, so
polynomial uniqueness applies. All retained original slopes survive.

Empty universal core is also preserved. Outside A, evaluation on W
vanishes exactly where evaluation on V is zero: the other possibility
would be a nonzero V-evaluation in F, which belongs to A by completeness.
At a V-zero, A_0=h_* and B_0=0. The original empty universal core
excludes u=A_0 and v=B_0 there. Nonzero locator division cannot change
that fact. These nonuniversal zero coordinates stay in the child domain.

## 3. Use The Existing Scalar Ledger At The Actual Agreement

The child has degree K-a, length n-a, agreement mu=m-t and empty
universal core, with explanations in the fixed carrier W/P_A. Apply the
required scalar-agreement descent to each support coordinate. Its anchored
families have dimension at most s-j-1 and gap d+a-t>=d. They are bad
in their FULL child codes, with the same original finite labels.

Any cap at the baseline gap d applies by taking exact bad subsets. If
none existed, uniqueness on overlapping subsets would glue a pair on the
larger agreement set. The degree-zero case uses uniqueness of the zero
polynomial and is included in the scalar supplier's base statement.

Writing z for the child's carrier zeros and tau for those allowing one
exceptional scalar label, that proved ledger gives

    mu*|Gamma_child| <= (n-a-z)*U+tau <= (n-a)*U,

since tau<=z and U>=1. Adding only the a-t removed labels proves CHILD.
There is no child near removal, smaller field or quotient-slope count.

## 4. One Resource Also Charges The Heavy Group

An independent incidence tuple determines the full affine parameter,
including its finite slope. The selected records have pairwise disjoint
tuple sets. If H labels are heavy and L labels are light, then

    T_up >= beta(b)*L + eta*beta_max*H
         >= beta(b)*(L+eta*H).

Therefore H+L<=T_up/beta(b)+(1-eta)*H. Insert CHILD, whose coefficient
is nonnegative, to prove SHARED. This is stronger than giving the entire
tuple budget to LIGHT and then adding the entire heavy child cap for free.
The unchanged earlier additive bound was valid but less efficient.

With no heavy label, occupancy is bounded by a-Delta/2. The relaxed
heavy formula at that endpoint dominates the light-only bound because
CHILD is nonnegative. Thus it may be included in a uniform supremum.
The finite proof owns any convexity or endpoint reduction of that supremum.

No receiver-class independence, favorable complete selection or field
realizability of relaxed endpoint parameters is assumed in this proof.
