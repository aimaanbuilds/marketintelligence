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

    with ThreadPoolExecutor(
        max_workers=3
    ) as executor:

        customer_future = (
            executor.submit(
                extract_customer_intelligence,
                topic,
                evidence,
                signals
            )
        )

        market_future = (
            executor.submit(
                extract_market_intelligence,
                topic,
                evidence,
                signals
            )
        )

        competitive_future = (
            executor.submit(
                extract_competitive_intelligence,
                topic,
                evidence,
                signals,
                known_competitors
            )
        )

        customer = (
            customer_future.result()
        )

        market = (
            market_future.result()
        )

        competitive = (
            competitive_future.result()
        )

    return {

        "customer":
        customer,

        "market":
        market,

        "competitive":
        competitive
    }