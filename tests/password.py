from password import Password


def test_repr():
	"""Tests correctness of password's string representation"""

	test_password = Password("ann1234")

	assert repr(test_password) == "ann1234"
