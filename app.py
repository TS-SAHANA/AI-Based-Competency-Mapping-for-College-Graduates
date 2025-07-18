# app.py

import streamlit as st
from questions import skills_questions
from backend.skill_gap import analyze_skill_gap, calculate_readiness_score
from backend.recommendations import recommend_learning
import joblib
import numpy as np


st.set_page_config(page_title="Skill Gap Analyzer", layout="centered")
model = joblib.load("models/skill_level_classifier.pkl")  # Adjust path if needed
label_to_level = {0: "none", 1: "beginner", 2: "intermediate", 3: "advanced"}

# -------------------------- Skill Level Assessment Logic --------------------------

# Mapping numeric labels back to string levels
label_to_level = {
    0: "none",
    1: "beginner",
    2: "intermediate",
    3: "advanced"
}

# -------------------------- Streamlit App --------------------------

def main():
    st.title("🎓 Real-Time Skill Gap Analyzer")

    with st.form("user_form"):
        st.subheader("👤 Personal Details")
        name = st.text_input("Your Name")
        degree = st.text_input("Your Degree (e.g., B.Tech CSE)")
        cgpa = st.slider("Your CGPA", min_value=0.0, max_value=10.0, step=0.01)
        career_goal = st.text_input("Career Goal")

        st.subheader("🎯 Choose Target Job Role")
        job_roles = {
            "Data Analyst": ["python", "sql", "excel", "statistics", "powerbi"],
            "Software Developer": ["python", "java", "ds_algo", "dbms", "oop"],
            "UI/UX Designer": ["figma", "design_thinking", "html_css", "portfolio"]
        }

        role_options = list(job_roles.keys())
        selected_role = st.selectbox("Target Role", ["Select..."] + role_options)

        skill_responses = {}
        submitted = False

        if selected_role != "Select...":
            st.subheader("🧠 Skill Assessment")

            selected_skills = job_roles[selected_role]
            available_skills = [s for s in selected_skills if s in skills_questions]

            if not available_skills:
                st.info("No questions available for the selected role yet.")
            else:
                for skill in available_skills:
                    st.markdown(f"### Skill: {skill.replace('_', ' ').capitalize()}")
                    answers = []
                    for q in skills_questions[skill]:
                        user_ans = st.radio(
                            f"{q['level'].capitalize()} - {q['question']}",
                            q['options'],
                            index=None,
                            key=f"{skill}_{q['level']}"
                        )
                        answers.append(int(user_ans == q['answer']))

                    feature = np.array([answers])  # shape (1, 3)
                    prediction = model.predict(feature)[0]
                    skill_responses[skill] = label_to_level.get(int(prediction), "none")

            submitted = st.form_submit_button("🔍 Analyze Skill Level")
        else:
            st.info("Please select a job role to proceed.")
            submitted = st.form_submit_button("🔍 Analyze")

    # After submission
    if submitted and selected_role != "Select...":
        st.success("✅ Analysis Complete!")

        required_skills = job_roles[selected_role]
        weak_skills = analyze_skill_gap(skill_responses, required_skills)
        readiness_score = calculate_readiness_score(skill_responses, required_skills)

        st.subheader("📊 Skill Level Report")
        for skill, level in skill_responses.items():
            st.markdown(f"- **{skill.replace('_', ' ').capitalize()}**: `{level}`")

        st.subheader("📉 Skill Gaps")
        if weak_skills:
            st.write("You may need to work on the following skills:")
            st.markdown(", ".join(f"`{skill.replace('_', ' ')}`" for skill in weak_skills))

            st.subheader("📚 Recommended Learning Plan")
            recommendations = recommend_learning(weak_skills)
            for rec in recommendations:
                st.markdown(f"- **{rec['skill'].replace('_', ' ').capitalize()}**:")
                for resource in rec['resources']:
                    st.markdown(f"  - {resource}")
        else:
            st.success("You're well-prepared for this role. Great job!")


        st.subheader("📈 Placement Readiness Score")
        st.metric(label="Readiness Score", value=f"{readiness_score}/100")

        st.subheader("📄 Student Profile Summary")
        st.markdown(f"**Name:** {name}")
        st.markdown(f"**Degree:** {degree}")
        st.markdown(f"**CGPA:** {cgpa}")
        st.markdown(f"**Career Goal:** {career_goal}")
        st.markdown(f"**Target Role:** {selected_role}")


if __name__ == "__main__":
    main()
