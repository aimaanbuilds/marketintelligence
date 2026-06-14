from app.services.openrouter_service import (
    OpenRouterService
)


def extract_competitive_intelligence(
    topic,
    evidence,
    signals,
    known_competitors=None
):
    
    known_competitors = (
    known_competitors
    or
    []
)
    competitive_evidence = [

    item

    for item in evidence

    if item.get("source") in [

        "producthunt",
        "ddgs"
    ]
]

    prompt = f"""
You are a senior competitive intelligence analyst.

Topic:
{topic}

Signals:
{signals}

Known Competitors:
{known_competitors}

Evidence:
{competitive_evidence}

Your job is to identify:

1. Competitors
2. Competitive threats
3. Positioning gaps
4. White space opportunities
5. Differentiation opportunities

 

Definitions:

Competitor:
A company, product, or solution solving the same or a similar problem.
- Use known competitors whenever relevant.
- Do not invent competitors if known competitors are provided.
- Identify gaps in their positioning.
- Identify unmet customer needs they do not serve well.

Competitive Threat:
Something that makes the market harder to enter or win.

Positioning Gap:
A customer need competitors are not serving well.

White Space Opportunity:
An underserved market area with strong potential.

Differentiation Opportunity:
A way the product could stand apart from competitors.

Rules:

- Base conclusions ONLY on provided evidence.
- Do not invent competitors.
- If evidence is weak, lower confidence.
- Rank strongest insights first.
- Scores must be between 0 and 100.
- Return ONLY valid JSON.
-Ignore evidence that solves a fundamentally different problem than the topic.

Schema:

Schema:

{{
  "competitors": [
    {{
      "name": "",
      "strength": 0
    }}
  ],

  "competitive_threats": [
    {{
      "name": "",
      "severity": 0
    }}
  ],

  "positioning_gaps": [
    {{
      "name": "",
      "opportunity": 0
    }}
  ],

  "white_space_opportunities": [
    {{
      "name": "",
      "score": 0
    }}
  ],

  "differentiation_opportunities": [
    {{
      "name": "",
      "score": 0
    }}
  ]
}}

Additional Requirements:

- Return a maximum of 5 items per category.
- Use concise names.
- Rank highest-confidence items first.
- Output valid JSON only.
"""

    service = OpenRouterService()
    

    return service.call_json(
        prompt,
        debug=False
    )
    
