from program import Program
from password import Password


def test_give_leak_numbers(requests_mock):
	"""Tests if user's password hash is correctly processed with the API's response content and assigns correct value
	as matched results"""

	# GIVEN
	test_program = Program()
	test_program.user_passwords_set.passwords_list = [Password("abc")]
	test_program.user_passwords_set.passwords_list[0].hashed_content = "280F400DB69704708F6BAE4406AC3F0A4A50C2CB"
	test_program.user_passwords_set.make_prefix_hashed_passwords()
	assert test_program.user_passwords_set.passwords_list[0].hashed_content_prefix == "280F4"
	# WHEN
	data = '00DB69704708F6BAE4406AC3F0A4A50C2CB:12\n00E919704E4B5CD1BB4562C4B1620CC1A14:1\n00F62DB6D817DB9B22BEBCB' \
	       '757FFE74AB1E:3\n023549BC1745A8931ED2AD2D1005C999F75:2'
	requests_mock.get("https://api.pwnedpasswords.com/range/280F4", text=data)
	test_program.give_leak_numbers()
	# THEN
	assert test_program.api_passwords.hashes_frequency_dict["280F400DB69704708F6BAE4406AC3F0A4A50C2CB"] == 12
	assert test_program.user_passwords_set.passwords_list[0].leaks_number == 12
	assert test_program.user_passwords_set.passwords_list[0].is_safe == False

# @TODO make an another case of passwords without setting hash by hand
