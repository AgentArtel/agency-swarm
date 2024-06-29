from flask import Flask
from agency_swarm import set_openai_key, Agent, Agency

app = Flask(__name__)

# Set your OpenAI API key here
set_openai_key("YOUR_OPENAI_API_KEY")

# Define your agent
ceo = Agent(
    name="CEO",
    description="Responsible for client communication, task planning, and management.",
    instructions="You must converse with other agents to ensure complete task execution."
)

# Create your agency
agency = Agency([ceo])

@app.route("/")
def hello():
    return "Hello from Agency Swarm!"

# Run the app
if __name__ == "__main__":
    app.run()
