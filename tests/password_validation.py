from password import Password
from passwords_set import PasswordsSet
from password_validation import (
	HasDigitValidation,
	PasswordValidation,
	HasSpecialCharValidation,
	HasLowerCaseValidation,
	HasUpperCaseValidation,
	IsLongEnoughValidation
	)


def test_if_has_digit_is_valid_positive():
	"""Checks if method returns correct value, when password fulfil the conditions"""

	# GIVEN
	test_password = "Adrian4"
	test_has_digit_validator = HasDigitValidation(test_password)
	# WHEN
	is_valid = test_has_digit_validator.is_valid()
	# THEN
	assert is_valid == True


def test_if_has_digit_is_valid_negative():
	"""Checks if method returns correct value, when password does not fulfil the conditions"""

	# GIVEN
	test_password = "Adrian"
	test_has_digit_validator = HasDigitValidation(test_password)
	# WHEN
	is_valid = test_has_digit_validator.is_valid()
	# THEN
	assert is_valid == False


def test_if_has_special_char_is_valid_positive():
	"""Checks if method returns correct value, when password fulfil the conditions"""

	# GIVEN
	test_password = "Adrian4%"
	test_has_special_char_validator = HasSpecialCharValidation(test_password)
	# WHEN
	is_valid = test_has_special_char_validator.is_valid()
	# THEN
	assert is_valid == True


def test_if_has_special_char_is_valid_negative():
	"""Checks if method returns correct value, when password does not fulfil the conditions"""

	# GIVEN
	test_password = "Adrian4"
	test_has_special_char_validator = HasSpecialCharValidation(test_password)
	# WHEN
	is_valid = test_has_special_char_validator.is_valid()
	# THEN
	assert is_valid == False


def test_if_has_lower_case_is_valid_positive():
	"""Checks if method returns correct value, when password fulfil the conditions"""

	# GIVEN
	test_password = "Adrian4"
	test_has_lower_case_validator = HasLowerCaseValidation(test_password)
	# WHEN
	is_valid = test_has_lower_case_validator.is_valid()
	# THEN
	assert is_valid == True


def test_if_has_lower_case_is_valid_negative():
	"""Checks if method returns correct value, when password does not fulfil the conditions"""

	# GIVEN
	test_password = "ADRIAN4"
	test_has_lower_case_validator = HasLowerCaseValidation(test_password)
	# WHEN
	is_valid = test_has_lower_case_validator.is_valid()
	# THEN
	assert is_valid == False


def test_if_has_upper_case_is_valid_positive():
	"""Checks if method returns correct value, when password fulfil the conditions"""

	# GIVEN
	test_password = "Adrian4"
	test_has_upper_case_validator = HasUpperCaseValidation(test_password)
	# WHEN
	is_valid = test_has_upper_case_validator.is_valid()
	# THEN
	assert is_valid == True


def test_if_has_upper_case_is_valid_negative():
	"""Checks if method returns correct value, when password fulfil the conditions"""

	# GIVEN
	test_password = "adrian4"
	test_has_upper_case_validator = HasUpperCaseValidation(test_password)
	# WHEN
	is_valid = test_has_upper_case_validator.is_valid()
	# THEN
	assert is_valid == False


def test_if_is_long_enough_positive():
	"""Checks if method returns correct value, when password fulfil the conditions"""

	# GIVEN
	test_password = "Adrian45"
	test_is_long_enough_validator = IsLongEnoughValidation(test_password)
	# WHEN
	is_valid = test_is_long_enough_validator.is_valid()
	# THEN
	assert is_valid == True


def test_if_is_long_enough_negative():
	"""Checks if method returns correct value, when password does not fulfil the conditions"""

	# GIVEN
	test_password = "Adrian4"
	test_is_long_enough_validator = IsLongEnoughValidation(test_password)
	# WHEN
	is_valid = test_is_long_enough_validator.is_valid()
	# THEN
	assert is_valid == False


def test_if_password_is_completely_valid():
	"""Checks if method returns correctly assign values to passwords after complete password validation"""

	# GIVEN
	test_passwords_set = PasswordsSet()
	test_passwords_set.passwords_list = [Password("test"), Password("Test123%"), Password("T?es2t")]
	test_password_validation = PasswordValidation(test_passwords_set)
	excepted_results = [False, True, False]
	# WHEN
	test_password_validation.is_valid()
	# THEN
	for index in range(len(test_passwords_set.passwords_list)):
		assert test_password_validation.user_passwords_set.passwords_list[index].is_valid == excepted_results[index]
