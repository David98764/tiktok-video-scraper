thonimport json
import csv
import os

def export_data(data):
    """Export scraped data to multiple formats."""
    os.makedirs("output", exist_ok=True)

    # Export to JSON
    with open("output/data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

    # Export to CSV
    with open("output/data.csv", "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    # Export to Excel (using a third-party library like openpyxl or pandas)
    try:
        import pandas as pd
        df = pd.DataFrame(data)
        df.to_excel("output/data.xlsx", index=False)
    except ImportError:
        print("Pandas is not installed, skipping Excel export.")