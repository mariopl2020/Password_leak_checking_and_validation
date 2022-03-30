class Password():
	"""Represents single password"""

	def __init__(self, password_content):
		"""Initialization of new password"""

		self.password_content = password_content
		self.encoded_content = b""
		self.hashed_content = ""
		self.hashed_content_prefix = ""
		self.leaks_number = 0
		self.is_safe = None

	def __repr__(self):
		"""Text representation of single password

		Returns: password_name (str): name of password simultaneously represents its content"""

		password_name = f"{self.password_content}"
		return password_name

