import requests

response = requests.get('http://pudim.com.br/')

print (response.status_code)  # 200 significa requisição OK

if (response.status_code == 200):
    print ("Consegui acessar o site Pudim!")
else:
    print("Não consegui acessar o site Pudim!")


#200

#print len(response.content)
#87773

#print response.content[:100]  # imprimindo só os 100 primeiros chars

#<!doctype html><html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en" ><head><title>prog