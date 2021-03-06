import os
from hashlib import sha1

from password import Password


class PasswordsSet():
	"""Represents group of passwords"""

	def __init__(self):
		"""Initialization of new passwords group"""

		self.passwords_list = []
		self.filename = "trial_passwords.txt"
		self.input_directory = "input"

	def give_filename(self):
		"""Asks user to give filename with trial passwords

		Returns:
			filename (str): name of file with trial passwords"""

		directory_path = os.path.join(os.getcwd(), self.input_directory)
		filename = input("Enter filename with trial passwords\n")
		filepath = os.path.join(directory_path, filename)
		if os.path.exists(filepath):
			return filename
		else:
			print("Provided file does not exist. Used default field - trial_passwords.txt")
			return None

	def load_your_passwords(self, filename: str = None):
		"""Load file with trial passwords and convert them into list of Password objects

		Arguments:
			filename (str): name of file with passwords in input directory"""

		if filename is None or filename == "":
			filename = self.filename
		with open(os.path.join(self.input_directory, filename), "r") as file:
			for password_content in file.readlines():
				self.passwords_list.append(Password(password_content))

	@staticmethod
	def clear_passwords(passwords_list: list):
		"""Clears raw passwords list from whitespaces

		Arguments:
			passwords_list (list): list of password objects only with raw content with whitespaces"""

		for password in passwords_list:
			password.password_content = password.password_content.rstrip()
			if password.password_content[-1:] == ",":
				password.password_content = list(password.password_content)
				password.password_content[-1:] = ""
				password.password_content = "".join(character for character in password.password_content)

	def encode_passwords(self):
		"""Transforms trial passwords content from string to byte form"""

		for password in self.passwords_list:
			password.encoded_content = password.password_content.encode()

	def hash_passwords(self):
		"""Transforms trial password's content in byte form to hashed hexidecimal form in upper case"""

		for password in self.passwords_list:
			password.hashed_content = sha1(password.encoded_content).hexdigest().upper()

	def make_prefix_hashed_passwords(self):
		"""Creates five characters prefix of hashed password to be processed in api requests"""

		for password in self.passwords_list:
			password.hashed_content_prefix = password.hashed_content[0:5]

	def print_password_hash(self): #N
		"""Prints summary of whole loaded trial passwords with their hashes"""

		print("Password : It's hash")
		for password in self.passwords_list:
			print(f"{password.password_content} : {password.hashed_content}")

	def fully_process_passwords(self):
		"""Sum of methods what totally allows converting simple file with passwords into single passwords with\
		their appropriate data to further processing."""

		filename = self.give_filename()
		self.load_your_passwords(filename)
		self.clear_passwords(self.passwords_list)
		self.encode_passwords()
		self.hash_passwords()
		self.make_prefix_hashed_passwords()
		self.print_password_hash()
