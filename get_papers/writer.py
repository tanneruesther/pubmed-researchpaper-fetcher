
import pandas as pd
from typing import List, Dict, Optional, Any

def export_to_csv_with_pandas(
    data: List[Dict[str, Any]], 
    filename: str, 
    columns: Optional[List[str]] = None
) -> None:
    if not data:
        print("⚠️ No data to export.")
        return
    df = pd.DataFrame(data)
    if columns:
        df = df[columns]
    df.to_csv(filename, index=False)
    print(f"✅ CSV saved to {filename}")
