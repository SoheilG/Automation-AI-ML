import pandas as pd

data = {
    'Model': ['Phone A', 'Phone B', 'Phone C', 'Phone D', 'Phone E'],
    'Price': [200, 800, 550, 900, 150],
    'In_Stock': [True, True, False, True, True]
}

df = pd.DataFrame(data)

premium_ready = df(df[df['Price']>500] & df[df['In_Stock'] = True])
print(premium_ready)