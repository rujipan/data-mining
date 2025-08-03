import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# --- ข้อมูลการใช้งานแอปของผู้ใช้แต่ละคน ---
app_usage = [
    ['YouTube', 'Facebook', 'LINE'],              # user 1
    ['YouTube', 'LINE'],                          # user 2
    ['YouTube', 'LINE', 'Shopee'],                # user 3
    ['Facebook', 'Shopee'],                       # user 4
    ['YouTube', 'Facebook', 'LINE', 'Shopee'],    # user 5
    ['LINE', 'TikTok'],                           # user 6
    ['YouTube', 'TikTok', 'Shopee'],              # user 7
    ['Facebook', 'LINE'],                         # user 8
    ['YouTube', 'LINE', 'Shopee', 'TikTok'],      # user 9
    ['Facebook', 'TikTok']                        # user 10
]

# --- แปลงรายการให้เป็น one-hot encoding ---
te = TransactionEncoder()
te_array = te.fit(app_usage).transform(app_usage)
df = pd.DataFrame(te_array, columns=te.columns_)

# --- สร้าง Frequent Itemsets ---
frequent_itemsets = apriori(df, min_support=0.3, use_colnames=True)

# --- สร้างกฎความสัมพันธ์ ---
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

# --- แสดงผลลัพธ์ ---
print("📊 Frequent App Itemsets:")
print(frequent_itemsets.sort_values(by="support", ascending=False))

print("\n📈 Association Rules:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].sort_values(by="confidence", ascending=False))
