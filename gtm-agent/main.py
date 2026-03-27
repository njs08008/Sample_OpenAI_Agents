import os
import json
from agent import rank_candidates
from stable_id import get_stable_id

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_output(name: str, content: str):
    with open(os.path.join(OUTPUT_DIR, name), "w") as f:
        f.write(content.strip())


def main():
    position_description, top_candidates = rank_candidates()

    # Print results to console
    print("Top candidates:")
    for c in top_candidates:
        print(f"Rank: {c['rank']}")
        print(f"Name: {c['name']}")
        print("Strengths:", c.get("strengths"))
        print("Concerns:", c.get("concerns"))
        print("---")

    # Save results + job description to outputs folder
    position_description_hash = get_stable_id(position_description)
    output_file = os.path.join(OUTPUT_DIR, f"{position_description_hash}_ranked_candidates.json")
    with open(output_file, "w") as f:
        json.dump(
            {
                "position_description": position_description,
                "top_candidates": top_candidates
            },
            f,
            indent=2
        )

    print(f"Results saved to {output_file}")


if __name__ == "__main__":
    main()
