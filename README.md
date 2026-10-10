# SEO Content Audit Automation

A lightweight Python workflow for scalable on-page SEO and content QA.
## Executive summary

This project demonstrates how I use automation to make SEO and content QA more scalable across large websites.

The workflow reviews common on-page issues such as titles, meta descriptions, heading structure, content depth, and internal linking, then flags pages that require attention.

The goal is not to replace human editorial judgment, but to help marketing teams focus that judgment where it has the highest value.

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

## Business value

This type of workflow can help marketing teams:

- Reduce manual QA effort across large websites
- Prioritize pages with the highest optimization need
- Standardize SEO checks across markets and content teams
- Support multilingual content governance
- Combine technical SEO signals with traffic and conversion data
- Create repeatable pre-publication and post-publication QA processes
All sample URLs and data are fictional.
