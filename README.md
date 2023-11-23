# q

Query PDF files in any directory with ChatGPT

## Installation

Install Python 3 https://www.python.org/downloads/

Open a terminal and install dependencies

```
pip install -r requirements.txt
./q.py ~/Downloads "Summarize Aspire's Job Description"
```

## Usage

Create an OpenAI API key https://platform.openai.com/api-keys and save it in the `OPENAI_API_KEY` environment variable

```
export OPENAI_API_KEY="your_openai_api_key"
```

Run q

```
./q.py "Summarize Aspire's Job Description"
```

q queries the current directory by default but you can query any directory you like

```
q ~/Downloads "Summarize Aspire's Job Description"
```
