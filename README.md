# SEO Content Audit Automation

A lightweight Python workflow for scalable on-page SEO and content QA.

## Checks included

- Missing or weak page titles
- Missing meta descriptions
- Incorrect H1 counts
- Thin content
- Weak internal linking

## Why I built this

Large multilingual or multi-market websites require repeatable QA. Manual review is valuable, but automation helps teams identify where human attention should go first.

## Run

```bash
python audit.py
```

The script reads `sample_pages.csv` and creates `audit_results.csv`.

## Potential extensions

- Crawl live URLs
- Add canonical and robots checks
- Detect duplicate titles/descriptions
- Integrate Google Search Console performance
- Prioritize issues using traffic and conversion data
- Add structured-data/schema validation

All sample URLs and data are fictional.
