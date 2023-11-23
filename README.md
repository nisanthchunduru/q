# q

Query PDF files in any directory with ChatGPT

## Installation

Install Python 3 https://www.python.org/downloads/

Open a terminal

Clone the repo

```
git clone git@github.com:nisanthchunduru/q.git
```

Visit the `q` directory

```
cd q
```

Install dependencies

```
pip install -r requirements.txt
```

## Usage

Create an OpenAI API key https://platform.openai.com/api-keys and save it in the `OPENAI_API_KEY` environment variable

```
export OPENAI_API_KEY="your_openai_api_key"
```

If you're on a Windows machine, use the `set` command

```
set OPENAI_API_KEY=your_openai_api_key
```

Run q

```
python q.py "Summarize Aspire's Job Description"
```

```
❯ python q.py "Summarize Aspire's Job Description"
Aspire is looking for a Senior Vue.js Developer with 4-8 years of experience to join their team. The developer will be responsible for developing, recording, and maintaining cutting-edge Vue.js web applications with a mobile-first mindset. They will collaborate with the UX team to build innovative applications and work with backend developers to consume REST API data services. The developer will lead the entire web application development lifecycle, document the development process, and coordinate with co-developers and project managers. Strong knowledge of JavaScript, CSS, and RESTful API design is required, and experience with unit testing and Vue.js is preferred. Code quality, code review, and problem-solving skills are important. Familiarity with agile methodologies and experience in start-ups or top tech companies is a plus.
```

q queries the current directory by default but you can query any directory you like

```
python q.py /Users/nisanth/Downloads "Summarize Aspire's Job Description"
```
