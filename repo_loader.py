import os
import shutil
from git import Repo

def clone_repo(url):

    repo_path = "repos/project"

    if os.path.exists(repo_path):
        shutil.rmtree(repo_path)

    if os.path.exists("vectorstore"):
        shutil.rmtree("vectorstore")

    Repo.clone_from(
        url,
        repo_path
    )

    print("Repository cloned!")

def load_files(path):

    documents = []

    for root, dirs, files in os.walk(path):

        for file in files:

            SUPPORTED_EXTENSIONS = (
                ".py",
                ".ipynb",
                ".md",
                ".txt",
                ".json",
                ".yaml",
                ".yml",
                ".js",
                ".ts",
                ".html",
                ".css"
            )

            if file.endswith(SUPPORTED_EXTENSIONS):

                filepath = os.path.join(root, file)

                with open(
                    filepath,
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    documents.append(
                        {
                            "filename": file,
                            "content": f.read()
                        }
                    )

    return documents