import os
import re
import json
import requests

from dotenv import load_dotenv

load_dotenv()


class OpenRouterService:

    def __init__(self):

        self.api_key = os.getenv(
            "OPENROUTER_API_KEY"
        )

        self.url = (
            "https://openrouter.ai/api/v1/chat/completions"
        )

        self.default_model = (
            "openrouter/free"
        )

    def call(
        self,
        prompt,
        model=None,
        debug=False
    ):

        model = (
            model
            or
            self.default_model
        )

        response = requests.post(

            self.url,

            timeout=60,

            headers={

                "Authorization":
                f"Bearer {self.api_key}",

                "Content-Type":
                "application/json",

                "HTTP-Referer":
                "http://localhost",

                "X-Title":
                "Signal"
            },

            json={

                "model":
                model,

                "messages": [

                    {
                        "role":
                        "user",

                        "content":
                        prompt
                    }
                ]
            }
        )

        if debug:

            print(
                "\nOPENROUTER STATUS:",
                response.status_code
            )

            print(
                "\nOPENROUTER BODY:\n",
                response.text[:2000]
            )

        response.raise_for_status()

        data = response.json()

        return (
            data["choices"][0]
            ["message"]
            ["content"]
        )

    def call_json(
        self,
        prompt,
        model=None,
        debug=False
    ):

        response_text = self.call(
            prompt=prompt,
            model=model,
            debug=debug
        )

        try:

            return json.loads(
                response_text
            )

        except Exception:

            match = re.search(
                r"\{.*\}",
                response_text,
                re.DOTALL
            )

            if not match:

                print("\nRAW RESPONSE:")
                print(response_text)

                raise Exception(
                    "No JSON found in model response"
                )

            return json.loads(
                match.group()
            )

        match = re.search(
            r"\{.*\}",
            response_text,
            re.DOTALL
        )

        if not match:

            print("\nRAW RESPONSE:")
            print(response_text)

            raise Exception(
                "No JSON found in model response"
            )

        return json.loads(
            match.group()
        )