"""

pip install requests
"""
import requests

response = requests.get('http://127.0.0.1:5000/users3',
                        json={'name':"lisi","age":[22,33]},
                        headers={'content-type': 'application/json',
                                 'Cookie': 'ck=7C98C109F3BCE8F8F30478678BC8F0ED'})
print(response.text)