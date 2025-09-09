"""Unit tests for bitmap.py."""

from bitmapy.bitmap import Bitmap
from tests.conftest import Status


def test_bitmap_set(status: Bitmap[Status]) -> None:
    """Test setting bits in the bitmap."""
    status.set(Status.BIT_1)

    assert status.value == 3


def test_bitmap_clear(status: Bitmap[Status]) -> None:
    """Test clearing bits in the bitmap."""
    status.clear(Status.BIT_0)

    assert status.value == 0


def test_bitmap_toggle(status: Bitmap[Status]) -> None:
    """Test toggling bits in the bitmap."""
    status.toggle(Status.BIT_0)
    status.toggle(Status.BIT_1)

    assert status.value == 2


def test_bitmap_length(status: Bitmap[Status]) -> None:
    """Test the length of the bitmap."""
    assert len(status) == 3


def test_bitmap_string_representation(status: Bitmap[Status]) -> None:
    """Test the string representation of the bitmap."""
    assert str(status) == "0b001"


def test_bitmap_flags(status: Bitmap[Status]) -> None:
    """Test retrieving set flags from the bitmap."""
    assert status.flags == ["BIT_0"]
