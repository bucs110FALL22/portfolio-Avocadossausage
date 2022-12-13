import requests
import bad_quotes_api

class Swagger:
  def __init__(self) -> None:
    ''' 
    Initializes instance of Swagger object
    Return: No return
    '''
  def get(url=""):
    '''
    Placeholder for url
    args: url
    Return: returns information from json request
    '''
    request = requests.get(url)
    request = request.json()
    return request

  def post(url="", payload = {}):
    '''
    Handles payload and requests url
    args: url, payload
    return: returns data from request
    '''
    request = requests.post(url, payload)
    request = request.json()
    return request


