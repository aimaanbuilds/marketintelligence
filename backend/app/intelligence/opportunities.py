def generate_opportunities(
    market_pulse
):

    opportunities = []

    if (
        market_pulse.growth > 20
        and
        market_pulse.competition < 5
    ):

        opportunities.append(
            {
                "title":
                "Underserved Market",

                "score":
                85,

                "confidence":
                78,

                "rationale":
                "High growth with limited competition"
            }
        )

    return opportunities