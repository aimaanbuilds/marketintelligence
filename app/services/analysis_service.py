from app.collectors.ddgs_collector import (
    DDGSCollector
)

collector = DDGSCollector()


class AnalysisService:

    async def analyze(
        self,
        topic: str
    ):

        evidence = await collector.collect(
            topic
        )

        return {
            "topic": topic,
            "summary": f"Found {len(evidence)} pieces of evidence"
        }