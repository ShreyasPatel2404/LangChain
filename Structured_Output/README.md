# LangChain Structured Output Demo

This repository demonstrates various techniques for parsing and extracting structured outputs from Large Language Models (LLMs) using LangChain. It showcases parser strategies with both Hugging Face Hub (Gemma-2) and OpenAI models, featuring:

- **Pydantic Output Parsers**: Validate structured models dynamically.
- **JSON & Structured Output Parsers**: Standard JSON parsing using defined response schemas.
- **`with_structured_output` API**: Modern LangChain APIs using Pydantic, JSON Schema, and TypedDict structures.
- **String Output Parsers**: Chaining prompts with string-only output processors.

---

## 🛠️ Project Structure

- `pydantic_demo.py` & `typeddict_demo.py`: Basic demonstration of parsing data natively using Pydantic and TypedDict.
- `jsonoutputparser.py`: Generates custom JSON outputs using HuggingFace.
- `pydanticoutputparser.py`: Generates outputs mapped to Pydantic objects using HuggingFace.
- `structuredoutputparser.py`: Parses schemas using LangChain's `StructuredOutputParser`.
- `stroutputparser.py` & `stroutputparser1.py`: Basic prompt chaining and summary parsing.
- `with_structured_output_*.py`: Uses the recommended `.with_structured_output()` API for reliable key-value predictions.

---

## 🛡️ Security Best Practices

> [!IMPORTANT]
> **API Keys Security Alert**: 
> Never commit your `.env` file containing access tokens to GitHub. The `.gitignore` file in this repository is preconfigured to prevent `.env` from being tracked or pushed.

### Setup Instructions

1. **Clone and Navigate**:
   ```bash
   git clone https://github.com/ShreyasPatel2404/LangChain.git
   cd LANG_Structured_Output
   ```

2. **Environment Setup**:
   Create a virtual environment (optional but recommended) and install dependencies:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # On Windows
   source .venv/bin/activate # On macOS/Linux
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Copy `.env.example` to `.env` and fill in your keys:
   ```bash
   cp .env.example .env
   ```
   Add your keys to the `.env` file:
   ```env
   HUGGINGFACEHUB_ACCESS_TOKEN="your-hf-token"
   OPENAI_API_KEY="your-openai-api-key"
   ```

---

## 🚀 Running the Examples

Run any demo script using Python:
```bash
python pydantic_demo.py
python jsonoutputparser.py
```
