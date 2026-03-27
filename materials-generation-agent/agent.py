import os
import json
import re
from dotenv import load_dotenv
from openai import OpenAI
from prompts import build_prompt


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_candidate_materials(resume_text: str) -> dict:
    prompt = build_prompt(resume_text)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    content = parse_output(response.choices[0].message.content)
    return content


def parse_output(text: str) -> dict:
    sections = {
        "resume_json": "",
        "notes": "",
        "email": ""
    }

    current = None

    for line in text.split("\n"):
        if "RESUME_JSON" in line:
            current = "resume_json"
            continue
        elif "NOTES" in line:
            current = "notes"
            continue
        elif "EMAIL" in line:
            current = "email"
            continue

        if current:
            sections[current] += line + "\n"

    sections["resume_json"] = load_json_from_markdown(sections["resume_json"])

    return sections


def load_json_from_markdown(text: str) -> dict:
    """
    Extracts JSON from a string that may be wrapped in ``` or ```json fences.
    """

    # Remove ```json ... ``` or ``` ... ```
    pattern = r"```(?:json)?\s*(.*?)\s*```"
    match = re.search(pattern, text, re.DOTALL)

    if match:
        json_str = match.group(1)
    else:
        json_str = text  # assume it's already raw JSON

    return json.loads(json_str)