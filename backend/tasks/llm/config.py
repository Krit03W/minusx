"""LLM configuration constants for task orchestration."""

import os

# Model configurations
DEFAULT_MODEL = "gpt-4o"
ANALYST_V2_MODEL = "gemini/gemini-2.5-flash"

# Token and step limits
MAX_TOKENS = 4000
MAX_STEPS_LOWER_LEVEL = 35

# Debug flags
DEBUG_DURATION = os.environ.get('DEBUG_DURATION', "False").lower() == 'true'
