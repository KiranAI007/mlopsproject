import os
from pathlib import Path

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainier.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "pyproject.toml",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.cfg",
    "setup.py",
    "template.py",
    "tox.ini",
    "experiment/experiments.ipynb"
]

for filepath in list_of_files:
    # making the file path with the system compatible like linux, windows etc...
    filepath = Path(filepath)
    # split the filedir and file from the path. filedir is the directory/ folder that we want to create.
    filedir, filename = os.path.split(filepath)
    # if the filedir is not empty then create a directory
    if filedir != "":
        # make the directory
        os.makedirs(filedir, exist_ok=True)

    # check if file path not exist othervise the size is zero
    if( not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass


