Career Agent — career_agent/README.md
# Career Agent

The **Career Agent** is an AI-powered assistant that provides personalized career guidance and planning using the OpenRouter API.  
It helps users explore career paths, skills, and opportunities interactively.

## Features
- Career Guidance - Discover suitable career paths based on interests and skills
- Skill Development - Get personalized learning roadmaps for career advancement
- Job Search - Find relevant job opportunities in chosen fields
- Interactive Planning - Step-by-step career development guidance

## Installation
1. Clone this repository:
   ```bash
   git clone <repo-url>
   cd career_agent


2. Create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\activate  # Windows


3. Install dependencies:

pip install -r requirements.txt


4. Create a .env file in the root directory and add:

OPENROUTER_API_KEY=your_api_key_here

Run the Project
chainlit run main.py -w