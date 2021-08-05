# Copyright (c) 2018 Preferred Networks, Inc.
# Copyright (c) 2021 Philip May
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

import pytest

from lazy_imports import try_import


def test_try_import_is_successful() -> None:
    with try_import() as imports:
        pass
    assert imports.is_successful()
    imports.check()


def test_try_import_is_successful_other_error() -> None:
    with pytest.raises(NotImplementedError):
        with try_import() as imports:
            raise NotImplementedError
    assert imports.is_successful()  # No imports failed so `imports` is successful.
    imports.check()


def test_try_import_not_successful() -> None:
    with try_import() as imports:
        raise ImportError
    assert not imports.is_successful()
    with pytest.raises(ImportError):
        imports.check()

    with try_import() as imports:
        raise SyntaxError
    assert not imports.is_successful()
    with pytest.raises(ImportError):
        imports.check()
