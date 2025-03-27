import os
from dotenv import load_dotenv
from dune_client.client import DuneClient
import pandas as pd

# Load environment variables
load_dotenv()

# API Key & Query ID
API_KEY = os.getenv('DUNE_API_KEY')
QUERY_ID = 4907172

# Redirect to output folder
output_dir = "csvfileselection"
os.makedirs(output_dir, exist_ok=True)

# Initialize Dune client and fetch result
dune = DuneClient(API_KEY)
query_result = dune.get_latest_result(QUERY_ID)

# Convert to DataFrame
df = pd.DataFrame(query_result.result.rows)

# Save to CSV
output_path = os.path.join(output_dir, f"dune_query_{QUERY_ID}.csv")
df.to_csv(output_path, index=False)

print(f"CSV saved at: {output_path}") 