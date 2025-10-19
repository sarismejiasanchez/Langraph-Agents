# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Development Setup

### Environment Setup
```bash
# This project uses UV for dependency management
# Install UV if not already installed:
# curl -LsSf https://astral.sh/uv/install.sh | sh
# or: brew install uv

# Install all dependencies and create virtual environment
uv sync

# Activate the virtual environment (optional - uv run handles this)
source .venv/bin/activate
```

### Environment Variables
Set up Google API credentials in `.env` file:
```bash
# Create .env file with your API key
echo "GOOGLE_API_KEY=your-api-key-here" > .env
```

Or export manually:
```bash
export GOOGLE_API_KEY="your-api-key-here"
```

## Common Development Commands

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

### Running the Application
```bash
# Run the main agent application (using UV)
uv run python src/agents/main.py

# Or with activated virtual environment
python src/agents/main.py
```

### LangGraph Development Server
```bash
# Run LangGraph API server in development mode (using UV)
uv run langgraph dev

# Launch LangGraph API server
uv run langgraph up

# Build LangGraph API server Docker image
uv run langgraph build
```

### Working with Jupyter Notebooks
```bash
# Start Jupyter notebook
uv run jupyter notebook notebooks/notebook.ipynb
```

### Creating New Projects
```bash
# Create a new LangGraph project from template
uv run langgraph new
```

## Architecture Overview

This is a LangGraph-based AI agent project using Google's Gemini model, managed with UV package manager. The architecture consists of:

- **src/agents/main.py**: Core agent definition with custom tools
- **langgraph.json**: LangGraph configuration defining the agent graph location and environment file
- **pyproject.toml**: UV-managed dependencies and project metadata
- **uv.lock**: Locked dependency versions for reproducible builds
- **Agent Pattern**: Uses `create_agent()` from LangChain with custom tools integration

### Key Components

1. **Agent Definition**: Located in `src/agents/main.py:agent` - a simple agent created with `create_agent()`
2. **Custom Tools**: Weather function example showing how to integrate custom functionality
3. **Model Integration**: Uses Google Gemini 2.5 Pro via `ChatGoogleGenerativeAI`
4. **Configuration**: LangGraph JSON config points to the main agent and uses `.env` for environment variables
5. **Dependency Management**: UV handles all package installation and version locking

### Tool Architecture

- Tools are defined as regular Python functions with docstrings
- Tools are passed to `create_agent()` in a list
- The agent automatically handles tool calling and response formatting

### State Management

The `.langgraph_api/` directory contains checkpoint and operation state files that are automatically managed by the LangGraph runtime (gitignored).

## Project Structure Notes

- This uses a modular `src/` layout for better organization
- **UV manages dependencies** via `pyproject.toml` and `uv.lock`
- The virtual environment (`.venv/`) is created by `uv sync`
- Configuration is environment-based using `.env` file (referenced in `langgraph.json`)
- `.python-version` file specifies Python 3.13+ requirement
- Development dependencies (Jupyter, LangGraph CLI) are in `[dependency-groups]`
- No test framework is currently set up

## UV-Specific Notes

- Always use `uv run <command>` to run commands in the project environment
- `uv.lock` is committed to git for reproducible builds
- `pyproject.toml` defines dependencies (UV standard format)
- Use `uv add` to add packages
- Virtual environment is automatically managed by UV
