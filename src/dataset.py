import pandas as pd

data = {
    "Name": ["Lucas", "Anna", "Peter", "Linda"],
    "Location": ["New York", "Paris", "Berlin", "London"],
    "Age": [24, 13, 53, 33],
}

df = pd.DataFrame(data)

df.head(5)
