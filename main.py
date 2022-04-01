from leak_analyse import LeakAnalyse
from password_validation import PasswordValidation
from passwords_set import PasswordsSet


class Program():
	"""Representation of complete program to check if provided passwords were leaked and are validated with other
	conditions to be safe passwords"""

	def __init__(self):
		"""Initialization of new program"""

		self.user_passwords_set = PasswordsSet()
		self.leak_analyse = LeakAnalyse(self.user_passwords_set)
		self.password_validation = PasswordValidation(self.user_passwords_set)

	def main_run(self): #N
		"""Collects group of program's main parts(called methods) what creates complete program run. Contains passwords
		processing provided by user, checking their leaks and validation of other conditions to be safe passwords"""

		self.user_passwords_set.fully_process_passwords()
		self.leak_analyse.main_run()
		self.password_validation.main_run()


if __name__ == "__main__":
	program = Program()
	program.main_run()


