**Association rule mining** is a machine learning technique used to discover interesting relationships between variables in large datasets. It's often used in market basket analysis to find products that are frequently bought together. The core idea is to identify strong rules in the form of "if X, then Y," where X and Y are sets of items.

**Key Concepts**
**Itemset: **A collection of one or more items.

**Support:** This metric measures how frequently an itemset appears in the dataset. A high support value indicates that the items in the set are bought together often. It's calculated as the fraction of transactions containing the itemset.

**Confidence:** This metric indicates how likely it is that item Y is purchased when item X has already been purchased. It's calculated by dividing the support of the combined itemset (X and Y) by the support of the antecedent (X).

**Lift:** This metric evaluates the strength of a rule by comparing the confidence of the rule to the expected confidence. A lift value greater than 1 suggests a positive association between the items, while a value less than 1 indicates a negative association.

The goal is to find rules that meet a user-specified minimum support and confidence threshold. The most common algorithm for this task is the **Apriori algorithm**.
