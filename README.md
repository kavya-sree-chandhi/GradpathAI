# GradPath AI

## **Project Summary**
GradPath AI is an intelligent, AI-powered career copilot for aspiring AI/ML professionals. It acts as a mentor, custom learning path builder, and job-prep assistant.
Target users: Students, recent graduates, or working professionals aiming for AI/ML roles like Data Scientist, LLM Engineer, Computer Vision Specialist, etc.

The Core Problem:
-Students don’t know where to start in AI/ML.
-Resources are overwhelming, scattered, and not tailored.
-No clear, role-specific learning path or ongoing personalized career advice.

Solution:
-Personalized, role-specific guidance powered by LLM (GPT-4).
-Builds custom learning roadmaps for each AI/ML target role.
-Fetches live resources (courses, GitHub, YouTube, projects) tailored to user skill gaps.
-Suggests projects, mock interview questions, and tracks progress with memory.
-Conversational AI that adapts and evolves recommendations over time.

---

## **Key Features & User Flow**
   
A. Onboarding
-User selects a target role (e.g., “Data Scientist”)
-User inputs current skills, background, goals, and time commitment

B. AI Career Copilot
-GPT-4 (via LangChain) parses user intent and background
-Maps the role to required skills/steps (via role-mapping logic)
-Recommends a custom roadmap: sequential topics, courses, projects

C. Resource Aggregation
Resource Agent fetches:
-Top YouTube videos
-GitHub trending repos/projects
-Up-to-date courses (Coursera, Udemy, etc.)
-Bot presents the roadmap with direct resource links

D. Interactive Guidance
-Bot suggests project ideas and mock interview questions
-Tracks user progress (optional user login for memory)
-Adapts recommendations over time (conversation memory)

E. (Optional, for V2)
-Track learning milestones and provide mentor feedback
-Store user session history and logs for personalized long-term guidance

---
## **Tech Stack**
**Frontend:** Streamlit (for interactive, fast UI)

**Backend:** Python (LangChain for LLM orchestration)

**AI Engine:** GPT-4/OpenAI API

**APIs:** YouTube API, GitHub API, Coursera/Udemy APIs

**Data Handling:** Pandas/NumPy

**Database:** Lightweight DB or local storage for MVP (upgrade to MongoDB/Postgres for full version)

**Deployment:** Streamlit Cloud, Hugging Face Spaces, or similar

---

## 🛠️ How to Run

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/GradPath-AI.git
    cd GradPath-AI
    ```
2. **(Recommended) Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Set up environment variables and configs as needed.**
5. **Run the application:**
    ```bash
    streamlit run app.py  # or python main.py, etc
    ```

---

## 🗺️ Architecture Diagram

Below is the architecture and workflow of GradPath AI:

![GradPath AI Architecture](./Updated%20GradPath%20AI.drawio.svg)

> _If the diagram doesn't render, [view the SVG file directly here.](./Updated%20GradPath%20AI.drawio.svg)_

---
## **Architecture Overview**

**User**
Inputs: Role, skills, interests, goals

Outputs: Custom roadmap, resource links, project suggestions

**Web App Interface (Streamlit)**
UI for chat and result display

Collects user inputs and displays AI-generated outputs

**AI Agent Core Logic**
LLM Router: GPT-4 (via LangChain) handles intent parsing and context tracking

Role Agent: Maps selected role to skills and steps needed (uses static datasets like skills.json, roadmap.csv)

Resource Agent: Fetches videos, docs, and GitHub repos via APIs (YouTube, GitHub, Course APIs)

**Database / Memory**
Stores session data, user history, and logs

Used for progress tracking and personalized recommendations

**Resource APIs**
Live data from YouTube, GitHub, course providers (Coursera, Udemy, etc.)



