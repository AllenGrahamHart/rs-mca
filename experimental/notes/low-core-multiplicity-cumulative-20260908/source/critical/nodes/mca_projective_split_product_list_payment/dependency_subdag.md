# Dependency sub-DAG

    mca_low_core_quadratic_graph_payment [PROVED]
        -> mca_low_core_homogeneous_level_payment [PROVED]
        -> mca_projective_split_product_list_payment [PROVED]
        -> rate_half_mca_cancelled_low_core_relation_payment [PROVED]
        -> rate_half_mca_low_core_kernel_quadratic_strip [PROVED]

Arrows above are requirements, owned by their consumers. The first
supplier proves proper-section degree bounds; the next supplies the
fixed-divisor argument. This node proves the projective fiber degree
and all four affine-scaling/list cases. The finite consumer owns HIGH,
LOW and original near accounting using its existing proved resource
suppliers. There is no reverse dependence on the finite consumer.

The full-kernel node and finite consumer retain evidence-only links to
the global rank/support router, which remains TARGET without req edges.
No arbitrary-source product assertion or new conditional child is added.
