from config import client

def extract_thermal_issues(text):

    prompt = f"""
You are analyzing thermal inspection data.

Extract building moisture or leakage issues.

Return JSON:

[
 {{
  "area": "...",
  "thermal_issue": "...",
  "explanation": "..."
 }}
]

Thermal Report:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0
    )

    return response.choices[0].message.content