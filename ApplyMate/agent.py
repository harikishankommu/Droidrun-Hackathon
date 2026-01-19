import json
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

def run_agent(task: str):
    print("Launching DroidRun Agent...\n")
    
    env = os.environ.copy()
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not found in .env file.")
        return

    cmd = ["droidrun", "run", "-p", "GoogleGenAI", "-m", "gemini-2.5-flash", "--steps", "100", task]
    
    subprocess.run(cmd, env=env)

def apply_linkedin(resume):
    task = f"""
Open the LinkedIn app.
Search for Software Developer jobs.
Filter to Jobs.
Filter to Easy Apply only.
Open the first relevant job.
Start filling the application.
If a question is asked outside of my resume information, Take it as a NO or 0.
Use this resume data to fill forms:
{json.dumps(resume, indent=2)}
Upload the latest resume from device.
STOP BEFORE SUBMITTING.
"""
    run_agent(task.strip())