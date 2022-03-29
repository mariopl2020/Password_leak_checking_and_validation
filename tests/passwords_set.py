import mock
import builtins

from passwords_set import PasswordsSet
from password import Password


def test_give_filename():
	"""Tests if returned string is correct"""

	# GIVEN
	test_passwords_set = PasswordsSet()
	# WHEN
	with mock.patch.object(builtins, 'input', lambda _: "my_passes"):
		# THEN
		assert test_passwords_set.give_filename() == "my_passes"


def test_load_your_password_no_argument():
	"""Tests if method takes default filename when argument is not provided, extracts raw content correctly and assign\
	it into new created password objects."""

	# GIVEN
	test_passwords_set = PasswordsSet()
	test_passwords_raw_content = ["antek1234,\n", "annab,\n", "conversion2,"]
	# WHEN
	test_passwords_set.load_your_passwords()
	for index in range(len(test_passwords_set.passwords_list)):
		assert test_passwords_set.passwords_list[index].password_content == test_passwords_raw_content[index]


def test_load_your_password_with_filename_argument():
	"""Tests if method runs with provided filename as argument extracts raw content correctly and assign it into new\
	created password objects."""

	# GIVEN
	test_passwords_set = PasswordsSet()
	test_passwords_raw_content = ["antek1234,\n", "annab,\n", "conversion2,"]
	# WHEN
	test_passwords_set.load_your_passwords("trial_passwords.txt")
	for index in range(len(test_passwords_set.passwords_list)):
		assert test_passwords_set.passwords_list[index].password_content == test_passwords_raw_content[index]


def test_load_your_password_list_length():
	"""Tests if method returns as the same number of passwords as in file"""

	# GIVEN
	test_passwords_set = PasswordsSet()
	expected_password_list_length = 3
	# WHEN
	test_passwords_set.load_your_passwords()
	# THEN
	assert len(test_passwords_set.passwords_list) == expected_password_list_length


def test_clear_password():
	"""Tests if method returns list of passwords where content is cleared from whitespaces"""

	# GIVEN
	test_passwords_set = PasswordsSet()
	test_passwords_raw_content = ["antek1234", "annab", "conversion2"]
	test_passwords_set.load_your_passwords()
	# WHEN
	test_passwords_set.clear_passwords(test_passwords_set.passwords_list)
	# THEN
	for index in range(len(test_passwords_set.passwords_list)):
		assert test_passwords_set.passwords_list[index].password_content == test_passwords_raw_content[index]


def test_clear_password_list_length():
	"""Tests if method returns correct number of trial passwords"""

	# GIVEN
	test_passwords_set = PasswordsSet()
	expected_passwords_list_length = 3
	test_passwords_set.load_your_passwords()
	# WHEN
	test_passwords_set.clear_passwords(test_passwords_set.passwords_list)
	# THEN
	assert len(test_passwords_set.passwords_list) == expected_passwords_list_length


def test_encode_passwords():
	"""Tests if method returns correct password's content in byte form"""

	# GIVEN
	test_passwords_set = PasswordsSet()
	test_passwords_set.load_your_passwords()
	expected_encoded_content_passwords_list = [b'antek1234', b'annab', b'conversion2']
	test_passwords_set.clear_passwords(test_passwords_set.passwords_list)
	# WHEN
	encoded_passwords = test_passwords_set.encode_passwords()
	# THEN
	for index in range(len(test_passwords_set.passwords_list)):
		assert test_passwords_set.passwords_list[index].encoded_content \
			== expected_encoded_content_passwords_list[index]


def test_hash_passwords():
	"""Tests if passwords are transformed correctly from byte form to hash"""

	# GIVEN
	test_passwords_set = PasswordsSet()
	expected_hashed_passwords_content_list = [
		'A2776D1D99EC7D9883A75F9F08EDA3CF3289E50F',
		'3B3D0B484DF21B12E7837B748116A4BEA3684456',
		'7B02B4B09CB9BC9EB10A08CD368A6237B22F17AC']
	test_passwords_set.passwords_list = [Password('antek1234'), Password('annab'), Password('conversion2')]
	# WHEN
	test_passwords_set.encode_passwords()
	test_passwords_set.hash_passwords()
	# THEN
	for index in range(len(test_passwords_set.passwords_list)):
		assert test_passwords_set.passwords_list[index].hashed_content \
			== expected_hashed_passwords_content_list[index]


def test_make_prefix_hashed_passwords():
	"""Tests if prefixes of hashed passwords are correct"""

	# GIVEN
	test_passwords_set = PasswordsSet()
	expected_prefixes_hashed_passwords_content_list = ['A2776', '3B3D0', '7B02B']
	test_passwords_set.passwords_list = [Password('antek1234'), Password('annab'), Password('conversion2')]
	# WHEN
	test_passwords_set.encode_passwords()
	test_passwords_set.hash_passwords()
	test_passwords_set.make_prefix_hashed_passwords()
	# THEN
	for index in range(len(test_passwords_set.passwords_list)):
		assert test_passwords_set.passwords_list[index].hashed_content_prefix \
			== expected_prefixes_hashed_passwords_content_list[index]


def test_fully_process_passwords():
	"""Tests if full path of processing file with passwords gets well to receive correct fields about all passwords\
	in every step
	"""

	#GIVEN
	test_passwords_set = PasswordsSet()
	#WHEN
	with mock.patch.object(builtins, 'input', lambda _: ""):
		test_passwords_set.fully_process_passwords()
	#THEN
	assert test_passwords_set.passwords_list[0].password_content == 'antek1234'
	assert test_passwords_set.passwords_list[0].encoded_content == b'antek1234'
	assert test_passwords_set.passwords_list[0].hashed_content == 'A2776D1D99EC7D9883A75F9F08EDA3CF3289E50F'
	assert test_passwords_set.passwords_list[0].hashed_content_prefix == 'A2776'
