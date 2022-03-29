from requests import get


class PasswordsApi():
	"""Representation of API where are stored password hashes with their leak's numbers"""

	def __init__(self, base_url='https://api.pwnedpasswords.com/range/'):
		"""Initialization od API object

		Arguments:
			base_url (str): first, base part of API url"""

		self.base_url = base_url
		self.answer_content = ""
		self.hashes_frequency_dict = {}
		self.user_hash_prefix = ""

	def give_hash_suffixes(self, user_hash_prefix: str):
		"""Gets all matched hash suffixes from api with provided prefix of hashed password and write them down to api\
		object field (self.answer_content) as block of text

		Arguments:
			user_hash_prefix (str): five characters of hashed password prefix from user used to url request"""

		self.user_hash_prefix = user_hash_prefix
		full_url = self.base_url + self.user_hash_prefix
		with get(full_url) as content:
			self.answer_content = content.text

	def create_dictionary_hashes_frequency(self):
		"""Processes block of text from api to dictionary where the key is suffix and value is leak frequency\
		Therefore prefix is added to every suffix to get complete hash code"""

		hashes_frequency_list = self.answer_content.splitlines()
		for element in hashes_frequency_list:
			hash_frequency = element.split(":")
			self.hashes_frequency_dict[self.user_hash_prefix + hash_frequency[0]] = int(hash_frequency[1])

