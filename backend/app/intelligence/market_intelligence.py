from app.services.openrouter_service import (
    OpenRouterService
)


def extract_market_intelligence(
    topic,
    evidence,
    signals
):

    prompt = f"""
You are a senior market intelligence analyst.

Topic:
{topic}

Signals:
{signals}

Detected Market Sizes:
{signals.get("market_opportunity", {}).get("detected_market_sizes", [])}

Detected Growth Rates:
{signals.get("market_opportunity", {}).get("detected_growth_rates", [])}

Evidence:
{evidence}

Your goal is to estimate:

1. Market opportunity
2. Market growth
3. Market maturity
4. Key trends
5. Emerging trends
6. Market drivers
7. Future outlook

Definitions:

Market Size:
Use detected market sizes when available.

Growth Rate:
Use detected growth rates when available.

Market Maturity:
Must be one of:

- Emerging
- Growth
- Mature
- Declining

Key Trend:
Already impacting the market.

Emerging Trend:
Likely to become important in the next 1-3 years.

Market Driver:
A force causing adoption or growth.

Future Outlook:
Expected market direction over the next 12-24 months.

Rules:

- Base conclusions ONLY on provided evidence.
- Prefer extracted market sizes and growth rates over assumptions.
- If evidence is weak, lower confidence.
- Rank strongest trends first.
- Scores must be 0-100.
- Return ONLY valid JSON.

Schema:

{{
  "market_size": {{
    "estimate": "",
    "confidence": 0
  }},

  "growth_rate": {{
    "estimate": "",
    "confidence": 0
  }},

  "market_maturity": {{
    "stage": "",
    "confidence": 0
  }},

  "future_outlook": {{
    "direction": "",
    "confidence": 0
  }},

  "key_trends": [
    {{
      "name": "",
      "strength": 0
    }}
  ],

  "emerging_trends": [
    {{
      "name": "",
      "potential": 0
    }}
  ],

  "market_drivers": [
    {{
      "name": "",
      "impact": 0
    }}
  ]
}}

Additional Requirements:

- Return 5-10 trends when evidence supports it.
- Use concise names.
- Rank highest-confidence items first.
- Output valid JSON only.
"""

    service = OpenRouterService()

    return service.call_json(
        prompt,
        debug=False
    )