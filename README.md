# Lazy-Imports

> [!CAUTION]
> This repository is deprecated and should no longer be used.\
> It is replaced by the friendly fork [lazy-imports](https://github.com/bachorp/lazy-imports) from [Pascal Bachor](https://github.com/bachorp).

[![Apache-2.0 License](https://img.shields.io/github/license/telekom/lazy-imports)](https://github.com/telekom/lazy-imports/blob/main/LICENSE)
[![Contributor Covenant](https://img.shields.io/badge/Code%20of%20Conduct-Contributor%20Covenant-ff69b4.svg)](https://github.com/telekom/lazy-imports/blob/main/CODE_OF_CONDUCT.md)
[![Python Version](https://img.shields.io/pypi/pyversions/lazy-imports)](https://www.python.org)
[![pypi](https://img.shields.io/pypi/v/lazy-imports.svg)](https://pypi.python.org/pypi/lazy-imports)
<br/>
[![pytest](https://github.com/telekom/lazy-imports/actions/workflows/pytest.yml/badge.svg)](https://github.com/telekom/lazy-imports/actions/workflows/pytest.yml)
[![Static Code Checks](https://github.com/telekom/lazy-imports/actions/workflows/static_checks.yml/badge.svg)](https://github.com/telekom/lazy-imports/actions/workflows/static_checks.yml)
[![GitHub issues](https://img.shields.io/github/issues-raw/telekom/lazy-imports)](https://github.com/telekom/lazy-imports/issues)

This is a Python tool to support lazy imports.
Likewise, the actual initialization of the module does not occur until usage time
to postpone `ModuleNotFoundError`s to the time of the actual usage of the module.
This is useful when using various optional dependencies which might not all be
installed or which have high load times and/or ressource consumption.

## Table of Contents

- [Maintainers](#maintainers)
- [Installation](#installation)
- [Usage & Example for LazyImporter](#usage--example-for-lazyimporter)
- [Usage & Example for try_import](#usage--example-for-try_import)
- [Support and Feedback](#support-and-feedback)
- [Reporting Security Vulnerabilities](#reporting-security-vulnerabilities)
- [Contribution](#contribution)
- [Code of Conduct](#code-of-conduct)
- [Licensing](#licensing)

## Maintainers

This project is maintained by a team of [Deutsche Telekom AG](https://www.telekom.com/).
It is based on
[`_LazyModule`](https://github.com/huggingface/transformers/blob/e218249b02465ec8b6029f201f2503b9e3b61feb/src/transformers/file_utils.py#L1945)
from [HuggingFace](https://huggingface.co/) and
[`try_import()`](https://github.com/optuna/optuna/blob/1f92d496b0c4656645384e31539e4ee74992ff55/optuna/_imports.py#L89)
from the [Optuna framework](https://optuna.readthedocs.io/).
Many thanks to HuggingFace for
[your consent](https://github.com/huggingface/transformers/issues/12861#issuecomment-886712209)
and to Optuna for
[your consent](https://github.com/optuna/optuna/issues/2776#issuecomment-874614137)
to publish it as a standalone package 🤗 ♥.

## Installation

Lazy-Imports is available at [the Python Package Index (PyPI)](https://pypi.org/project/lazy-imports/).
It can be installed with pip:

```bash
$ pip install lazy-imports
```

## Usage & Example for LazyImporter

A good and easy to understand example of how to use Lazy-Imports can be found in the
[`__init__.py` file of the HPOflow package](https://github.com/telekom/HPOflow/blob/1b26f3b86cad607dd89a31fa9135256d956948cb/hpoflow/__init__.py).
It is printed here:

```python
import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter

from hpoflow.version import __version__


_import_structure = {
    "mlflow": [
        "normalize_mlflow_entry_name",
        "normalize_mlflow_entry_names_in_dict",
        "check_repo_is_dirty",
    ],
    "optuna": ["SignificanceRepeatedTrainingPruner"],
    "optuna_mlflow": ["OptunaMLflow"],
    "optuna_transformers": ["OptunaMLflowCallback"],
    "utils": ["func_no_exception_caller"],
}

# Direct imports for type-checking
if TYPE_CHECKING:
    from hpoflow.mlflow import (  # noqa: F401
        check_repo_is_dirty,
        normalize_mlflow_entry_name,
        normalize_mlflow_entry_names_in_dict,
    )
    from hpoflow.optuna import SignificanceRepeatedTrainingPruner  # noqa: F401
    from hpoflow.optuna_mlflow import OptunaMLflow  # noqa: F401
    from hpoflow.optuna_transformers import OptunaMLflowCallback  # noqa: F401
    from hpoflow.utils import func_no_exception_caller  # noqa: F401
else:
    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        _import_structure,
        extra_objects={"__version__": __version__},
    )
```

## Usage & Example for try_import

`try_import` is a context manager that can wrap imports of optional packages to defer
exceptions. This way you don't have to import the packages every time you call a function,
but you can still import the package at the top of your module. The context manager
defers the exceptions until you actually need to use the package.
You can see an example below:

```python
from lazy_imports import try_import

with try_import() as optional_package_import:  # use try_import as a context manager
    import optional_package  # optional package that might not be installed

# other non optional functions here

def optional_function():  # optional function that uses the optional package
    optional_package_import.check()  # check if the import was ok or raise a meaningful exception

    optional_package.some_external_function()  # use the optional package here
```

## Support and Feedback

The following channels are available for discussions, feedback, and support requests:

- [open an issue in our GitHub repository](https://github.com/telekom/lazy-imports/issues/new/choose)
- [send an e-mail to our open source team](mailto:opensource@telekom.de)

## Reporting Security Vulnerabilities

This project is built with security and data privacy in mind to ensure your data is safe.
We are grateful for security researchers and users reporting a vulnerability to us, first.
To ensure that your request is handled in a timely manner and non-disclosure of vulnerabilities
can be assured, please follow the below guideline.

**Please do not report security vulnerabilities directly on GitHub.
GitHub Issues can be publicly seen and therefore would result in a direct disclosure.**

Please address questions about data privacy, security concepts,
and other media requests to the [opensource@telekom.de](mailto:opensource@telekom.de) mailbox.

## Contribution

Our commitment to open source means that we are enabling - in fact encouraging - all interested
parties to contribute and become part of our developer community.

Contribution and feedback is encouraged and always welcome. For more information about how to
contribute, as well as additional contribution information, see our
[Contribution Guidelines](https://github.com/telekom/lazy-imports/blob/main/CONTRIBUTING.md).

## Code of Conduct

This project has adopted the [Contributor Covenant](https://www.contributor-covenant.org/)
as our code of conduct. Please see the details in our
[Contributor Covenant Code of Conduct](https://github.com/telekom/lazy-imports/blob/main/CODE_OF_CONDUCT.md).
All contributors must abide by the code of conduct.

## Licensing

Copyright (c) 2021 [Philip May](https://may.la/), [Deutsche Telekom AG](https://www.telekom.com/)<br/>
Copyright (c) 2020, 2021 [The HuggingFace Team](https://huggingface.co/)<br/>
Copyright (c) 2018 Preferred Networks, Inc.

Licensed under the [Apache License, Version 2.0](https://github.com/telekom/lazy-imports/blob/main/LICENSE) (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
