# A Root Changes The Codimension; A Nonroot Lowers The Degree

Write S=T*u with a nonzero constant pair direction u. Distinct constant
directions have zero intersection. An s-dimensional constant subspace
in another direction cannot coexist with S in W of dimension2s-3.
Thus the absence of a full constant subspace is exactly maximality
of S in its own direction.

At a regular anchor x, shared and pair dimensions become s-1 and2s-5.
If T(x) is nonzero, S_x has dimension s-2 and is the full constant
pencil in that direction inside W_x. No full constant (s-1) subspace
in a different direction can coexist with it, since their dimensions
would sum to2s-3>2s-5. Hence the child remains in the partial class.

Write T=G*T0 with gcd(T0)=1 and max degree(T0)=E. At a nonroot of G,
the scalar kernel (T0)_x consists of polynomials divisible by X-x.
After dividing that factor and the full gcd, its primitive degree is
at most E-1. Dividing any common factor of the shared carrier does not
change this primitive scalar degree.

If G(x)=0, S is retained and its component span T has dimension s-1,
the entire child shared carrier. Hence the child has a FULL constant
subspace and primitive shared degree E. The exceptional coordinate
count is at most deg G<=D-E, including all finite roots conservatively.
Repeated roots and degree slack at infinity cannot increase this count.

For a full constant carrier, choose coordinates with W=(V,0)+(0,B),
dim B=s-3. Regularity forces evaluation on B to be nonzero.
The child is (V_x,0)+(0,B_x), still full constant, with shared dimension
s-1 and primitive shared degree at most D-1.

At s=3, a maximal constant plane with no full constant3 is necessarily
function-field rank2. The existing codimension-one rational-compression
theorem applies with constant height0. The scalar costs and original
owner accounting are justified in degree_prices.md.

These arguments generalize the earlier constant-three child ledger.
They do not assume generic normalization degree is a uniform fibre cap,
and use no curve-genus or characteristic-zero result.
