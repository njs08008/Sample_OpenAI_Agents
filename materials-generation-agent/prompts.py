def build_prompt(resume_text: str) -> str:
    return f"""
You are an assistant helping an executive search firm process candidate data.
For this use case, you are receiving a resume to use in manufacturing data to help them test other downstream processes.

Given the following resume, generate:

1. A structured JSON profile true to the resume with:
   - name
   - summary
   - roles
      - company
         - company_industry
         - company_growth_stage
         - role_title
            - key_achievements
            - years_in_role
   - skills
   - education
      - institution
      - degree
      - degree_year
      - specialization

2. Interview-style notes (bullet points, informal tone).
These notes may support what is in the resume, add clarification to details, or slightly contest or contradict certain points.
Feel free to make up data as needed.

3. An internal back-and-forth email about the candidate that is 2-3 replies long with 2-3 sentences per reply.
Each reply should be directly pertinent to the previous message and have timestamps.
These emails may support what is in the resume, add clarification to details, or slightly contest or contradict certain points.
It should, however, not contradict the interview notes.

Resume:
{resume_text}

Return in this format:

RESUME_JSON:
<json>

NOTES:
<notes>

EMAIL:
<email>
"""
