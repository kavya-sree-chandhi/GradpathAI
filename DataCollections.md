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

```json
{
  "Users": {
    "name": "String",
    "email": "String",
    "role": "String",
    "createdAt": "DateTime",
    "skills": ["String"],
    "progress": {"courses_done": "Number"}
  },
```

### Courses Collection

| Field      | Type    | Description         | Example                   |
|------------|---------|---------------------|---------------------------|
| _id        | String  | Unique course ID    | course_456                |
| title      | String  | Course name         | Intro to Machine Learning |
| description| String  | Course summary      | Covers ML basics...       |
| provider   | String  | Course platform     | Coursera                  |
| url        | String  | Course link         | https://coursera.org/...  |
| tags       | Array   | Topics              | [machine learning, python]|

```json
"Courses": {
    "title": "String",
    "description": "String",
    "provider": "String",
    "url": "String",
    "tags": ["String"]
  },
```

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

```json
 "Jobs": {
    "title": "String",
    "company": "String",
    "location": "String",
    "url": "String",
    "tags": ["String"],
    "postedDate": "DateTime"
  },
```

### Projects Collection

| Field     | Type    | Description             | Example           |
|-----------|---------|-------------------------|-------------------|
| _id       | String  | Unique project ID       | repo_321          |
| name      | String  | Repo/project name       | awesome-ml-project|
| url       | String  | GitHub link             | https://github... |
| language  | String  | Programming language    | Python            |
| stars     | Number  | GitHub stars            | 1234              |
| topics    | Array   | Repo tags               | [AI, ML]          |

```json
 "Projects": {
    "name": "String",
    "url": "String",
    "language": "String",
    "stars": "Number",
    "topics": ["String"]
  }
```
---

## 🔗 API/Data Sources

- **YouTube Data API** – [Docs](https://developers.google.com/youtube/v3)
- **GitHub API** – [Docs](https://docs.github.com/en/rest)
- **Coursera** – [Catalog](https://www.coursera.org/courses) / [Unofficial API](https://github.com/coursera-dl/coursera)
- **Udemy API** – [Docs](https://www.udemy.com/developers/instructor/)
- **LinkedIn Jobs** – [Search](https://www.linkedin.com/jobs/) / [SerpAPI](https://serpapi.com/linkedin-jobs-api)
- **arXiv** – [API](https://info.arxiv.org/help/api/index.html)
- **NewsAPI** – [Docs](https://newsapi.org/)

1. **YouTube Data API**
**Used For:**
- Fetching the best AI/ML video tutorials and explainers for the user’s learning roadmap.

## Data Collection (Videos):

```json
Copy code
{
  "title": "Intro to Deep Learning",
  "description": "A beginner's guide to deep learning concepts.",
  "channel": "3Blue1Brown",
  "publishedAt": "2023-06-20T00:00:00Z",
  "url": "https://youtube.com/watch?v=aircAruvnKk",
  "tags": ["deep learning", "neural networks"]
}
```

2. **GitHub API***
**Used For:**
- Recommending trending/open-source AI/ML projects to users for learning and hands-on practice.

## Data Collection (Projects):

```json
Copy code
{
  "name": "awesome-machine-learning",
  "description": "A curated list of awesome Machine Learning frameworks, libraries and software.",
  "owner": "josephmisiti",
  "language": "Python",
  "stars": 60000,
  "topics": ["machine learning", "deep learning"],
  "url": "https://github.com/josephmisiti/awesome-machine-learning"
}
```

3. **Coursera / Udemy APIs**

**Used For:**
- Providing the most relevant and up-to-date online courses for each user’s learning path.

## Data Collection (Courses):

```json
Copy code
{
  "title": "Machine Learning by Andrew Ng",
  "description": "A foundational course on machine learning concepts and algorithms.",
  "instructor": "Andrew Ng",
  "provider": "Coursera",
  "url": "https://coursera.org/learn/machine-learning",
  "tags": ["machine learning", "supervised learning"]
}
```

4. **LinkedIn Jobs (via SerpAPI or scraping)**

**Used For:**
- Showing real job opportunities tailored to the user’s chosen career path and progress.

## Data Collection (Jobs):

```json
Copy code
{
  "title": "AI Engineer",
  "company": "Google",
  "location": "Remote, USA",
  "postedDate": "2025-07-18T00:00:00Z",
  "description": "Join our team to build AI solutions.",
  "url": "https://linkedin.com/jobs/view/1234567890",
  "tags": ["AI", "Python", "TensorFlow"]
}
```

5. **arXiv API**
**Used For:**
- Recommending state-of-the-art research papers for advanced learners and upskilling.

## Data Collection (Papers):

``` json
Copy code
{
  "title": "Attention Is All You Need",
  "authors": ["Ashish Vaswani", "Noam Shazeer"],
  "abstract": "We propose a new simple network architecture, the Transformer.",
  "publishedAt": "2017-06-12",
  "categories": ["cs.CL", "stat.ML"],
  "url": "https://arxiv.org/abs/1706.03762"
}
```

6. **NewsAPI**
**Used For:**
- Keeping users updated with the latest news and real-world trends in AI/ML.

## Data Collection (News):

```json
Copy code
{
  "title": "The Rise of AI in Healthcare",
  "description": "How artificial intelligence is changing medical diagnostics.",
  "source": "TechCrunch",
  "author": "Jane Smith",
  "publishedAt": "2025-07-18T09:00:00Z",
  "url": "https://techcrunch.com/ai-healthcare"
}
```
---



