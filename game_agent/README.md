Game Agent — game_agent/README.md
# Game Agent

The **Game Agent** is an AI-based game master that interacts with players, narrates storylines, and manages game progress.  
It is powered by the OpenRouter API for AI-driven storytelling.

# Features
- Dynamic Storytelling - AI-generated narrative with branching storylines
- Combat System - Turn-based combat with dice mechanics
- Item Management - Collect and use items throughout the adventure
- Multiple AI Agents - Specialized agents for narration, combat, and rewards

## Installation
1. Clone this repository:
   ```bash
   git clone <repo-url>
   cd game_agent


2. Create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\activate  # Windows

3. Install dependencies:

pip install -r requirements.txt


4. Create a .env file in the root directory and add:

OPENROUTER_API_KEY=your_api_key_here

Run the Project
chainlit run main.py -w