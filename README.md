# Research Assistant with LangChain

## Overview
This project is a simple research assistant powered by LangChain and multiple LLMs (GPT-4o-mini, DeepSeek, and Anthropic). It enables users to query for research topics, fetch relevant information using search tools, and save structured outputs to a text file.

## Features
- Uses multiple language models for research generation.
- Integrates Wikipedia and DuckDuckGo for fetching information.
- Saves research output in a structured format.
- Implements LangChain's tool calling agent for better research execution.

## Technologies Used
- **LangChain** (for tool execution and agent setup)
- **OpenAI GPT-4o-mini** (primary model)
- **DeepSeek Chat** (alternative LLM)
- **Anthropic Claude** (alternative LLM)
- **DuckDuckGo Search** (for web-based research)
- **Wikipedia API** (for structured knowledge retrieval)
- **Python** (core implementation)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/research-assistant.git
   cd research-assistant
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file and add your API keys for OpenAI, DeepSeek, and Anthropic if needed.
   
4. Run the program:
   ```sh
   python main.py
   ```

## Usage
- When prompted, enter a research topic.
- The assistant will search for relevant information using Wikipedia and DuckDuckGo.
- The structured research response will be printed and saved to `research_output.txt`.

## File Structure
```
├── main.py        # Core script running the research assistant
├── tools.py       # Contains research tools (search, Wikipedia, save function)
├── requirements.txt # Dependencies
├── .env           # API keys (ignored in git)
└── research_output.txt # Saved research results
```

## Future Improvements
- Add support for more LLMs (e.g., Gemini, Mistral AI).
- Improve response formatting for better readability.
- Implement a front-end interface for user interaction.
