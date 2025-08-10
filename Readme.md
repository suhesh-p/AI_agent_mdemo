This project is an AI Agent built using Python and Django.
It allows users to enter a query (such as a topic or keyword) and get intelligent, relevant responses using the OpenAI API.
🚀 Features

    Accepts user queries via a web interface.

    Uses OpenAI GPT for natural language responses.

    Easy to deploy and run locally.

    Secure API key management using .env file.

    ai_agent/
│-- ai_agent/        # Main Django project folder
│-- templates/       # HTML templates
│-- static/          # CSS, JS, Images
│-- .env             # Environment variables (DO NOT COMMIT)
│-- requirements.txt # Python dependencies
│-- manage.py        # Django management script

    Clone the repository

git clone https://github.com/your-username/AI_agent_mdemo.git
cd AI_agent_mdemo

    Create and activate a virtual environment

python3 -m venv .venv
source .venv/bin/activate

    Install dependencies

pip install -r requirements.txt

    Create .env file

OPENAI_API_KEY=your_openai_key_here
DJANGO_SECRET_KEY=your_django_secret_here
DEBUG=1

    Run the development server

python manage.py runserver

Screenshot


