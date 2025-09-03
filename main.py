string = "23-0a"

string = string.strip().split("-")
print(string)
string = list(map(int, string))
print(string)
            