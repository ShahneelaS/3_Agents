Travel Agent — travel-agent/README.md
# Travel Agent

The **Travel Agent** is an AI-based virtual assistant that helps users plan trips, suggest destinations, and provide travel tips.  
It uses the OpenRouter API for AI responses.

## Features
- Destination Discovery - Find perfect travel destinations
- Itinerary Planning - Create detailed day-by-day travel plans
- Flight Search - Find and compare flight options
- Hotel Recommendations - Get personalized accommodation suggestions

## Installation
1. Clone this repository:
   ```bash
   git clone <repo-url>
   cd travel-agent


2. Create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\activate  # Windows

3. Install dependencies:

pip install -r requirements.txt


4. Create a .env file in the root directory and add:

OPENROUTER_API_KEY=your_api_key_here

Run the Project
chainlit run main.py -w