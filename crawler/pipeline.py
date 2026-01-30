import pandas as pd
import os
from datetime import datetime

def save_to_csv(data, category):
    if not data:
        print("No data to save.")
        return

    os.makedirs("data/raw", exist_ok=True)

    df = pd.DataFrame(data)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/raw/{category}_{timestamp}.csv"

    df.to_csv(filename, index=False)
    print("Total products collected:", len(data))
    print(f"Saved file: {filename}")