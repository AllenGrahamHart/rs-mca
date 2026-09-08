# Hand audit

Same-agent hand audit, 2026-09-06. Independent review remains due.

1. R_i f_i has degree <=a-1; the strict remainder cutoff matches it.
   At least a distinct common roots force the exact polynomial identity.
2. Relations concern the full threshold list, not an exact-size support.
3. Rationally independent rows force equality of any two polynomial
   solutions even if their determinant has roots in D.
4. A nonprimitive row cannot be divided in the received identity at
   its domain roots. J retains exactly the incompatible points.
5. G not dividing T_R, or absence of a bounded polynomial solution,
   makes the list empty. No candidate anchor is silently assumed.
6. Coprimality after division ensures that the direction vector never
   vanishes simultaneously in both components, so w is unique.
7. The homogeneous kernel is (A_1 H,-A_0 H), with degree <k-d.
   Zero entries, d=0, d>=k and the zero polynomial are covered.
8. Every member of the reduced scalar list gives an actual joint
   pair. J contains forced errors; threshold a is unchanged.
9. Full-domain extension is an upper comparison only. The diagonal
   source supplies the separate reverse inequality for the maxima.
10. Row invariance uses degree <=a-1<n, so reducing modulo P_D
    does not introduce a high coefficient after adding a codeword.
11. The linear-map domain has 2(a-k+1) coefficients; its codomain
    has n-a coefficients. Strict dimension surplus gives a kernel.
12. Relation-free error normalization uses the gcd of the canonical
    polynomial errors, not an arbitrary a-subset locator. Its degree
    is at least the actual number of common agreement coordinates.
13. (W,0), (W,XW), and the three-point nonprimitive example are
    checked symbolically in proof.md. No numerical check is a premise.

14. For a merged projection fiber, the full agreement intersection
    has size <=k-1, because two actual tuples differ in a polynomial
    component. The union threshold is 2a-k+1, not 2a-k.
15. Every nonsingleton fiber contributes a distinct scalar polynomial
    at that stronger threshold; its many pair witnesses are not counted.
16. A second independent projection is injective within each first
    fiber. It bounds fiber size, not the number of arbitrary supports.
17. Counting one member per fiber yields J+(L_w(a)-1)H, so the
    subtraction of one is required. Empty projected lists are separated.
18. Uniform maxima M(a)>=1 and M(b)>=0 justify the monotone
    substitutions. b>n gives no nonsingleton fiber. The final budget
    comparison is inclusive, and its input upper bounds remain open.

No scripts, CAS, tests, graph compiler or numerical jobs ran. No general
LIST or MCA prize upper bound follows from this audit.
