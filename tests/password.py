import mock
import builtins

from password import PasswordsSet


def test_give_filename():
	"""Tests if returned string is correct"""

	#GIVEN
	test_passwords_set = PasswordsSet()
	#WHEN
	with mock.patch.object(builtins, 'input', lambda _: "my_passes"):
		#THEN
		assert test_passwords_set.give_filename() == "my_passes"


def test_load_your_password_no_argument():
	"""Tests if function take defualt filename when argument is not provided and convert data from it into a raw\
	passwords list correctly"""

	#GIVEN
	test_passwords_set = PasswordsSet()
	#WHEN
	test_passwords_set.load_your_passwords()
	assert test_passwords_set.raw_passwords_list == ['antek1234,\n', 'annab,\n', 'conversion2,']


def test_load_your_password_with_filename_argument():
	"""Tests if function run with provided filename as argument and convert data from it into a raw passwords list\
	correctly"""

	#GIVEN
	test_passwords_set = PasswordsSet()
	#WHEN
	test_passwords_set.load_your_passwords("trial_passwords.txt")
	assert test_passwords_set.raw_passwords_list == ['antek1234,\n', 'annab,\n', 'conversion2,']


def test_load_your_password_list_length():
	"""Tests if function returns as the same number of passwords as in file"""

	#GIVEN
	test_passwords_set = PasswordsSet()
	#WHEN
	test_passwords_set.load_your_passwords()
	#THEN
	assert len(test_passwords_set.raw_passwords_list) == 3

def test_clear_password():
	"""Tests if function returns list of passwords cleared from whitespaces"""

	#GIVEN
	test_passwords_set = PasswordsSet()
	test_passwords_set.load_your_passwords()
	#WHEN
	test_passwords_set.clear_passwords(test_passwords_set.raw_passwords_list)
	#THEN
	assert test_passwords_set.passwords_list == ['antek1234', 'annab', 'conversion2']


def test_clear_password_list_length():
	"""Tests if function returns correct number of trial passwords"""

	# GIVEN
	test_passwords_set = PasswordsSet()
	test_passwords_set.load_your_passwords()
	# WHEN
	test_passwords_set.clear_passwords(test_passwords_set.raw_passwords_list)
	# THEN
	assert test_passwords_set.passwords_list == ['antek1234', 'annab', 'conversion2']


