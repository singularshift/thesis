# Election Day Data Extraction

This project extracts data from Dune Analytics using their API.

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with your Dune API key:
   ```
   DUNE_API_KEY=your_api_key_here
   ```

## Usage

Run the extraction script:
```bash
python csvextractions/electionday_extraction.py
```

The extracted data will be saved in the `csvfileselection` directory.

## Environment Variables

- `DUNE_API_KEY`: Your Dune Analytics API key 