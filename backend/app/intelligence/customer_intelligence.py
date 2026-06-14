import json

from app.services.openrouter_service import (
    OpenRouterService
)


def extract_customer_intelligence(
    topic,
    evidence,
    signals
):

    prompt = f"""
You are a customer research analyst.

Topic:
{topic}

Signals:
{signals}

Evidence:
{evidence}

Base conclusions ONLY on provided evidence.

Return ONLY valid JSON.

Definitions:

Customer Segment:
A distinct group of users likely to buy this product.

Pain Point:
A frustration, unmet need, challenge, or obstacle experienced by customers.

Desired Outcome:
A result customers want to achieve.

Behavior Pattern:
An observable behavior, habit, or decision-making pattern.

Opportunity Area:
An underserved customer need, emerging trend, or market gap.

Rules:

- Base conclusions ONLY on provided evidence.
- Do not invent facts.
- Pain points must be actual problems.
- Desired outcomes must be customer goals.
- Customer segments must be specific, not generic.
- Return the highest-confidence insights first.
- Scores must be 0-100
- Return 5-10 items per category
- Rank highest scoring items first
- No explanations outside JSON

Schema:

{{
  "customer_segments": [
    {{
      "name": "",
      "importance": 0
    }}
  ],

  "pain_points": [
    {{
      "name": "",
      "signal_strength": 0
    }}
  ],

  "desired_outcomes": [
    {{
      "name": "",
      "importance": 0
    }}
  ],

  "behavior_patterns": [
    {{
      "name": "",
      "confidence": 0
    }}
  ],

  "opportunity_areas": [
    {{
      "name": "",
      "score": 0
    }}
  ]
}}

Additional Requirements:

- Return at least 5 items when evidence supports it.
- Use concise names (3-8 words).
- Avoid generic segments like "everyone" or "health-conscious users" unless strongly supported by evidence.
- Rank by confidence and importance.
- Output valid JSON only.
"""

    service = OpenRouterService()

    service = OpenRouterService()

    return service.call_json(
        prompt
)