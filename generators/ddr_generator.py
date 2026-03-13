from config import client

def generate_ddr(observations, thermal):

    prompt = f"""
You are a structural diagnostic engineer.

Using the following inspection observations and thermal findings,
generate a professional **Detailed Diagnostic Report (DDR)**.

The format must match:

1 PROPERTY ISSUE SUMMARY
2 AREA-WISE OBSERVATIONS
3 PROBABLE ROOT CAUSE
4 SEVERITY ASSESSMENT
5 RECOMMENDED ACTIONS
6 ADDITIONAL NOTES
7 MISSING INFORMATION

Inspection Observations:
{observations}

Thermal Findings:
{thermal}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content