import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from prompts import build_prompt

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

CANDIATE_DIR = r"data/candidate"
POSITION_FILE = r"data/position/position.txt"

def load_candidate_materials():
    candidates = {}

    files = os.listdir(CANDIATE_DIR)
    for f in files:
        base = f.split("_")[0]
        if base not in candidates:
            candidates[base] = {}
        if f.endswith("_resume.json"):
            with open(os.path.join(CANDIATE_DIR, f)) as fp:
                candidates[base]["resume"] = json.load(fp)
        elif f.endswith("_notes.txt"):
            with open(os.path.join(CANDIATE_DIR, f)) as fp:
                candidates[base]["notes"] = fp.read()
        elif f.endswith("_email.txt"):
            with open(os.path.join(CANDIATE_DIR, f)) as fp:
                candidates[base]["email"] = fp.read()
    return candidates

def load_position_description():
    with open(POSITION_FILE) as f:
        position_description = f.read()
    return position_description

def rank_candidates():
    position_description = load_position_description()
    candidates = load_candidate_materials()
    prompt = build_prompt(position_description, candidates)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        response_format={"type": "json_object"}
    )

    content = response.choices[0].message.content
    top_candidates = json.loads(content)["candidates"]


    return position_description, top_candidates
