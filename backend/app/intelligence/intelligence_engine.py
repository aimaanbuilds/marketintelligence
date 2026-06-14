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

    try:

        customer = (
            extract_customer_intelligence(
                topic,
                evidence,
                signals
            )
        )

    except Exception as e:

        print(
            "\nCUSTOMER INTELLIGENCE FAILED:\n",
            e
        )

        customer = {}

    try:

        market = (
            extract_market_intelligence(
                topic,
                evidence,
                signals
            )
        )

    except Exception as e:

        print(
            "\nMARKET INTELLIGENCE FAILED:\n",
            e
        )

        market = {}

    try:

        competitive = (
            extract_competitive_intelligence(
                topic,
                evidence,
                signals,
                known_competitors
            )
        )

    except Exception as e:

        print(
            "\nCOMPETITIVE INTELLIGENCE FAILED:\n",
            e
        )

        competitive = {}

    return {

        "customer":
        customer,

        "market":
        market,

        "competitive":
        competitive
    }