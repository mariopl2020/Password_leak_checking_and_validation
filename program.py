from passwords_set import PasswordsSet
from passwords_api import PasswordsApi


class Program():
	"""Representation of single program to check, if user's trials passwords were leaked in the Internet"""

	def __init__(self):
		"""Initialization of new run of program"""

		self.user_passwords_set = PasswordsSet()
		self.api_passwords = PasswordsApi()

	# @TODO test and build
	def main_run(self):
		""""""

		self.user_passwords_set.fully_process_passwords()

	# @TODO experiment to divide it into 2 single methods
	def give_matched_passwords_hashes(self):
		"""Makes requests to API for all provided passwords (their hashed prefixes) by user, get response as block\
		of data with suffixes of potential hashes, transform it into understandable dictionary. Next looking for equal\
		hash and if it is found, it is saved in password object as matched result"""

		for password in self.user_passwords_set.passwords_list:
			self.api_passwords.give_hash_suffixes(user_hash_prefix=password.hashed_content_prefix)
			self.api_passwords.create_dictionary_hashes_frequency()

			for hash_password, frequency in self.api_passwords.hashes_frequency_dict.items():
				if password.hashed_content == hash_password:
					password.is_safe = False
					password.leaks_number = frequency
					break
				else:
					password.is_safe = True



if __name__ == "__main__":
	program = Program()
	program.main_run()
	program.give_matched_passwords_hashes()
