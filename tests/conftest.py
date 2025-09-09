"""Global test configuration and fixtures."""

from enum import IntFlag, auto

import pytest
from bitmapy.bitmap import Bitmap


class Status(IntFlag):
    """Example IntFlag for testing."""

    BIT_0 = auto()
    BIT_1 = auto()
    BIT_2 = auto()


@pytest.fixture
def status() -> Bitmap[Status]:
    """Fixture that provides a status bitmap."""
    return Bitmap[Status](value=1)
