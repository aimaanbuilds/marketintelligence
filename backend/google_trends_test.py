# test_google_trends.py

import asyncio

from app.collectors.google_trends_collector import (
    GoogleTrendsCollector
)


async def main():

    collector = GoogleTrendsCollector()

    results = await collector.collect(
        "AI Nutrition Coach"
    )

    print()

    print(results)

    print()

asyncio.run(main())