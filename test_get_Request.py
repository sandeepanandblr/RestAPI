# Url : https://reqres.in/
###GO to this video as well : https://symfonycasts.com/screencast/rest/rest#play

import requests
import pytest

url="https://reqres.in/api/users?page=2"
def test_001():
    response = requests.get(url)



    print(response)
    print(response.status_code)

    #get body , and the type of content is BYTE type
    print(response.content)
    print('response.content:::', type(response.content))

    #get header
    print(response.headers)
    print('response.headers:::', type(response.headers))
    head = response.headers
    print('Date:::',response.headers['Date'])

    #getting body using TEXT has return type STRING
    print(response.text)

    print(type(response.text))

    ##Total time to Execute
    print('Total time to Execute::::::', response.elapsed)

    assert response.status_code == 200