import os
from pathlib import Path
from typing import Union
from dotenv import load_dotenv

def load_env_vars(root_dir: Union[str, Path]) -> dict:
    """
    Load enviornment variables from .env.default and .env fles.
    Args:
        root_dir: Root directory of the .evn files.

    Returns:
        Dictionary with the environment variables.
    """

    if isinstance(root_dir, str):
        root_dir = Path(root_dir)

    load_dotenv(dotenv_path=root_dir / ".env.default")
    load_dotenv(dotenv_path=root_dir / ".env", override=True)

    return dict(os.environ)

def get_root_dir(default_value: str = "./My_repo/7-steps-MLOps-Framework") -> Path:
    """
    Get the root directory of the project.
    Args: 
        default_value: Default value to use if the environment variable is not set.
    Returns:
        Path to the root directory of the project.        
    """

    return Path(os.getenv("ML_PIPELINE_ROOT_DIR", default_value))

ML_PEIPELINE_ROOT_DIR = get_root_dir()
OUTPUT_DIR =  ML_PEIPELINE_ROOT_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SETTINGS = load_env_vars(root_dir=ML_PEIPELINE_ROOT_DIR)
