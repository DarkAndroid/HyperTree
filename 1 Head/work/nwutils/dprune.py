#! /usr/bin/env python
# -*- coding: utf-8 -*-

import dendropy

# tree0 = dendropy.Tree.get(
#         path="test.ordN",
#         schema="newick")

tree = dendropy.Tree.get(
        path="test.ordN",
        schema="newick")

# node_filter_fn = lambda nd: nd.taxon is None or nd.taxon.label.startswith("36496")
# tree1 = tree0.extract_tree(node_filter_fn=node_filter_fn)


# tree.prune_taxa_with_labels(["AF BW 0013", "AF BW 0133"])

tree1 = tree.extract_tree_with_taxa_labels(["AF BW 0013", "AF BW 0133"])

# tree1 = tree.extract_tree_with_taxa(["36494"])

# print(tree.as_string("newick"))
# print(tree.as_ascii_plot())
print(tree.as_string("newick"))
print(tree.as_ascii_plot())
print(tree1.as_string("newick"))
print(tree1.as_ascii_plot())