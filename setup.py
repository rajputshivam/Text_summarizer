import setuptools

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = ""
AUTHOR_USER_NAME = ""
SRC_REPO = ""
AUTHOR_EMAIL = ""

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email_id=AUTHOR_EMAIL,
    description="a small python package for CNN app",
    Long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issue",
    },
    package_dir = {"":"src"},
    package = setuptools.find_packages(where="src")

)
