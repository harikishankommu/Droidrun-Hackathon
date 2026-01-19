from pypdf import PdfReader
from google import genai
import json
import os

print("Resume Parser Started...")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are an expert resume parser.

Return ONLY valid JSON.
No markdown. No explanation.

Keys:
name, email, phone, education, skills, experience, projects, links
"""

def extract_text_from_pdf(path):
    reader = PdfReader(path)
    text = ""
    links = []

    for page in reader.pages:
        text += (page.extract_text() or "") + "\n"
        if "/Annots" in page:
            for annot in page["/Annots"]:
                obj = annot.get_object()
                if "/A" in obj and "/URI" in obj["/A"]:
                    links.append(obj["/A"]["/URI"])

    if links:
        text += "\nDetected URLs:\n" + "\n".join(set(links))
    return text

def parse_resume(pdf_path):
    text = extract_text_from_pdf(pdf_path)

    response = client.models.generate_content(
        model="gemini-2.5-flash",    #GEMINI 2.5
        contents=[SYSTEM_PROMPT, text]
    )

    raw = response.text.strip()
    start, end = raw.find("{"), raw.rfind("}") + 1
    return json.loads(raw[start:end])

if __name__ == "__main__":
    print(json.dumps(parse_resume("resume.pdf"), indent=2))