from config import client

def extract_observations(text):

    prompt = f"""
You are a building inspection expert.

From the following inspection report extract area-wise issues.

Return STRICT JSON:

[
 {{
  "area": "...",
  "issue": "...",
  "details": "..."
 }}
]

Inspection Report:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0
    )

    return response.choices[0].message.content