import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# --- Sample Dataset: Transactions ---
dataset = [
    ['milk', 'bread', 'nuts', 'apple'],
    ['milk', 'bread', 'nuts'],
    ['milk', 'bread'],
    ['milk', 'bread', 'apple'],
    ['milk', 'bread', 'apple']
]

# Convert to one-hot encoded DataFrame
from mlxtend.preprocessing import TransactionEncoder
te = TransactionEncoder()
te_data = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_data, columns=te.columns_)

# --- Step 1: Frequent Itemsets ---
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)

# --- Step 2: Generate Association Rules ---
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

# --- Display Results ---
print("Frequent Itemsets:\n", frequent_itemsets)
print("\nAssociation Rules:\n", rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
