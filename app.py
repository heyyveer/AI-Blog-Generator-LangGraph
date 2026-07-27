import streamlit as st
from langgraph.types import Command

from graph import graph

st.set_page_config(
    page_title="AI Blog Generator",
    page_icon="📝",
    layout="wide",
)

st.title("📝 AI Blog Generator")
st.caption("LangGraph + Human in the Loop")

# ----------------------------------------------------
# Session State
# ----------------------------------------------------

if "thread_id" not in st.session_state:
    st.session_state.thread_id = "blog-thread"

config = {
    "configurable": {
        "thread_id": st.session_state.thread_id
    }
}

if "started" not in st.session_state:
    st.session_state.started = False

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

with st.sidebar:

    st.header("Blog Settings")

    topic = st.text_input("Topic")

    audience = st.selectbox(
        "Audience",
        [
            "Beginners",
            "Students",
            "Developers",
            "Professionals",
        ],
    )

    tone = st.selectbox(
        "Tone",
        [
            "Professional",
            "Friendly",
            "Conversational",
            "Formal",
        ],
    )

    keywords = st.text_input(
        "Keywords",
        placeholder="AI, LangGraph, Python"
    )

    generate = st.button(
        "🚀 Generate Blog",
        use_container_width=True,
    )

# ----------------------------------------------------
# Start Graph
# ----------------------------------------------------

if generate:

    initial_state = {
        "topic": topic,
        "audience": audience,
        "tone": tone,
        "keywords": [
            x.strip()
            for x in keywords.split(",")
            if x.strip()
        ],
        "plan": "",
        "research": "",
        "outline": "",
        "draft": "",
        "final_blog": "",
        "approved": False,
        "feedback": "",
        "current_step": "",
        "messages": [],
    }

    graph.invoke(
        initial_state,
        config=config,
    )

    st.session_state.started = True
    st.rerun()

# ----------------------------------------------------
# Continue Workflow
# ----------------------------------------------------

if st.session_state.started:

    snapshot = graph.get_state(config)

    # Finished
    if snapshot.next == ():

        st.success("✅ Blog Generated Successfully")

        blog = snapshot.values["final_blog"]

        st.markdown(blog)

        st.download_button(
            "📄 Download Markdown",
            blog,
            file_name="blog.md",
            mime="text/markdown",
        )

        st.download_button(
            "📄 Download TXT",
            blog,
            file_name="blog.txt",
            mime="text/plain",
        )

        if st.button("Generate Another Blog"):

            st.session_state.started = False
            st.session_state.thread_id = (
                st.session_state.thread_id + "_new"
            )

            st.rerun()

    else:

        interrupt_data = snapshot.interrupts[0].value

        stage = interrupt_data["stage"]
        content = interrupt_data["content"]

        st.subheader(stage)

        with st.expander("Generated Output", expanded=True):
            st.markdown(content)

        decision = st.radio(
            "Review Decision",
            ["Approve", "Reject"],
            horizontal=True,
        )

        feedback = ""

        # Show feedback box ONLY when rejected
        if decision == "Reject":
            feedback = st.text_area(
                "Why are you rejecting?",
                placeholder="Example: Add more statistics, improve introduction, use recent examples...",
                height=150,
            )

        if st.button("Continue"):

            # Feedback mandatory on rejection
            if decision == "Reject" and not feedback.strip():
                st.warning("Please provide feedback before rejecting.")
                st.stop()

            graph.invoke(
                Command(
                    resume={
                        "approved": decision == "Approve",
                        "feedback": feedback.strip(),
                    }
                ),
                config=config,
            )

            st.rerun()