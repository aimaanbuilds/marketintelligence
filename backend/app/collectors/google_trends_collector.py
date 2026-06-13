# app/collectors/google_trends_collector.py

from pytrends.request import TrendReq


class GoogleTrendsCollector:

    async def collect(
        self,
        topic: str
    ):

        try:

            pytrends = TrendReq(
                hl="en-US",
                tz=360
            )

            pytrends.build_payload(
                [topic],
                timeframe="today 12-m"
            )

            data = pytrends.interest_over_time()

            if data.empty:

                return []

            values = data[
                topic
            ].tolist()

            latest = values[-1]

            average = (
                sum(values)
                / len(values)
            )

            peak = max(values)

            trend = (
                "rising"
                if latest > average
                else "falling"
            )

            return [
                {
                    "source":
                    "google_trends",

                    "title":
                    topic,

                    "url":
                    "",

                    "snippet":
                    (
                        f"Interest: {latest}, "
                        f"Average: {average:.1f}, "
                        f"Peak: {peak}"
                    ),

                    "interest":
                    latest,

                    "average_interest":
                    average,

                    "peak_interest":
                    peak,

                    "trend":
                    trend
                }
            ]

        except Exception as e:

            print(
                "GOOGLE TRENDS ERROR:",
                e
            )

            return []