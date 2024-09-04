from versions import (
    python_version,
    requests_version,
    pytest_version
)

def test_python_version():
    version_info = python_version()
    assert version_info.major == 3  # Ensuring that Python 3 is being used
    assert version_info.minor >= 8  # Allowing any minor version greater than or equal to 8

def test_requests_version():
    assert requests_version().startswith("2.")  # Ensuring it's version 2.x.x of requests

def test_pytest_version():
    assert pytest_version().startswith("7.") or pytest_version().startswith("8.")  # Ensuring it's version 7.x.x or 8.x.x of pytest
