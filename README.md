# web-scraping-chatbott
#  Website Question Answering Chatbot using Hugging Face Mistral (Nebius)

This project is a **Python-based console chatbot** that lets users input a website URL, scrapes important content from that site, and allows them to ask questions about it using the **Mistral-Small-3.1-24B-Instruct** model from Hugging Face’s Nebius Inference API.

It combines **web scraping**, **large language models**, and **automated dependency handling** into a single, clean script that can be run directly in your terminal.

---

##  Features

- ✅ Web scraping using `BeautifulSoup`
- ✅ Title, meta description, and H1 extraction
- ✅ Visible text scraping (up to 3000 characters)
- ✅ Natural Language Question Answering using Mistral LLM
- ✅ Automatic dependency installation
- ✅ Command-line interface (console chatbot)
- ✅ Hugging Face `InferenceClient` with Nebius support

---

##  Use Cases

- Summarize the purpose of a website
- Extract key info for competitive research
- Use as a foundation for SEO tools
- Build personal research assistants
- Educational or demonstration purposes

---

##  Files

- `chatbot_scraper.py` – Main Python script that contains scraping, chatbot logic, and API integration

---

##  Setup Instructions

### Prerequisites

- Python 3.8 or newer
- A Hugging Face account and API key (with Nebius access)

>  Note: The script automatically installs all necessary packages (like `requests`, `beautifulsoup4`, and `huggingface_hub`) if they’re not already installed.

---

### ▶ How to Run the Script

1. **Download** the file: `chatbot_scraper.py`

2. **Open your terminal** (Command Prompt or VS Code Terminal)

3. **Run the script using:**

```bash
python -u "path_to/chatbot_scraper.py"
