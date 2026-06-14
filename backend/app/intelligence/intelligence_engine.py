# app/intelligence/intelligence_engine.py

from concurrent.futures import (
    ThreadPoolExecutor
)

from app.intelligence.customer_intelligence import (
    extract_customer_intelligence
)

from app.intelligence.market_intelligence import (
    extract_market_intelligence
)

from app.intelligence.competitive_intelligence import (
    extract_competitive_intelligence
)


def build_intelligence(
    topic,
    evidence,
    signals,
    known_competitors=None
):

   customer = extract_customer_intelligence(
    topic,
    evidence,
    signals
)

market = extract_market_intelligence(
    topic,
    evidence,
    signals
)

competitive = extract_competitive_intelligence(
    topic,
    evidence,
    signals,
    known_competitors
)

    return {

        "customer":
        customer,

        "market":
        market,

        "competitive":
        competitive
    }