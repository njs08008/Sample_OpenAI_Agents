import os
import json
from pdf_parser import extract_text_from_pdf
from agent import generate_candidate_materials
from stable_id import get_stable_id


INPUT_PATH = "data"
OUTPUT_DIR = "outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_output(name: str, content: str):
    with open(os.path.join(OUTPUT_DIR, name), "w") as f:
        if name[-4:] == 'json':
            json.dump(content, f, indent=2)
        else:
            f.write(content)


def main():
    for resume in os.listdir(INPUT_PATH):
        if not resume.lower().endswith(".pdf"):
            continue

        resume_path = os.path.join(INPUT_PATH, resume)

        print(f"Reading resume {resume}...")
        try:
            resume_text = extract_text_from_pdf(resume_path)
            if not resume_text:
                print(f"No text extracted from {filename}")
                # Continue to the next PDF
                continue
        except Exception as e:
            print(f"Failed to process {resume}: {e}")
            # Continue to the next PDF
            continue
        
        resume_id = get_stable_id(resume_text)

        print("Generating materials...")
        results = generate_candidate_materials(resume_text)

        print("Saving outputs...")
        save_output(f"{resume_id}_resume.json", results["resume_json"])
        save_output(f"{resume_id}_notes.txt", results["notes"])
        save_output(f"{resume_id}_email.txt", results["email"])

        print("Done.")


if __name__ == "__main__":
    main()
