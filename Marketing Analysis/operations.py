import pandas as pd


p_df = pd.read_csv("dataset/purchase_behaviour.csv")
t_df = pd.read_csv("dataset/transaction_data.csv")


m_df = t_df.merge(p_df, on="LYLTY_CARD_NBR")

