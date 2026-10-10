import pandas as pd

df = pd.read_csv("sample_pages.csv").fillna("")

def audit(row):
    issues = []
    if not row["title"]:
        issues.append("Missing title")
    elif len(row["title"]) < 25:
        issues.append("Title may be too short")
    if not row["meta_description"]:
        issues.append("Missing meta description")
    if row["h1_count"] != 1:
        issues.append(f'H1 count = {row["h1_count"]}')
    if row["word_count"] < 800:
        issues.append("Thin content")
    if row["internal_links"] < 5:
        issues.append("Low internal-link count")
    return "; ".join(issues) if issues else "OK"

df["audit_result"] = df.apply(audit, axis=1)
df.to_csv("audit_results.csv", index=False)

print(df[["url","audit_result"]].to_string(index=False))
print("\nSaved: audit_results.csv")
