# Padded Johnson bounds in scalar-agreement descent

Status: PROVED, 2026-09-07. Count distinct ORIGINAL finite bad slopes,
with explanations in an affine polynomial space of the stated dimension.
Badness always means noncontainment of the received pair on the SAME
support, in the full RS code.

## General cutoff theorem

Fix integers R>=d>=1 and 2<=L<R, and a field of size at least 2R.
Rows have (n,K,m)=(R+K,K,d+K), 1<=K<=R, on arbitrary distinct
points. Suppose U>=1 bounds every such selected family with explanation
affine dimension at most s-1. Suppose J bounds the FULL original MCA
numerator on every (R+L,L,d+L) row over this field. Put

```text
A=max(U,J,floor((R+L+1)*U/(d+L+1))).
```

Then every selected family of explanation dimension at most s satisfies

```text
|Z| <= A+max(0,K-L) <= A+R-L.                       (PJ)
```

The field-size hypothesis permits padding any K<=L row to degree L
without changing the ambient field. The proof charges at most one slope
at each nonuniversal common-zero removal. It does not assume that such
removal is lossless, or that children retain a post-near property.

## Uniform KoalaBear constants

For R=1048576, d=67472 and any field of size at least 2097152,
the required scalar and weighted-line bounds, combined with seven fixed
rounded Johnson certificates, give the following uniform caps V_s:

```text
s     V_s
1     4070947
2     63264449
3     983145945
4     15278131113
5     231038329409
6     3424826154478
7     50371450079970
8     737012707696078
9     10755802499540570
10    156765527508668296
11    2283382040940633027
```

These hold simultaneously for every 1<=K<=R and arbitrary received
values, with no common-core or error-rank assumption on the child families.
V_10 pays the original KoalaBear error-rank-eleven branch after its gauge.
V_9 strengthens the existing two-anchor rank-twelve consumer. V_11 is
still over the original budget: no full rank-twelve theorem follows.

See [proof.md](proof.md) and [certificates.md](certificates.md).
