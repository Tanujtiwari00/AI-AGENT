import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Career Agent Pro", page_icon="🚀", layout="wide")

st.title("🚀 AI Career Agent Pro")
st.caption("Advanced Career Intelligence Platform for Freshers")

# Sidebar
st.sidebar.header("👤 Candidate Profile")
name = st.sidebar.text_input("Name")
experience = st.sidebar.selectbox(
    "Experience",
    ["Fresher", "0-1 Year", "1-3 Years", "3+ Years"]
)
preferred = st.sidebar.selectbox(
    "Preferred Domain",
    ["Any", "Data", "Development", "Business", "AI/ML"]
)

skills = st.text_area(
    "Enter Skills (comma separated)",
    "Python, SQL, Excel"
)

# Career Database
career_map = {
    "Data Analyst": ["sql", "excel", "python", "power bi", "tableau", "statistics"],
    "Business Analyst": ["excel", "sql", "communication", "power bi", "analysis"],
    "Python Developer": ["python", "api", "flask", "django", "git"],
    "Frontend Developer": ["html", "css", "javascript", "react"],
    "Backend Developer": ["python", "sql", "api", "fastapi", "django"],
    "AI Engineer": ["python", "machine learning", "numpy", "pandas"],
    "ML Engineer": ["python", "machine learning", "statistics", "sql"],
    "MIS Executive": ["excel", "reporting", "communication"],
    "BI Analyst": ["power bi", "sql", "excel", "dashboard"],
    "Product Analyst": ["sql", "excel", "analysis", "communication"]
}

domain_map = {
    "Data": ["Data Analyst", "Business Analyst", "BI Analyst", "Product Analyst"],
    "Development": ["Python Developer", "Frontend Developer", "Backend Developer"],
    "Business": ["Business Analyst", "MIS Executive", "Product Analyst"],
    "AI/ML": ["AI Engineer", "ML Engineer"]
}

if st.button("🔍 Analyze Career Opportunities"):

    user_skills = [x.strip().lower() for x in skills.split(",") if x.strip()]

    results = []

    for role, req_skills in career_map.items():
        matched = [s for s in req_skills if s in user_skills]
        score = int((len(matched) / len(req_skills)) * 100)

        # Domain filtering
        if preferred != "Any":
            if role not in domain_map.get(preferred, []):
                continue

        missing = [s for s in req_skills if s not in user_skills]

        results.append({
            "Role": role,
            "Match Score": score,
            "Matched Skills": ", ".join(matched) if matched else "-",
            "Missing Skills": ", ".join(missing[:4])
        })

    df = pd.DataFrame(results).sort_values(by="Match Score", ascending=False)

    st.success(f"Welcome {name}! Here are your best-fit careers.")

    # Top 3 metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Top Role", df.iloc[0]["Role"])

    with col2:
        st.metric("Best Score", f'{df.iloc[0]["Match Score"]}%')

    with col3:
        st.metric("Roles Analyzed", len(df))

    st.subheader("🏆 Top Career Matches")
    st.dataframe(df, use_container_width=True)

    st.subheader("📈 Top 5 Roles")
    top5 = df.head(5)
    st.bar_chart(top5.set_index("Role")["Match Score"])

    st.subheader("📚 Personalized Learning Roadmap")
    best_role = df.iloc[0]["Role"]
    best_missing = df.iloc[0]["Missing Skills"]

    st.write(f"To become a stronger **{best_role}**, learn:")
    st.info(best_missing)

    st.subheader("📌 Resume Advice")
    st.write("✔ Add 2 portfolio projects")
    st.write("✔ Add measurable achievements")
    st.write("✔ Use ATS keywords for target role")
    st.write("✔ Keep resume one page")
    st.write("✔ Add GitHub + LinkedIn links")

    st.subheader("🔥 Final Recommendation")
    if df.iloc[0]["Match Score"] >= 70:
        st.success(f"You are job-ready for {best_role}")
    elif df.iloc[0]["Match Score"] >= 45:
        st.warning(f"You are close to {best_role}. Upskill now.")
    else:
        st.error("Need stronger skills before applying aggressively.")