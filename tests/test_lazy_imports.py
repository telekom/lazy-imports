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

import pytest

from lazy_imports import LazyImporter, __version__


def test_sinple_case() -> None:
    _import_structure = {
        "lazy_imports": ["LazyImporter"],
    }
    extra_objects = {"__version__": __version__}
    lazy_importer = LazyImporter(
        __name__,
        globals()["__file__"],
        _import_structure,
        extra_objects=extra_objects,
    )

    assert lazy_importer._import_structure == _import_structure
    assert lazy_importer._objects == extra_objects

    lazy_importer_dir = dir(lazy_importer)

    assert "lazy_imports" in lazy_importer_dir
    assert "_import_structure" in lazy_importer_dir

    assert lazy_importer.__version__ == __version__


def test_imports() -> None:
    import test_package
    import test_package.module_a
    from test_package import func_of_module_a
    from test_package.module_a import func_of_module_a  # noqa: F811

    assert func_of_module_a() == "func_of_module_a"

    with pytest.raises(ModuleNotFoundError):
        import test_package.module_b  # noqa: F401

    with pytest.raises(ModuleNotFoundError):
        from test_package import func_of_module_b  # noqa: F401


def test_duplicate() -> None:
    with pytest.raises(ValueError):
        import test_package_duplicate_1  # noqa: F401

    with pytest.raises(ValueError):
        import test_package_duplicate_2  # noqa: F401
