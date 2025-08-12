import pandas as pd
import random
from datetime import datetime, timedelta

# Generate 50 dates starting from 03.03.19
start_date = datetime.strptime("03.03.19", "%d.%m.%y")
dates = [start_date + timedelta(days=i) for i in range(50)]

# Generate 50 random temperatures in Fahrenheit
temperatures = [round(random.uniform(40.0, 85.0), 1) for _ in range(50)]

# Create the DataFrame
df = pd.DataFrame({
    "Date": [date.strftime("%d.%m.%y") for date in dates],
    "Temperature": temperatures
})

# Save to CSV with index, but no header row at all
df.to_csv("temperature.csv", index=True, header=False)
