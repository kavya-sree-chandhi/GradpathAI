﻿# GradPath AI 

**Your Personalized Career Copilot**  
An intelligent AI agent that acts as a career mentor, learning path builder, and job-prep assistant for aspiring AI/ML professionals.

---

## Overview

**GradPath AI** helps students and recent graduates navigate the overwhelming world of AI/ML careers by providing:

- Role-specific learning roadmaps (e.g., Data Scientist, LLM Engineer)
- Personalized resources (GitHub, YouTube, Coursera)
- Project ideas & mock interviews
- LLM memory to refine paths over time

> “There’s a flood of information, but no map.” — That’s what we solve.

---

## Problem Statement

Many aspiring AI/ML professionals face challenges like:

- No clear starting point or structure
- Scattered online resources
- Lack of personalization
- Generic career guidance

GradPath AI solves this by offering tailored, intelligent, and role-specific career coaching powered by LLMs.

---

## Research & Background

- AI job market growing at **35% per year** (LinkedIn 2024)
- 200,000+ students in the US interested in AI/Data Science
- Nearly 50% of learners don’t know what to learn next (StackOverflow 2023)
- Existing tools are fragmented and not personalized

---

## Key Features

- **Custom Role Selection** – Choose your target role (e.g., NLP Engineer)
- **Tailored Learning Paths** – Based on your background, goals, and time
- **Live Resource Integration** – GitHub, YouTube, Coursera & more
- **LLM Memory** – Tracks your progress and refines suggestions
- **Projects & Interview Prep** – Real-world project ideas + mock questions

---

##  Tech Stack

| Layer         | Technology                            |
|--------------|----------------------------------------|
| **Frontend**  | Streamlit                             |
| **Backend**   | Python, LangChain, OpenAI GPT-4       |
| **AI Engine** | GPT-4 + LangChain Chains with Memory  |
| **Resources** | YouTube API, GitHub Scraper, Coursera |
| **Data**      | Pandas, NumPy                         |
| **Deployment**| Streamlit Cloud / Hugging Face Spaces |

---

##  How It Works

1. **User selects a career goal**
2. AI asks for:
   - Current skill level
   - Interests
   - Time commitment
3. GPT-4 builds a **custom roadmap**
4. Recommends:
   - Courses
   - Projects
   - Mock interviews
5. Learner gets an **interactive, evolving guide** based on progress

---

## Future Enhancements

- User Login & Progress Tracking
- Feedback loops for roadmap accuracy
- Visual skill graph
- Community project submission & peer review

---

## Getting Started

> Clone the repo and install dependencies:

```bash
git clone https://github.com/kavya-sree-chandhi/GradpathAI.git
cd GradpathAI


