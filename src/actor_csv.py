import pandas as pd

class CSVActor:
    def __init__(self, csv_path="data/prices.csv"):
        self.df = pd.read_csv(csv_path)
        print(f"[CSVActor] Loaded {len(self.df)} rows from {csv_path}")

    def lookup(self, query_item):
        query_item_lower = query_item.lower().strip()
        # Case-insensitive matching
        matched = self.df[self.df['item'].str.lower() == query_item_lower]
        if not matched.empty:
            price = matched['price'].values[0]
            return f"The price of {query_item_lower} is {price}."
        else:
            # Find closest match if exact match fails
            self.df['diff'] = self.df['item'].apply(lambda x: abs(len(x) - len(query_item_lower)))
            closest = self.df.loc[self.df['diff'].idxmin()]['item']
            price = self.df.loc[self.df['diff'].idxmin()]['price']
            return f"The price of {closest} (closest match) is {price}."
