# Enter your code here. Read input from STDIN. Print output to STDOUT

class EvenStream:
    def __init__(self):
        self.current_value = 0
    def get_next(self):
        value = self.current_value
        self.current_value += 2
        return value

class OddStream:
    def __init__(self):
        self.current_value = 1
    def get_next(self):
        value = self.current_value
        self.current_value += 2
        return value

def print_from_stream(n, stream=EvenStream()):
    for i in range(n):
        print(stream.get_next())

query_set = input()
if int(query_set) >=1 and int(query_set) <= 100:
	for i in range(int(query_set)):
		stream_name, n = input().split()
		n = int(n)
		if n >=1 and n <= 10:
			if stream_name == "even":
				print_from_stream(n, EvenStream())
			else:
				print_from_stream(n, OddStream())
		else:
			pass
else:
	pass
