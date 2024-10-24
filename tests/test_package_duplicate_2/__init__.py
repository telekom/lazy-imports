# Copyright (c) 2024 Pascal Bachor
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

"""Dummy test package."""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


_import_structure = {
    "module": ["module"],
}

# Direct imports for type-checking
if TYPE_CHECKING:
    from .module import module  # noqa: F401
else:
    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        _import_structure,
    )
