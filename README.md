# 🎯 AI-Based Competency Mapping for College Graduates

An intelligent tool designed to help college graduates assess their job readiness for various career roles by identifying skill gaps through AI-driven analysis. This system provides personalized learning recommendations based on performance in a multi-level MCQ assessment.

---

## 📌 Key Features

- ✅ MCQ-based skill assessment across 3 difficulty levels
- 🧠 Predicts skill levels using an ML classification model
- 📉 Automatically detects weak areas and skill gaps
- 📊 Calculates a readiness score out of 100
- 📚 Suggests curated online courses to improve specific skills
- 🎯 Supports multiple roles:
  - Data Analyst
  - Software Developer
  - UI/UX Designer
  - ...and more

---

## 🧠 How It Works

1. **User Profile**: Enter basic details and choose a target job role.
2. **Skill Assessment**: Answer MCQs across key competencies relevant to that role.
3. **Prediction Engine**:
   - Uses a machine learning model to evaluate skill proficiency.
4. **Results Displayed**:
   - Role-specific **skill report**
   - **Readiness Score** out of 100
   - Identified **weak skills**
   - Personalized **learning plan** with resource links

---

## 🛠️ Technologies Used

| Component     | Stack/Library                          |
|---------------|-----------------------------------------|
| Frontend      | Streamlit (Python Web UI)               |
| Backend       | Python logic for evaluation and scoring |
| ML Model      | Scikit-learn, joblib                    |
| Data Source   | Custom MCQs mapped to role competencies |

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/your-username/AI-Competency-Mapping.git
cd AI-Competency-Mapping

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install streamlit scikit-learn pandas joblib

# Run the app
streamlit run app.py
