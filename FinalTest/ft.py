import pandas as pd 
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
data['tmp'] = 1
data.set_index([data.index, 'whoAmI'], inplace=True)
#data = data.unstack(fill_value = 0).astype(int)
print(data)
