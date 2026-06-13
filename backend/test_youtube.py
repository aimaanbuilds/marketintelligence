import asyncio

from app.collectors.youtube_collector import (
    YouTubeCollector
)


async def main():

    collector = YouTubeCollector()

    results = await collector.collect(
        "AI Nutrition Coach"
    )

    print()

    for item in results:

        print("=" * 60)

        print(
            item["title"]
        )

        print(
            "Views:",
            item["views"]
        )

        print(
            "Likes:",
            item["likes"]
        )

        print(
            "Comments:",
            item["comments"]
        )

        print(
            "Channel:",
            item["channel"]
        )

        print(
            "Published:",
            item["published"]
        )

        print(
            item["url"]
        )

        print()

asyncio.run(main())