from app.collectors.ddgs_collector import (
    DDGSCollector
)
from app.intelligence.analysis import analyze_market

collector = DDGSCollector()


class AnalysisService:

    async def analyze(
        self,
        topic: str
    ):

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

            evidence.extend(results)

        # Remove duplicate URLs
        unique_evidence = []
        seen_urls = set()

        for item in evidence:

            url = item.get(
                "url",
                ""
            )

            if url in seen_urls:
                continue

            seen_urls.add(url)

            unique_evidence.append(
                item
            )

            analysis = analyze_market(
            unique_evidence
        )

        top_evidence = unique_evidence[:10]

        return {
            "topic": topic,
            "evidence_count": len(
                unique_evidence
            ),
            "market_pulse": analysis["market_pulse"],
            "opportunities": analysis["opportunities"],
            "threats": analysis["threats"],
            "top_evidence": top_evidence
        }