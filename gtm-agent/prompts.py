import json

def build_prompt(position_description: str, candidates: dict) -> str:
    return f"""
You are an executive search assistant AI.

Given a job description and candidate materials, rank the top 3 candidates.  
For each candidate, provide:
- Candidate name (from resume JSON, 'name' field)
- Top 3 reasons they are a good fit
- Top 3 areas of concern

Make sure each reason they are a good or bad fit explicitly ties back to the job description.

Job description:
{position_description}

Candidate materials:
{json.dumps(candidates, indent=2)}

Return JSON exactly in this format:
{{"candidates":
  [
    {{
      "rank": integer_rank,
      "name": "Candidate Name",
      "strengths": ["reason1", "reason2", "reason3"],
      "concerns": ["concern1", "concern2", "concern3"]
    }}
  ]
}}
"""
