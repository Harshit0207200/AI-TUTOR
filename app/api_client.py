# app/api_client.py

from dotenv import load_dotenv
import os
from groq import Groq

# Load environment variables from .env
load_dotenv()
print("🔥 api_client.py loaded ENV (has key?):", bool(os.getenv("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")))


class GroqClient:
    def __init__(self):
        # Get API key from environment
        self.api_key = os.getenv("GROQ_API_KEY")

        print("📌 DEBUG: GROQ_API_KEY is set?", bool(self.api_key))

        if not self.api_key:
            raise ValueError(
                "❌ ERROR: GROQ_API_KEY is NOT set! Make sure your .env contains:\n"
                "GROQ_API_KEY=your_key_here"
            )

        # Initialize Groq client
        self.client = Groq(api_key=self.api_key)
        print("✅ GroqClient initialized successfully.")

    def get_response(self, messages):
        """
        Send messages to Groq and return the model's text response.
        Messages must be a list like:
        [{"role": "user", "content": "..."}]
        """
        try:
            response = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",  # fast and stable model
                messages=messages,
                temperature=0.5,
                max_tokens=300,
            )

            # Correct extraction of response content
            return response.choices[0].message.content

        except Exception as e:
            print("❌ ERROR calling Groq API:", e)
            raise
