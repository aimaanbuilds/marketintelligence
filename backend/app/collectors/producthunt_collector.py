# app/collectors/producthunt_collector.py

import os
import requests

from dotenv import load_dotenv

load_dotenv()


class ProductHuntCollector:

    def get_token(self):

        response = requests.post(
            "https://api.producthunt.com/v2/oauth/token",
            json={
                "client_id": os.getenv(
                    "PRODUCTHUNT_CLIENT_ID"
                ),
                "client_secret": os.getenv(
                    "PRODUCTHUNT_CLIENT_SECRET"
                ),
                "grant_type": "client_credentials"
            }
        )

        response.raise_for_status()

        return response.json()[
            "access_token"
        ]

    async def collect(
        self,
        topic: str
    ):

        try:

            token = self.get_token()

            query = """
            {
              posts(first: 50) {
                edges {
                  node {
                    name
                    tagline
                    votesCount
                    commentsCount
                    createdAt
                    url

                    topics {
                      edges {
                        node {
                          name
                        }
                      }
                    }
                  }
                }
              }
            }
            """

            response = requests.post(
                "https://api.producthunt.com/v2/api/graphql",
                json={
                    "query": query
                },
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json"
                }
            )

            response.raise_for_status()

            data = response.json()

            results = []

            posts = (
                data["data"]
                ["posts"]
                ["edges"]
            )

            for post in posts:

                node = post["node"]

                topics = [
                    topic_node["node"]["name"]
                    for topic_node
                    in node["topics"]["edges"]
                ]

                results.append(
                    {
                        "source": "producthunt",

                        "title": node["name"],

                        "url": node["url"],

                        "snippet": node["tagline"],

                        "votes": node["votesCount"],

                        "comments": node["commentsCount"],

                        "launch_date": node["createdAt"],

                        "topics": topics
                    }
                )

            print(
                f"PRODUCT HUNT RESULTS: {len(results)}"
            )

            return results

        except Exception as e:

            print(
                "PRODUCT HUNT ERROR:",
                e
            )

            return []