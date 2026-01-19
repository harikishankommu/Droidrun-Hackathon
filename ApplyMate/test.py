import os
from mobilerun import Mobilerun

client = Mobilerun(
    api_key=os.environ.get("MOBILERUN_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.tasks.run(
    llm_model="openai/gpt-5.1",
    task="x",
)
print(response.id)