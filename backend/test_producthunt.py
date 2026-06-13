# test_producthunt.py

import asyncio

from app.collectors.producthunt_collector import (
    ProductHuntCollector
)

async def main():

    collector = ProductHuntCollector()

    results = await collector.collect(
        "AI Nutrition Coach"
    )

    print()

    print(
        "RESULT COUNT:",
        len(results)
    )

    print()

    for item in results[:5]:

        print("=" * 60)

        print(
            "TITLE:",
            item["title"]
        )

        print(
            "VOTES:",
            item["votes"]
        )

        print(
            "COMMENTS:",
            item["comments"]
        )

        print(
            "TOPICS:",
            item["topics"]
        )

        print(
            "LAUNCHED:",
            item["launch_date"]
        )

        print(
            "URL:",
            item["url"]
        )

        print(
            "TAGLINE:",
            item["snippet"]
        )

        print()

asyncio.run(main())