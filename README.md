# Langraph Agents

A Python project for creating AI agents using LangChain and Google Generative AI.

## Description

This project demonstrates how to create intelligent agents using LangChain framework with Google's Gemini model. The example includes a weather tool that can be used by the agent to provide weather information for different cities.

## Features

- AI agent powered by Google Gemini 2.5 Pro
- Custom tool integration (weather function)
- Simple and extensible architecture

## Prerequisites

- Python 3.7+
- Google API credentials for Generative AI

## Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd Langraph-Agents
```

2. Install the required dependencies:

```bash
# Install LangGraph (pre-release version)
pip install --pre -U langgraph

# Install LangChain (pre-release version)  
pip install --pre -U langchain

# Install LangChain with Google Generative AI support
pip install -U "langchain[google-genai]" langchain-google-genai

# Install LangGraph CLI with in-memory support
pip install -U "langgraph-cli[inmem]"
```

3. Set up your Google API credentials:

- Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
- Set the environment variable:

```bash
export GOOGLE_API_KEY="your-api-key-here"
```

## Usage

Run the main script:
```bash
python main.py
```

## Project Structure

```
Langraph-Agents/
├── main.py          # Main application file
├── README.md        # Project documentation
├── .gitignore       # Git ignore rules
└── langgraph.json   # LangGraph configuration
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).