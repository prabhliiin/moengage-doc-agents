# 📄 MoEngage Documentation Analyzer & Rewriter (Agents 1 & 2)

  This project includes two AI-powered agents that analyze and improve the quality of technical documentation:

- Agent 1 (Analyzer): Extracts a documentation article from a URL, evaluates its readability, structure, completeness, and style using Gemini API, and generates actionable improvement suggestions.
- Agent 2 (Rewriter): Takes Agent 1’s suggestions and rewrites the original article with improved readability, structure, examples, and a customer-friendly style.


## How to Run the Project:

### 1. Clone the Repository
``` bash
git clone https://github.com/prabhliiin/moengage-doc-agents.git
cd moengage-doc-agents
```

### 2. Install Dependencies
Install required Python packages:

``` bash
pip install -r requirements.txt
```
### 3. Add Your API Key
-Create a .env file in the project root:
```bash
touch .env
```
-Add your Google Gemini API key:
```env
GOOGLE_API_KEY=your-gemini-api-key-here
```
(This file is ignored via .gitignore for security reasons.)

### 4. Run the code

▶️ Agent 1 - Analyze a Documentation Page
(replace this example url with the url you got)
```bash
python agent1_analyzer.py https://docs.moengage.com/docs/example-page
```
-Extracts content

-Computes Flesch and Gunning Fog readability scores

-Sends a prompt to Gemini

-Saves analysis to examples/report.json

✍️ Agent 2 - Rewrite the Article Using Analysis
(replace this example url with the url you got)
```bash
python agent2_rewriter.py https://docs.moengage.com/docs/example-page 
```
-Loads suggestions from examples/report.json
-Sends rewrite prompt to Gemini
-Saves revised article to examples/revised.md



## 📁 Folder Structure
.AI-Doc-Agent
├── agent1_analyzer.py       # Agent 1: Analyzes documentation
├── agent2_rewriter.py       # Agent 2: Rewrites based on feedback
├── scraper.py               # Utility to extract text from URLs
├── gemini_api.py            # Handles API requests to Gemini
├── .env                     # NOT COMMITTED - contains API key
├── .gitignore               # Ignores .env and example outputs
├── examples/                # Output folder (analysis + rewritten file)
│   ├── report.json
│   └── revised.md
└── README.md                # You're here
└── Output files             # Two example outputs for twp example url that i used.
    └── report(json).txt
    └── revised(md).txt

##📎 Assumptions Made
  MoEngage documentation pages are accessible without login.
  Markdown format is appropriate for rewritten content.
  The first 10,000–12,000 characters of content are sufficient for analysis and rewriting due to LLM input limits.

##⚙️ Design Choices
  Modular structure: Agents are split into distinct files.
  LLM prompt engineering: Prompts are clearly scoped for structured feedback and rewriting.
  Text extraction: We use BeautifulSoup + markdownify for clean and readable input.


##❓Challenges & How I Handled Them

  Gemini API key management:	Used .env and python-dotenv to keep keys safe
  Large document input limit:	Trimmed to first 10,000–12,000 characters
  Maintaining markdown output:	Rewriter prompt explicitly requests Markdown formatting

##📊 Example Output
  You can find output from Agent 1 for two URLs under the examples/ folder:

  examples/report.json – analysis of the first URL
  examples/revised.md – rewritten article using Agent 2

  To demonstrate results for two MoEngage URLs, you may upload two separate files like:
    examples/report1.json
    examples/report2.json


##✅ Evaluation Checklist
 Functional Agent 1 with clear, structured suggestions
 Bonus: Fully working Agent 2 with rewritten output
 Secure API key handling via .env
 Clean and maintainable Python code
 Example outputs provided
 Clear documentation and instructions

 
##Feel free to reach out 'prabhleenkaur13130@gmail.com' if you need help running the project or evaluating the agents.
