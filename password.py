class PasswordsSet():
	"""Represents group of password"""

	def __init__(self):
		"""Initialization of new passwords group"""

		self.raw_passwords_list = []
		self.passwords_list = []
		self.filename = "trial_passwords.txt"

	def give_filename(self):
		"""Asks user to give filename with trial passwords

		Returns:
			filename (str): name of file with trial passwords"""

		#@TODO validation
		filename = input("Enter filename with trial passwords\n")
		return filename

	def load_your_passwords(self, filename: str = None):
		"""Load file with trial passwords and convert them into list

		Arguments:
			filename (str): name of file with passwords in the same directory"""

		if filename is None or filename == "":
			filename = self.filename
		with open(filename, "r") as file:
			self.raw_passwords_list = file.readlines()

	def clear_passwords(self, raw_passwords: list):
		"""Clears raw passwords list from whitespaces
		Arguments:
			raw_passwords (list): list of raw passwords with whitespaces
		Returns:
			self.passwords_list (list): list of cleared passwords"""

		for password in raw_passwords:
			clean_password = password.strip().replace(",", "")
			self.passwords_list.append(clean_password)
		print(self.passwords_list)
		return self.passwords_list
