import streamlit as st
import os

from agent import (
    run_agent,
    generate_plan
)

# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="Autonomous AI Document Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# Custom CSS
# =====================================================

st.markdown("""
<style>

.main{
    padding-top:20px;
}

.stButton>button{
    width:100%;
    height:55px;
    font-size:18px;
    border-radius:12px;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# Sidebar
# =====================================================

with st.sidebar:

    st.title("🤖 AI Document Agent")

    st.write("---")

    st.markdown("""
This autonomous agent can generate:

- 📄 Business Proposal
- 📊 Business Report
- 📚 SOP
- 🏥 Technical Design
- 📈 Project Plan
- 📝 Meeting Minutes
- 📖 Product Specification
""")

    st.write("---")

    st.success("Powered by Groq + Llama 3.3")

# =====================================================
# Main Page
# =====================================================

st.title("🤖 Autonomous AI Document Generator")

st.write(
    "Describe any professional document. "
    "The AI agent will automatically create an execution plan, "
    "generate each section, and produce a downloadable Word document."
)

user_request = st.text_area(
    "Enter your request",
    placeholder="Example:\n\nCreate a business proposal for an AI chatbot for a hospital.",
    height=220
)

# =====================================================
# Generate Button
# =====================================================

generate = st.button(
    "🚀 Generate Document"
)

if generate:

    if len(user_request.strip()) < 10:

        st.error("Please enter a longer request.")

        st.stop()

    st.write("---")

    st.subheader("📋 Execution Plan")

    with st.spinner("Planning..."):

        plan = generate_plan(user_request)

    st.success("Plan Generated")

    for task in plan.tasks:

        st.markdown(
            f"""
**Step {task.step}**

**Task:** {task.description}

**Expected Output:** {task.expected_output}

---
"""
        )



# =====================================================
# Generate Document
# =====================================================

if generate:

    if len(user_request.strip()) < 10:
        st.error("Please enter a valid request.")
        st.stop()

    # -----------------------------
    # Progress Components
    # -----------------------------
    progress_bar = st.progress(0)

    status = st.empty()

    def update_progress(current, total, task_name):

        percent = int((current / total) * 100)

        progress_bar.progress(percent)

        status.info(
            f"Step {current}/{total} : {task_name}"
        )

    try:

        with st.spinner("AI Agent is working..."):

            result = run_agent(
                user_request=user_request,
                progress_callback=update_progress
            )

        progress_bar.progress(100)

        status.success("Document Generated Successfully!")

        st.balloons()

        st.write("---")

        st.subheader("📄 Document Information")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Title",
                result.title
            )

        with col2:

            st.metric(
                "Type",
                result.document_type
            )

        st.write("---")

        st.subheader("Generated Sections")

        for step, content in result.sections.items():

            with st.expander(f"Section {step}"):

                st.write(content)

        st.write("---")

        with open(result.filename, "rb") as file:

            st.download_button(
                label="📥 Download Word Document",
                data=file,
                file_name=os.path.basename(result.filename),
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

    except Exception as e:

        progress_bar.empty()

        status.empty()

        st.error(str(e))        