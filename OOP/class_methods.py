class Hotel:
	salary= 200

	@classmethod
	def sal(cls):
		return cls.salary

print(Hotel.sal())