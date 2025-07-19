# Data Collection:

For GradPath AI, we need to keep track of:
- Users (students, mentors)
- Courses (learning resources)
-Jobs (job opportunities)
- Projects (GitHub repos, etc.)

### Users Collection

| Field     | Type    | Description             | Example           |
|-----------|---------|-------------------------|-------------------|
| _id       | String  | Unique user ID          | user_123          |
| name      | String  | Full name               | Kavya Chandhi     |
| email     | String  | Email address           | kavya@gmail.com   |
| role      | String  | student/mentor/admin    | student           |
| createdAt | Date    | When created            | 2025-07-19        |
| skills    | Array   | List of skills          | [Python, AI]      |
| progress  | Object  | Learning progress       | {courses_done: 2} |

'''bash
{
  "Users": {
    "name": "String",
    "email": "String",
    "role": "String",
    "createdAt": "DateTime",
    "skills": ["String"],
    "progress": {"courses_done": "Number"}
  },
'''

### Courses Collection

| Field      | Type    | Description         | Example                   |
|------------|---------|---------------------|---------------------------|
| _id        | String  | Unique course ID    | course_456                |
| title      | String  | Course name         | Intro to Machine Learning |
| description| String  | Course summary      | Covers ML basics...       |
| provider   | String  | Course platform     | Coursera                  |
| url        | String  | Course link         | https://coursera.org/...  |
| tags       | Array   | Topics              | [machine learning, python]|

### Jobs Collection

| Field      | Type    | Description         | Example                   |
|------------|---------|---------------------|---------------------------|
| _id        | String  | Unique job ID       | job_789                   |
| title      | String  | Job title           | AI Engineer               |
| company    | String  | Company name        | Google                    |
| location   | String  | Job location        | Remote                    |
| url        | String  | Link to job post    | https://linkedin.com/...  |
| tags       | Array   | Job skills/keywords | [AI, Python]              |
| postedDate | Date    | Date posted         | 2025-07-18                |

### Projects Collection

| Field     | Type    | Description             | Example           |
|-----------|---------|-------------------------|-------------------|
| _id       | String  | Unique project ID       | repo_321          |
| name      | String  | Repo/project name       | awesome-ml-project|
| url       | String  | GitHub link             | https://github... |
| language  | String  | Programming language    | Python            |
| stars     | Number  | GitHub stars            | 1234              |
| topics    | Array   | Repo tags               | [AI, ML]          |

---

## 🔗 API/Data Sources

- **YouTube Data API** – [Docs](https://developers.google.com/youtube/v3)
- **GitHub API** – [Docs](https://docs.github.com/en/rest)
- **Coursera** – [Catalog](https://www.coursera.org/courses) / [Unofficial API](https://github.com/coursera-dl/coursera)
- **Udemy API** – [Docs](https://www.udemy.com/developers/instructor/)
- **LinkedIn Jobs** – [Search](https://www.linkedin.com/jobs/) / [SerpAPI](https://serpapi.com/linkedin-jobs-api)
- **arXiv** – [API](https://info.arxiv.org/help/api/index.html)
- **NewsAPI** – [Docs](https://newsapi.org/)

---


