import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('Deu erro.')
else:
    print('Deu certo.')