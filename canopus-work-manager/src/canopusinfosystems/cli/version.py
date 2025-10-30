import importlib.metadata


def get_crewai_version() -> str:
    """Get the version number of Canopus Infosystems running the CLI"""
    return importlib.metadata.version("canopusinfosystems")
