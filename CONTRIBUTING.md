# Contributing

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Reporting Bugs and Issues](#reporting-bugs-and-issues)
- [Engaging in our Project](#engaging-in-our-project)
- [Pull Request Checklist](#pull-request-checklist)
- [Contributing Code](#contributing-code)
- [Contributing Documentation](#contributing-documentation)
- [Testing, linting and formatting](#testing-linting-and-formatting)
- [Style Guidelines](#style-guidelines)
- [Code Owners](#code-owners)

## Code of Conduct

All members of the project community must abide by the
[Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). Only by respecting each other can we
develop a productive and collaborative community. Instances of abusive, harassing, or otherwise
unacceptable behavior may be reported by contacting
[opensource@telekom.de](mailto:opensource@telekom.de) and/or a [code owner](#code-owners).

We appreciate your courtesy of avoiding political questions here. Issues that are not related to
the project itself will be closed by our community managers.

## Reporting Bugs and Issues

- We use GitHub issues to track bugs and enhancement requests.
- Please provide as much context as possible when you report a bug and open an issue.
- Ensure the bug was not already reported by searching on GitHub under Issues.
- The information you provide must be comprehensive enough to reproduce
  that issue for the assignee.

## Engaging in our Project

- If you have a trivial fix or improvement, plese go ahead and create a pull request.
- A general guide to pull requests is here:
  [About pull requests](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
- If you want you can address (with `@...`) a suitable [code owner](#code-owners) of this
  repository.
- If you plan to do something more involved, please open an issue to start a discussion with us.
- Relevant coding [style guidelines](#style-guidelines) are available in this document.
- Should you wish to work on an issue, please claim it first by commenting
  on the GitHub issue that you want to work on. This is to prevent duplicated
  efforts from other contributors on the same issue.
- If you have questions about one of the issues, please comment on them,
  and one of the maintainers will clarify.
- We kindly ask you to follow the [Pull Request Checklist](#Pull-Request-Checklist)
  to ensure reviews can happen accordingly.

## Pull Request Checklist

- Branch from the master branch and, if needed, rebase to the current master branch
  before submitting your pull request. You may be asked to rebase your changes if your
  branch doesn't merge cleanly with master.
- Commits should be as small as possible while ensuring that each commit is correct
  independently (i.e., each commit should work and pass tests).
- Test your changes as thoroughly as possible before you commit them. Preferably,
  automate your test by unit/integration tests. If tested manually, provide information
  about the test scope in the PR description (e.g. “Test passed: Upgrade version from
  0.42 to 0.42.23.”).
- To differentiate your PR from PRs ready to be merged and to avoid duplicated work,
  please prefix the title with \[WIP\].
- If your pull request is not getting reviewed, or you need a specific person to review it,
  you can @-reply a [code owner](#code-owners) asking for a review in the pull request.
- Post review:
  - If a review requires you to change your commit(s), please test the changes again.
  - Amend the affected commit(s) and force push onto your branch.
  - Set respective comments in your GitHub review to resolved.
  - Create a general PR comment to notify the reviewers that your amendments are ready for
    another round of review.

## Contributing Code

You are welcome to contribute code in order to fix a bug or to implement a new feature.
The following rules governs code contributions:

- Contributions must be licensed under the [license of this project](LICENSE).
- Newly created files must be opened by the following file header and a
  blank line.

```python
# Copyright (c) <year> <your_name>[, <your_organization>]
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

```

## Contributing Documentation

You are welcome to contribute documentation to the project.
The following rule governs documentation contributions:

- Contributions must be licensed under the [license of this project](LICENSE).
- This is the same license as the code.

## Testing, linting and formatting

To run unit tests locally, ensure that you have installed all relevant requirements.
You will probably want to install it in "editable mode" if you are developing locally.

```bash
$ pip install -e .[optional,testing,checking]
```

Unit tests can then be run as follows:

```bash
$ pytest -v tests
```

To check for linting errors use make (not available on Windows):

```bash
$ make check
```

To format the code use make (not available on Windows):

```bash
$ make format
```

## Style Guidelines

- The code must be compatible with Python 3.8 and higher.
- Max line length is 119
- Docstrings
  - Use the [Google docstring format](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings).
    This is integrated with [Sphinx](https://www.sphinx-doc.org/) using the
    [napoleon extension](https://sphinxcontrib-napoleon.readthedocs.io/).
- Versioning follows the [Semantic Versioning Specification](https://semver.org/) and
  [PEP 440 -- Version Identification and Dependency Specification](https://www.python.org/dev/peps/pep-0440/).

## Code Owners

[@PhilipMay](https://github.com/PhilipMay) - code, general documentation, GitHub actions,
everything else
