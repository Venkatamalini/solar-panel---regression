import streamlit as st
import pandas as pd
import pickle
import joblib
import tempfile
import plotly.express as px
from PIL import Image

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(
    page_title="Malini Venkata | Data Science Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================
# CUSTOM CSS
# =========================================
st.markdown("""
<style>
    .main {
        background-color: #0E1117;
        color: white;
    }

    h1, h2, h3, h4 {
        color: white;
    }

    .stButton>button {
        background-color: #2563EB;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 0.5rem 1rem;
    }

    .stButton>button:hover {
        background-color: #1D4ED8;
        color: white;
    }

    .card {
        background-color: #161B22;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }

    .skill-box {
        background-color: #1F2937;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        margin: 5px;
        font-weight: bold;
    }

    footer {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)

# =========================================
# SIDEBAR
# =========================================
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Go To",
    ["Home", "About", "Skills", "Projects", "Certificates", "Contact"]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Data Science | Machine Learning | Streamlit Developer"
)

# =========================================
# HOME PAGE
# =========================================
if page == "Home":

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1526379095098-d400fd0bf935?q=80&w=1200&auto=format&fit=crop",
            use_container_width=True
        )

    with col2:
        st.markdown("# 👋 Hello, I'm Malini Venkata")
        st.markdown("## Data Science & Machine Learning Enthusiast")

        st.write(
            """
            Passionate about building interactive data-driven applications,
            machine learning models, dashboards, and forecasting systems.

            I love transforming raw data into meaningful insights using
            Python, Streamlit, Machine Learning, and Data Visualization.
            """
        )

        st.markdown("---")

        colA, colB, colC = st.columns(3)

        with colA:
            st.metric("Projects", "10+")

        with colB:
            st.metric("Certifications", "5+")

        with colC:
            st.metric("Technologies", "15+")

# =========================================
# ABOUT PAGE
# =========================================
elif page == "About":

    st.title("🙋 About Me")

    st.markdown(
        """
        <div class="card">
        <h3>Who Am I?</h3>
        <p>
        I am an aspiring Data Scientist passionate about AI, Machine Learning,
        Data Analytics, and creating modern applications using Streamlit.

        I enjoy solving real-world problems through data-driven solutions
        and interactive dashboards.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">
        <h3>Career Goals</h3>
        <p>
        My goal is to become a skilled Data Scientist and build impactful
        AI applications that improve user experiences and business decisions.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================
# SKILLS PAGE
# =========================================
elif page == "Skills":

    st.title("🛠️ Skills & Technologies")

    skills = [
        "Python", "Machine Learning", "Pandas", "NumPy",
        "Matplotlib", "Plotly", "Scikit-Learn", "Streamlit",
        "SQL", "Data Visualization", "Deep Learning",
        "GitHub", "Power BI", "Forecasting", "EDA"
    ]

    cols = st.columns(3)

    for i, skill in enumerate(skills):
        cols[i % 3].markdown(
            f"<div class='skill-box'>{skill}</div>",
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.subheader("📊 Skill Proficiency")

    skill_df = pd.DataFrame({
        "Skill": [
            "Python", "Machine Learning", "Data Visualization",
            "Streamlit", "SQL", "EDA"
        ],
        "Level": [90, 85, 88, 92, 75, 89]
    })

    fig = px.bar(
        skill_df,
        x="Skill",
        y="Level",
        text="Level",
        title="Skill Levels"
    )

    fig.update_layout(
        template="plotly_dark",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================
# PROJECTS PAGE
# =========================================
elif page == "Projects":

    st.title("🚀 Featured Projects")

    project1, project2 = st.columns(2)

    with project1:
        st.markdown(
            """
            <div class="card">
            <h3>📈 Apple Stock Prediction</h3>
            <p>
            Developed a Streamlit application for forecasting Apple stock prices
            using Machine Learning and visualization tools.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.link_button(
            "🔗 View GitHub Repository",
            "https://github.com/"
        )

    with project2:
        st.markdown(
            """
            <div class="card">
            <h3>✈️ Airline Clustering Analysis</h3>
            <p>
            Performed customer segmentation using clustering algorithms
            on airline customer data.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.link_button(
            "🔗 View GitHub Repository",
            "https://github.com/"
        )

    st.markdown("---")

    project3, project4 = st.columns(2)

    with project3:
        st.markdown(
            """
            <div class="card">
            <h3>📚 Book Recommendation System</h3>
            <p>
            Built a recommendation engine using collaborative filtering
            and machine learning techniques.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.link_button(
            "🔗 View GitHub Repository",
            "https://github.com/Venkatamalini/book-recommendation-system.git"
        )

    with project4:
        st.markdown(
            """
            <div class="card">
            <h3>📊 Interactive Dashboard</h3>
            <p>
            Designed interactive dashboards with charts and KPIs
            for business analytics.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.link_button(
            "🔗 View GitHub Repository",
            "https://github.com/"
        )

# =========================================
# CERTIFICATES PAGE
# =========================================
elif page == "Certificates":

    st.title("🏆 Certifications")

    certs = pd.DataFrame({
        "Certificate": [
            "Data Science Certification",
            "Python Programming",
            "Machine Learning Fundamentals",
            "SQL for Data Analytics",
            "Power BI Dashboard Development"
        ],
        "Status": [
            "Completed",
            "Completed",
            "Completed",
            "Completed",
            "Completed"
        ]
    })

    st.dataframe(certs, use_container_width=True)

# =========================================
# CONTACT PAGE
# =========================================
elif page == "Contact":

    st.title("📬 Contact Me")

    st.markdown(
        """
        <div class="card">
        <h3>Let's Connect!</h3>
        <p>
        Interested in collaborating or discussing data science opportunities?
        Feel free to connect with me.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("📧 Email: malinivenkata@example.com")
    st.write("💼 LinkedIn: linkedin.com/in/malini-venkata")
    st.write("🐙 GitHub: github.com/Venkatamalini")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")

        submit = st.form_submit_button("Send Message")

        if submit:
            st.success("✅ Your message has been submitted successfully!")

# =========================================
# MODEL SECTION
# =========================================

st.markdown("---")
st.subheader("🤖 Load Machine Learning Model (.pkl)")

uploaded_model = st.file_uploader(
    "Upload your trained .pkl model",
    type=["pkl"]
)

if uploaded_model is not None:
    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pkl') as tmp_file:
            tmp_file.write(uploaded_model.read())
            tmp_path = tmp_file.name

        # Load model using joblib
        model = joblib.load(tmp_path)

        st.success("✅ Machine Learning model loaded successfully!")
        st.write("Loaded Model Type:", type(model))

    except Exception as e:
        st.error("❌ Model compatibility error")
        st.code(str(e))

        st.info(
            """
            Fix:
            - Use same scikit-learn version used during training
            - Re-save model using joblib
            - Add correct dependencies in requirements.txt
            """
        )

# =========================================
# FOOTER
# =========================================
st.markdown("---")
st.caption("© 2026 Malini Venkata | Built with Streamlit 🚀")


 