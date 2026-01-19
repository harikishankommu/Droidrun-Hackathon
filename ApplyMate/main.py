import json
from agent import apply_linkedin

if __name__ == "__main__":
    print("Loading cached resume...")

    with open("resume_data.json") as f:
        data = json.load(f)

    print("Step 2: Starting DroidRun Agent...")
    apply_linkedin(data)