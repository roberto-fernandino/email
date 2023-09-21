from pathlib import Path


def define_template_path(instance, filename:str ) -> str:
    return Path(f"emails/{filename}")