from passwords_api import PasswordsApi

# def test_give_hashes_online_wrong_attitude():
# 	"""Tests if url with provided prefix by user to API's usage returned correct text content. Additionaly response\
# 	is splitted into lines, due to huge text volume"""
#
# 	# GIVEN
# 	test_passwords_api = PasswordsApi()
# 	user_hash_prefix = "a2776"
# 	# WHEN
# 	test_passwords_api.give_hashes(user_hash_prefix)
# 	lines = test_passwords_api.answer_content.splitlines()
# 	# THEN
# 	assert lines[0] == "00194B6D812AC755DFC0B02AE7FF501769E:4"
# 	assert lines[3] == "00B8750546E046B31D70818A2769212CE32:1"


def test_give_hashes_offline_attitude(requests_mock):
	"""Tests if url with provided prefix by user to API's usage returned correct text content. Used mocking to avoid\
	online data change what could affect on tests in time"""

	# GIVEN
	test_passwords_api = PasswordsApi()
	user_hash_prefix = "a2776"
	data = "00194B6D812AC755DFC0B02AE7FF501769E:4\n0078C5DDE59D855EB60D40C8598677FA961:31"
	# WHEN
	requests_mock.get("https://api.pwnedpasswords.com/range/a2776", text=data)
	test_passwords_api.give_hash_suffixes(user_hash_prefix)
	# THEN
	assert test_passwords_api.answer_content == "00194B6D812AC755DFC0B02AE7FF501769E:4\n" + \
		"0078C5DDE59D855EB60D40C8598677FA961:31"


def test_create_dictionary_hashes_frequency(requests_mock):
	"""Tests if provided block of text from API is correctly transformed into dictionary"""

	#GIVEN
	test_passwords_api = PasswordsApi()
	user_hash_prefix = "A2776"
	data = "00194B6D812AC755DFC0B02AE7FF501769E:4\n0078C5DDE59D855EB60D40C8598677FA961:31"
	#WHEN
	requests_mock.get("https://api.pwnedpasswords.com/range/a2776", text=data)
	test_passwords_api.give_hash_suffixes(user_hash_prefix)
	test_passwords_api.create_dictionary_hashes_frequency()
	#THEN
	assert test_passwords_api.hashes_frequency_dict == {
		"A277600194B6D812AC755DFC0B02AE7FF501769E": 4,
		"A27760078C5DDE59D855EB60D40C8598677FA961": 31}

