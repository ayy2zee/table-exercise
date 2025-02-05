import pandas as pd
import numpy as np

# Define the size of the array (rows and columns)
rows = 5
cols = 4

# Generate random numbers between 1 and 100
random_data = np.random.randint(1, 101, size=(rows, cols))

# Define row and column headers
row_headers = [f'Fluor {i+1}' for i in range(rows)]
col_headers = [f'Fluor {i+1} MFI' for i in range(cols)]

# Create a pandas DataFrame
df = pd.DataFrame(random_data, index=row_headers, columns=col_headers)

# Display the DataFrame
print(df)

# Iterate over rows and extract the value where the row and column fluorochromes match
for row in df.index:
    column = f"{row} MFI"  # Construct the column name dynamically
    value = df.loc[row, column]  # Use square brackets for .loc
    print(f"{row} MFI is {value}")