import os
import sys
import json
import textstat

from scraper import extract_text_from_url
from gemini_api import get_gemini_response


def analyze_article(url):
    print(f"🔍 Extracting content from: {url}")
    raw_text = extract_text_from_url(url)

    # ✅ Compute readability scores
    flesch_score = textstat.flesch_reading_ease(raw_text)
    fog_score = textstat.gunning_fog(raw_text)

    # ✨ Prepare Gemini prompt
    prompt = f"""
You're an AI documentation improvement agent.

Your job is to analyze the following technical documentation and provide improvement suggestions in four areas:
1. Readability for a marketer (explain using Flesch={flesch_score}, Fog={fog_score})
2. Structure & flow
3. Completeness & examples
4. Writing style: clarity, customer-focused tone, concise action-oriented writing (based on Microsoft style guide)

Document:
```text
{raw_text[:12000]}
```

Output format:

Readability: [Assessment + Suggestions]

Structure: [Assessment + Suggestions]

Completeness: [Assessment + Suggestions]

Style: [Assessment + Suggestions]
"""
    
    print("🧠 Sending prompt to Gemini...")
    ai_response = get_gemini_response(prompt)

    # 📦 Structure the final output
    output = {
        "url": url,
        "readability_score": {
            "Flesch": flesch_score,
            "GunningFog": fog_score
        },
        "gemini_analysis": ai_response
    }

    # 📁 Ensure output directory exists
    output_dir = "examples"
    os.makedirs(output_dir, exist_ok=True)

    # 💾 Save to JSON file
    output_path = os.path.join(output_dir, "report.json")
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"✅ Analysis saved to {output_path}")
    
    # Return the output so it can be used
    return output


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    result = analyze_article(url)
    print(json.dumps(result, indent=2))