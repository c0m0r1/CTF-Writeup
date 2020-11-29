## Spark
linux kernel module exploit from hitcon 2020

## Vulnerability
kernel UAF of release node
 - in release(`spark_node_free`->`spark_node_put`), node & links starting from it freed but links pointing to it doesn't.  
we can trigger UAF(crash) by simple pseudocode below.
```
open(0), open(1)
link (0, 1) -> make link 0->1 & 1->0
close (0) -> free node 0 and link 0->1
finalize (1) -> traverse(1, ...) calls traverse(0, ...) by link 1->0 and crash by UAF from node 0 
```

## Exploit
TODO
- spawn process for UAF crash
- leak kernel heap & stack by reading kernel buffer
- retain UAF node with setxattr
- query to heap-relative arb. write
- overwrite kernel stack and ret2user.

flag:`hitcon{easy_graph_theory_easy_kernel_exploitation}`