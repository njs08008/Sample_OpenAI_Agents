# 📊 GTM Candidate Intelligence Agents

This project demonstrates a lightweight, end-to-end pipeline for transforming unstructured candidate data into actionable insights for executive search.

It consists of two AI-powered agents:

1. **Materials Generation Agent** – Converts raw resumes into structured data and synthetic artifacts (notes, emails)  
2. **Candidate Intelligence Agent** – Evaluates candidates against a job description and ranks the top matches  

---

# 🚀 Overview

Executive search firms sit on large amounts of **unstructured data**:
- Resumes  
- Interview notes  
- Emails  
- Call transcripts  

This project simulates that environment and shows how AI can:

- Structure messy data  
- Enrich candidate profiles  
- Enable intelligent ranking and decision-making  

---

# 🧠 Architecture
PDF Resumes

↓

[Agent 1: Materials Generator]

↓

Structured JSON + Notes + Emails

↓

[Agent 2: Candidate Intelligence]

↓

Top Candidates + Strengths + Concerns


---

# 🧩 Agent 1: Materials Generation Agent

## 🎯 Purpose

Transforms raw PDF resumes into:

- Structured candidate profiles (JSON)
- Interview-style notes
- Internal email summaries  

---

## ⚙️ How it works

1. Extracts text from PDF resumes  
2. Sends content to an LLM  
3. Generates:
   - Structured JSON (skills, roles, achievements)
   - Notes (informal evaluation)
   - Email (candidate summary)

---

## 📂 Output

For each resume, the following documents are produced:

```
├── data/
│   └── {id}_resume.json
│   └── {id}_notes.json
│   └── {id}_email.json
```

---

## 💡 Key Features

- Handles multiple resumes in batch  
- Gracefully skips invalid or corrupted PDFs  
- Uses deterministic hashing (`sha256`) for consistent IDs  
- Structured outputs (no fragile string parsing)  

---

# 🧩 Agent 2: Candidate Intelligence Agent

## 🎯 Purpose

Evaluates all candidates for a given role and identifies the **top 3 fits**.

---

## ⚙️ How it works

1. Loads all candidate materials:
   - Structured resume JSON  
   - Notes  
   - Emails  

2. Combines them with a job description  

3. Uses an LLM to:
   - Rank candidates  
   - Identify strengths  
   - Highlight risks  

---

## 📂 Output

```json
{
  "position_description": "...",
  "ranked_candidates": [
    {
      "name": "Candidate Name",
      "strengths": ["...", "...", "..."],
      "concerns": ["...", "...", "..."]
    }
  ]
}
```

Saved to:

```
outputs/ranked_candidates.json
```

# 🛠️ Setup
1. Clone repo
```bash
git clone https://github.com/njs08008/Sample_OpenAI_Agents.git
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Add environment variables

Create a .env file:
```
OPENAI_API_KEY=your_api_key_here
```

# ▶️ Usage
## Step 1: Generate candidate materials

Place resume PDFs in:

```
materials-generation-agent/data/resumes/
```

Run:

```bash
python materials-generation-agent/main.py
```

This will:

- Parse PDFs
- Generate structured JSON, notes, and emails

## Step 2: Rank candidates

Update the job description in:

```
gtm-agent/data/position/position.txt
```

Run:

```bash
python materials-generation-agent/main.py
```

This will:

- Analyze all candidates
- Output top 3 matches

# ⚠️ Error Handling

The system is designed to be robust:

- Skips invalid or corrupted PDFs
- Handles empty or malformed JSON
- Logs failures without stopping execution

# 🧪 Example Use Case

Input:
- 10 candidate resumes
- Job: VP Marketing Ops (B2B SaaS)

Output:
- Top 3 candidates
- Clear strengths and concerns
- Structured JSON for downstream use

# 🔍 Design Decisions

## ✅ Structured Outputs

Uses OpenAI’s JSON response format to:
- Avoid markdown parsing issues
- Ensure reliable downstream processing

## ✅ Deterministic IDs

Uses hashlib.sha256 instead of Python’s hash() to:
- Ensure consistent IDs across runs
- Enable stable file naming

## ✅ Separation of Concerns
- Agent 1: Data generation
- Agent 2: Decision-making

This mirrors real-world data pipelines.

# 🚧 Future Improvements
- Add Pydantic validation for strict schema enforcement
- Refactor into an API
- Connect to a database rather than flat files
- Add scoring model alongside qualitative reasoning
- Incorporate call transcripts and real-time ingestion
