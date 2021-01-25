import pandas as pd
housing=pd.read_csv(r"C:\Users\shilpi\Downloads\realestatepricepredictor\data.csv")
housing.head()
housing.info()
housing['CHAS']
housing['CHAS'].value_counts()
housing['NOX']
housing['NOX'].value_counts()
housing.describe()

import  numpy as np
def split_train_test(data, test_ratio):
    np.random.seed(42)
    shuffled=np.random.permutation(len(data))
    print(shuffled)
    test_set_size=int(len(data)* test_ratio)
    test_indices=shuffled[:test_set_size]
    train_indices=shuffled[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]



train_set, test_set=split_train_test(housing, 0.2)

print(f"Rows in train set:{len(train_set)}\n Rows in test_set:{len(test_set)}")

from sklearn.model_selection import StratifiedShuffleSplit
split=StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing['CHAS']):
    strat_train_set=housing.loc[train_index]
    strat_test_set=housing.loc[test_index]


strat_test_set

strat_test_set.describe()
strat_test_set.info()




strat_test_set['CHAS'].value_counts()

strat_train_set['CHAS'].value_counts()
