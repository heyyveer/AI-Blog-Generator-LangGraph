from dotenv import load_dotenv

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq

from prompts import (
    PLANNER_PROMPT,
    RESEARCH_PROMPT,
    OUTLINE_PROMPT,
    WRITER_PROMPT,
    EDITOR_PROMPT,
)

load_dotenv()

# ----------------------------------------------------
# LLM
# ----------------------------------------------------

llm = ChatGroq(
    model_name="openai/gpt-oss-20b",
    temperature=0.5,
)

# ----------------------------------------------------
# Helper
# ----------------------------------------------------

def generate(system_prompt: str, human_prompt: str):
    response = llm.invoke(
        [
            SystemMessage(content=system_prompt),
            HumanMessage(content=human_prompt),
        ]
    )
    return response.content


# ----------------------------------------------------
# Planner
# ----------------------------------------------------

def planner_agent(state):

    prompt = PLANNER_PROMPT.format(
        topic=state["topic"],
        audience=state["audience"],
        tone=state["tone"],
        keywords=", ".join(state["keywords"]),
    )

    plan = generate(
        "You are an expert Content Strategist.",
        prompt,
    )

    return {
        "plan": plan,
        "current_step": "Planning",
    }


# ----------------------------------------------------
# Research
# ----------------------------------------------------

def research_agent(state):

    prompt = RESEARCH_PROMPT.format(
        topic=state["topic"],
        plan=state["plan"],
        feedback=state["feedback"],
    )

    research = generate(
        "You are an expert Research Analyst.",
        prompt,
    )

    return {
        "research": research,
        "feedback": "",
        "current_step": "Research",
    }


# ----------------------------------------------------
# Outline
# ----------------------------------------------------

def outline_agent(state):

    prompt = OUTLINE_PROMPT.format(
        topic=state["topic"],
        research=state["research"],
        feedback=state["feedback"],
    )

    outline = generate(
        "You are an expert Technical Writer.",
        prompt,
    )

    return {
        "outline": outline,
        "feedback": "",
        "current_step": "Outline",
    }


# ----------------------------------------------------
# Writer
# ----------------------------------------------------

def writer_agent(state):

    prompt = WRITER_PROMPT.format(
        topic=state["topic"],
        audience=state["audience"],
        tone=state["tone"],
        keywords=", ".join(state["keywords"]),
        outline=state["outline"],
        feedback=state["feedback"],
    )

    draft = generate(
        "You are an expert Blog Writer.",
        prompt,
    )

    return {
        "draft": draft,
        "feedback": "",
        "current_step": "Writing",
    }


# ----------------------------------------------------
# Editor
# ----------------------------------------------------

def editor_agent(state):

    prompt = EDITOR_PROMPT.format(
        draft=state["draft"],
    )

    final_blog = generate(
        "You are a Senior Content Editor.",
        prompt,
    )

    return {
        "final_blog": final_blog,
        "current_step": "Completed",
    }