import pandas as pd
import numpy as np

# Define the number of Fluors (rows)
num_fluors = 5  # Change this value to adjust the number of Fluors

# Generate random numbers between 1 and 100
# The shape is (num_fluors, num_fluors * 4) because each Fluor has 4 columns
random_data = np.random.randint(1, 101, size=(num_fluors, num_fluors * 4))

# Define row headers
row_headers = [f'Fluor {i+1}' for i in range(num_fluors)]

# Define column headers
col_headers = []
for i in range(1, num_fluors + 1):
    col_headers.extend([
        f'Fluor {i} Pos MFI',
        f'Fluor {i} Neg MFI',
        f'Fluor {i} Pos rSD',
        f'Fluor {i} Neg rSD'
    ])

# Create a pandas DataFrame
df = pd.DataFrame(random_data, index=row_headers, columns=col_headers)

# Display the DataFrame
print(df)