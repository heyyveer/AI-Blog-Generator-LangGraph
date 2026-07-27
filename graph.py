from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import interrupt

from states import BlogState

from agents import (
    planner_agent,
    research_agent,
    outline_agent,
    writer_agent,
    editor_agent,
)

# =====================================================
# Review Nodes
# =====================================================

def review_research(state: BlogState):

    review = interrupt(
        {
            "stage": "Research Review",
            "content": state["research"],
        }
    )

    return {
        "approved": review.get("approved", False),
        "feedback": review.get("feedback", ""),
    }


def review_outline(state: BlogState):

    review = interrupt(
        {
            "stage": "Outline Review",
            "content": state["outline"],
        }
    )

    return {
        "approved": review.get("approved", False),
        "feedback": review.get("feedback", ""),
    }


def review_draft(state: BlogState):

    review = interrupt(
        {
            "stage": "Draft Review",
            "content": state["draft"],
        }
    )

    return {
        "approved": review.get("approved", False),
        "feedback": review.get("feedback", ""),
    }


# =====================================================
# Routers
# =====================================================

def research_router(state: BlogState):
    if state["approved"]:
        return "outline"
    return "research"


def outline_router(state: BlogState):
    if state["approved"]:
        return "writer"
    return "outline"


def draft_router(state: BlogState):
    if state["approved"]:
        return "editor"
    return "writer"


# =====================================================
# Build Graph
# =====================================================

builder = StateGraph(BlogState)

builder.add_node("planner", planner_agent)
builder.add_node("research", research_agent)
builder.add_node("review_research", review_research)

builder.add_node("outline", outline_agent)
builder.add_node("review_outline", review_outline)

builder.add_node("writer", writer_agent)
builder.add_node("review_draft", review_draft)

builder.add_node("editor", editor_agent)

# =====================================================
# Edges
# =====================================================

builder.add_edge(START, "planner")
builder.add_edge("planner", "research")
builder.add_edge("research", "review_research")

builder.add_conditional_edges(
    "review_research",
    research_router,
    {
        "research": "research",
        "outline": "outline",
    },
)

builder.add_edge("outline", "review_outline")

builder.add_conditional_edges(
    "review_outline",
    outline_router,
    {
        "outline": "outline",
        "writer": "writer",
    },
)

builder.add_edge("writer", "review_draft")

builder.add_conditional_edges(
    "review_draft",
    draft_router,
    {
        "writer": "writer",
        "editor": "editor",
    },
)

builder.add_edge("editor", END)

# =====================================================
# Compile
# =====================================================

memory = MemorySaver()

graph = builder.compile(
    checkpointer=memory
)