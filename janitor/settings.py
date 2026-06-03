from functools import cached_property

from google.adk.models import Gemini
from google.genai import Client


class GlobalGemini(Gemini):
  """Utility class to use the global region for the Gemini models."""
  @cached_property
  def api_client(self) -> Client:
    return Client(location="global")

GEMINI_MODEL=GlobalGemini(model="gemini-3.5-flash")