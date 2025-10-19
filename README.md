# Langraph Agents

A Python project for creating AI agents using LangChain and Google Generative AI, managed with UV for fast and reliable dependency management.

## Description

This project demonstrates how to create intelligent agents using the LangChain framework with Google's Gemini model. It includes a weather tool example and is configured as a LangGraph application with proper package structure.

## Features

- AI agent powered by Google Gemini 2.5 Pro
- Custom tool integration (weather function example)
- Modular package structure with `src/` layout
- LangGraph configuration for deployment
- Environment-based configuration with `.env` support
- Development tools including Jupyter notebooks
- Fast dependency management with UV

## Prerequisites

- Python 3.13 or higher
- [UV](https://docs.astral.sh/uv/) package manager
- Google API key for Generative AI

## Installation

### 1. Install UV

If you don't have UV installed:

```bash
# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or using Homebrew
brew install uv

# Or using pip
pip install uv
```

### 2. Clone and Setup

```bash
# Clone this repository
git clone <repository-url>
cd Langraph-Agents

# Install all dependencies using UV
uv sync

# This will:
# - Create a virtual environment (.venv)
# - Install all project dependencies
# - Install development dependencies (Jupyter, LangGraph CLI, etc.)
```

### 3. Configure Environment

Create a `.env` file in the project root with your Google API key:

```bash
GOOGLE_API_KEY=your-api-key-here
```

Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

## Usage

### Running the Agent

```bash
# Using UV (recommended)
uv run python src/agents/main.py

# Or activate the virtual environment first
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows
python src/agents/main.py
```

### Using LangGraph CLI

Start the LangGraph development server:

```bash
# Using UV
uv run langgraph dev

# Or with activated environment
langgraph dev

# The server will start at http://localhost:8123
```

### Working with Jupyter Notebooks

```bash
# Start Jupyter with UV
uv run jupyter notebook notebooks/notebook.ipynb

# Or with activated environment
jupyter notebook notebooks/notebook.ipynb
```

### Managing Dependencies

```bash
# Add a new package
uv add package-name

# Add a development dependency
uv add --dev package-name

# Remove a package
uv remove package-name

# Update dependencies
uv sync

# Update all dependencies to latest versions
uv lock --upgrade
```

## Project Structure

```plaintext
Langraph-Agents/
├── .env                    # Environment variables (API keys) - not in git
├── .gitignore             # Git ignore rules
├── .python-version        # Python version specification
├── langgraph.json         # LangGraph configuration
├── pyproject.toml         # Project dependencies and metadata (UV)
├── uv.lock                # Locked dependencies (UV)
├── README.md              # This file
├── main.py                # Legacy main file
├── notebooks/             # Jupyter notebooks for development
│   └── notebook.ipynb
└── src/                   # Main source code
    ├── __init__.py
    ├── agents/            # Agent implementations
    │   ├── __init__.py
    │   └── main.py        # Main agent definition
    └── api/               # API related code (future)
        └── __init__.py
```

## Configuration Files

### `pyproject.toml`

Defines project metadata and dependencies:

```toml
[project]
name = "langraph-agents"
version = "0.1.0"
requires-python = ">=3.13"

dependencies = [
    "langchain-google-genai>=3.0.0",
    "langchain[google-genai]>=1.0.0",
    "langgraph>=1.0.0",
]

[dependency-groups]
dev = [
    "ipykernel>=7.0.1",
    "langgraph-cli[inmem]>=0.4.4",
]
```

### `langgraph.json`

LangGraph service configuration:

```json
{
    "dependencies": ["."],
    "graphs": {
        "agent": "./src/agents/main.py:agent"
    },
    "env": ".env"
}
```

### `.env`

Environment variables (create this file):

```bash
GOOGLE_API_KEY=your-api-key-here
```

## Why UV?

This project uses [UV](https://docs.astral.sh/uv/) for dependency management because:

- **Fast**: 10-100x faster than pip
- **Reliable**: Deterministic dependency resolution with `uv.lock`
- **Compatible**: Works with standard `pyproject.toml`
- **Simple**: One command (`uv sync`) to set up everything
- **Modern**: Built in Rust, designed for Python 3.7+

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Ensure dependencies are up to date: `uv sync`
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Development Tips

- **Use UV for all dependency operations** - Don't use pip directly
- **Keep `uv.lock` in version control** - Ensures everyone has the same dependencies
- **Environment variables** - Always use `.env` file (already in `.gitignore`)
- **Main code location** - Use `src/agents/main.py` (not the root `main.py`)
- **Testing locally** - Use `langgraph dev` for local development server
- **Jupyter notebooks** - Great for prototyping and testing agents interactively

## Troubleshooting

### UV not found
```bash
# Install UV first
curl -LsSf https://astral.sh/uv/install.sh | sh
# Or: brew install uv
```

### Dependencies not installing
```bash
# Clear cache and reinstall
rm -rf .venv
uv sync
```

### API key errors
```bash
# Make sure .env file exists and contains:
GOOGLE_API_KEY=your-actual-api-key
```

### LangGraph server won't start
```bash
# Make sure langgraph-cli is installed
uv add --dev "langgraph-cli[inmem]"
uv sync
```

## License

This project is open source and available under the [MIT License](LICENSE).
