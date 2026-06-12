from ddgs import DDGS


class DDGSCollector:

    async def collect(
        self,
        query: str
    ):

        try:

            with DDGS() as ddgs:

                results = list(
                    ddgs.text(
                        query,
                        max_results=10
                    )
                )

            normalized_results = []

            for result in results:

                normalized_results.append(
                    {
                        "source": "ddgs",
                        "title": result.get(
                            "title",
                            ""
                        ),
                        "url": result.get(
                            "href",
                            ""
                        ),
                        "snippet": result.get(
                            "body",
                            ""
                        )
                    }
                )

            return normalized_results

        except Exception as e:

            print(
                "DDGS ERROR:",
                str(e)
            )

            return []