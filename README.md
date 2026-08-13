# Master Papers

Daily paper notes for recommender systems.

The automation runs every day at 08:00 Asia/Taipei and adds:

- one Markdown note under `papers/YYYY-MM/`
- the paper PDF under `pdfs/YYYY-MM/`

## Paper Selection

The script searches for recommender-system papers and prioritizes venues in this order:

1. NeurIPS
2. ICML
3. ICLR
4. SIGIR
5. RecSys

It avoids papers that already appear in this repository and only selects papers with a downloadable open-access PDF.

## Required GitHub Secret

Add this repository secret for better summaries:

- `OPENAI_API_KEY`: used to generate the English and Traditional Chinese summaries.

Optional secrets:

- `OPENAI_MODEL`: defaults to `gpt-5-mini`.
- `S2_API_KEY`: Semantic Scholar API key, useful if unauthenticated rate limits are hit.

## Manual Run

In GitHub, open **Actions** -> **Daily Recommender Systems Paper** -> **Run workflow**.
