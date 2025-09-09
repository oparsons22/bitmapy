"""Unit tests for bitmap.py."""

import pytest
from bitmapy.bitmap import Bitmap
from tests.conftest import Status


def test_bitmap_is_set(status: Bitmap[Status]) -> None:
    """Test checking if bits are set in the bitmap."""
    assert status.is_set(Status.BIT_0)
    assert not status.is_set(Status.BIT_1)


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


def test_enum_type(status: Bitmap[Status]) -> None:
    """Test retrieving the enum type from the bitmap."""
    assert type(status._enum_type) is type(Status)


def test_enum_type_error() -> None:
    """Test that a TypeError is raised if the generic type is not specified."""
    status = Bitmap()
    with pytest.raises(TypeError, match="Generic type T must be specified."):
        _ = status._enum_type


def test_bitmap_reset(status: Bitmap[Status]) -> None:
    """Test resetting the bitmap to zero."""
    status.reset()
    assert status.value == 0


def test_bitmap_equality(status: Bitmap[Status]) -> None:
    """Test equality comparisons for the bitmap."""
    another_status = Bitmap[Status](value=1)
    different_status = Bitmap[Status](value=2)

    assert status == another_status
    assert status != different_status
    assert status == 1
    assert status != 2
    assert status != "invalid type"


def test_bitmap_hashability(status: Bitmap[Status]) -> None:
    """Test that Bitmap instances are hashable."""
    match = "Bitmap objects are mutable and cannot be hashed."
    with pytest.raises(TypeError, match=match):
        hash(status)
