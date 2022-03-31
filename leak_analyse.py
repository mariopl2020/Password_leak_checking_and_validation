from passwords_set import PasswordsSet
from passwords_api import PasswordsApi


class LeakAnalyse():
	"""Representation of single password leak analyse to check, if user's trials passwords were leaked in the Internet"""

	def __init__(self, user_passwords_set: PasswordsSet):
		"""Initialization of new run of program"""

		self.user_passwords_set = user_passwords_set
		self.api_passwords = PasswordsApi()

	def main_run(self): #N
		"""Collects group of called methods what compares passwords with API request, gives results, show them and 
		write to appropriate files""" #N

		self.give_leak_numbers()
		self.user_passwords_set.show_results()
		self.user_passwords_set.save_all_passwords_details()

	def give_leak_numbers(self):
		"""Makes requests to API for all provided passwords (their hashed prefixes) by user, get response as block\
		of data with suffixes of potential hashes, transform it into understandable dictionary. Next looking for equal\
		hash and if it is found, it is saved in password object as matched result"""

		for password in self.user_passwords_set.passwords_list:
			self.api_passwords.give_hash_suffixes(user_hash_prefix=password.hashed_content_prefix)
			self.api_passwords.create_dictionary_hashes_frequency()

			# compare_hashes
			for hash_password, frequency in self.api_passwords.hashes_frequency_dict.items():
				if password.hashed_content == hash_password:
					password.is_safe = False
					password.leaks_number = frequency
					break
				else:
					password.is_safe = True
