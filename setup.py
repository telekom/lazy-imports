# Copyright (c) 2021 Philip May, Deutsche Telekom AG
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Build script for setuptools."""

import os
from typing import List

import setuptools


project_name = "lazy_imports"
source_code = "https://github.com/telekom/lazy-imports"
keywords = "import imports lazy"
install_requires: List[str] = []
extras_require = {
    "checking": [
        "black",
        "flake8",
        "isort",
        "mdformat",
        "pydocstyle",
        "mypy",
        "pylint",
        "pylintfileheader",
    ],
    "optional": [],
    "testing": ["pytest"],
    # "doc": ["sphinx", "sphinx_rtd_theme", "myst_parser", "sphinx_copybutton"],
}


def get_version():
    """Read version from ``version.py``."""
    version_filepath = os.path.join(os.path.dirname(__file__), project_name, "version.py")
    with open(version_filepath) as f:
        for line in f:
            if line.startswith("__version__"):
                return line.strip().split()[-1][1:-1]
    assert False


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name=project_name,
    version=get_version(),
    maintainer="Philip May",
    author="Philip May",
    author_email="philip.may@t-systems.com",
    description="Tool to support lazy imports",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=source_code,
    project_urls={
        "Bug Tracker": source_code + "/issues",
        # "Documentation": "https://telekom.github.io/lazy-imports/",
        "Source Code": source_code,
        "Contributing": source_code + "/blob/main/CONTRIBUTING.md",
        "Code of Conduct": source_code + "/blob/main/CODE_OF_CONDUCT.md",
    },
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=install_requires,
    extras_require=extras_require,
    keywords=keywords,
    classifiers=[
        "Development Status :: 3 - Alpha",
        # "Development Status :: 4 - Beta",
        # "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
    ],
)
