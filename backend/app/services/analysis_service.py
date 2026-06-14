from app.collectors.ddgs_collector import (
    DDGSCollector
)

from app.signals.signal_engine import (
    build_signals
)

from app.pipeline.analyze_topic import (
    analyze_topic
)


collector = DDGSCollector()


class AnalysisService:

    async def analyze(
        self,
        topic: str
    ):

        print(
            "\nSTEP 1: START COLLECTION"
        )

        queries = [

            # Competition
            f"{topic} competitors",
            f"{topic} alternatives",

            # Customer sentiment
            f"{topic} customer complaints",
            f"{topic} reviews",
            f"{topic} complaints",

            # Market intelligence
            f"{topic} funding",
            f"{topic} startup launches",
            f"{topic} market trends",
            f"{topic} pricing",
            f"{topic} growth",

            # Community discussions
            f"site:reddit.com {topic}",
            f"site:youtube.com {topic}"
        ]

        evidence = []

        for query in queries:

            results = await collector.collect(
                query,
                topic
            )

            evidence.extend(
                results
            )

        print(
            "\nSTEP 2: COLLECTION COMPLETE"
        )

        unique_evidence = []

        seen_urls = set()

        for item in evidence:

            url = item.get(
                "url",
                ""
            )

            if url in seen_urls:
                continue

            seen_urls.add(
                url
            )

            unique_evidence.append(
                item
            )

        print(
            "\nSTEP 3: UNIQUE EVIDENCE:",
            len(unique_evidence)
        )

        signals = build_signals(
            unique_evidence
        )

        print(
            "\nSTEP 4: SIGNALS BUILT"
        )

        known_competitors = []

        print(
            "\nSTEP 5: RUNNING PIPELINE"
        )

        result = analyze_topic(

            topic=topic,

            evidence=unique_evidence,

            signals=signals,

            known_competitors=
            known_competitors
        )

        print(
            "\nSTEP 6: PIPELINE COMPLETE"
        )

        return result