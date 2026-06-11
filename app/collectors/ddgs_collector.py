from duckduckgo_search import DDGS


class DDGSCollector:

    async def collect(
        self,
        query: str
    ):

        with DDGS() as ddgs:

            return list(
                ddgs.text(
                    query,
                    max_results=10
                )
            )