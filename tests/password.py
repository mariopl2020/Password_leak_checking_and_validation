import mock
import builtins

from password import PasswordsSet


def test_give_filename():
	"""Tests if returned string is correct"""

	# GIVEN
	test_passwords_set = PasswordsSet()
	# WHEN
	with mock.patch.object(builtins, 'input', lambda _: "my_passes"):
		# THEN
		assert test_passwords_set.give_filename() == "my_passes"


def test_load_your_password_no_argument():
	"""Tests if method take defualt filename when argument is not provided and convert data from it into a raw\
	passwords list correctly"""

	# GIVEN
	test_passwords_set = PasswordsSet()
	# WHEN
	test_passwords_set.load_your_passwords()
	assert test_passwords_set.raw_passwords_list == ['antek1234,\n', 'annab,\n', 'conversion2,']


def test_load_your_password_with_filename_argument():
	"""Tests if method run with provided filename as argument and convert data from it into a raw passwords list\
	correctly"""

	# GIVEN
	test_passwords_set = PasswordsSet()
	# WHEN
	test_passwords_set.load_your_passwords("trial_passwords.txt")
	assert test_passwords_set.raw_passwords_list == ['antek1234,\n', 'annab,\n', 'conversion2,']


def test_load_your_password_list_length():
	"""Tests if method returns as the same number of passwords as in file"""

	# GIVEN
	test_passwords_set = PasswordsSet()
	# WHEN
	test_passwords_set.load_your_passwords()
	# THEN
	assert len(test_passwords_set.raw_passwords_list) == 3


def test_clear_password():
	"""Tests if method returns list of passwords cleared from whitespaces"""

	# GIVEN
	test_passwords_set = PasswordsSet()
	test_passwords_set.load_your_passwords()
	# WHEN
	test_passwords_set.clear_passwords(test_passwords_set.raw_passwords_list)
	# THEN
	assert test_passwords_set.passwords_list == ['antek1234', 'annab', 'conversion2']


def test_clear_password_list_length():
	"""Tests if method returns correct number of trial passwords"""

	# GIVEN
	test_passwords_set = PasswordsSet()
	test_passwords_set.load_your_passwords()
	# WHEN
	test_passwords_set.clear_passwords(test_passwords_set.raw_passwords_list)
	# THEN
	assert test_passwords_set.passwords_list == ['antek1234', 'annab', 'conversion2']


def test_encode_passwords():
	"""Tests if method return correct passwords in byte form"""

	# GIVEN
	test_passwords_set = PasswordsSet()
	test_passwords_set.load_your_passwords()
	test_passwords_set.clear_passwords(test_passwords_set.raw_passwords_list)
	# WHEN
	encoded_passwords = test_passwords_set.encode_passwords()
	# THEN
	assert encoded_passwords == [b'antek1234', b'annab', b'conversion2']


def test_hash_passwords():
	"""Tests if passwords are transformed correctly from byte form to hash"""

	# GIVEN
	test_passwords_set = PasswordsSet()
	test_passwords_set.passwords_list = ['antek1234', 'annab', 'conversion2']
	# WHEN
	hashed_passwords = test_passwords_set.hash_passwords()
	# THEN
	assert hashed_passwords == [
		'a2776d1d99ec7d9883a75f9f08eda3cf3289e50f',
		'3b3d0b484df21b12e7837b748116a4bea3684456',
		'7b02b4b09cb9bc9eb10a08cd368a6237b22f17ac']
