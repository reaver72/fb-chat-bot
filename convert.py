import json

cookies = input("Paste fb cookies here: ")
cookies = cookies.replace("=", ":").replace(";", ",")[:-1]
cookies_dict = {}
cookies = cookies.split(",")

for values in cookies:
    values = values.split(":")
    cookies_dict[values[0]] = values[1]

json_cookies = json.dumps(cookies_dict)

print(f'\n------------------->> JSON COOKIES <<---------------------\n\n{json_cookies}\n')
