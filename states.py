from typing import Annotated
from typing_extensions import TypedDict
from operator import add


class BlogState(TypedDict):

    # User input
    topic: str
    audience: str
    tone: str
    keywords: list[str]

    # Agent outputs
    plan: str
    research: str
    outline: str
    draft: str
    final_blog: str

    # Human review
    approved: bool
    feedback: str

    # Current workflow stage
    current_step: str

    # Conversation history
    messages: Annotated[list, add]