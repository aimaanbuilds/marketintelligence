import asyncio

from app.intelligence.gemini_analysis import (
    analyze_with_gemini
)


async def main():

    result = await analyze_with_gemini(
        [
            {
                "title":
                "Best shoes for flat feet",

                "snippet":
                "Many customers seek supportive footwear."
            }
        ]
    )

    print(result)


asyncio.run(main())