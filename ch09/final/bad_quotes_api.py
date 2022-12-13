import requests
import swagger_api

class BreakingBadQuotesAPI:
  def __init__(self) -> None:
    ''' 
    Initializes instance of BreakingBadQuotesAPI object
    Return: No return
    '''
    self.api_url =  "https://api.breakingbadquotes.xyz/v1/quotes"
  
  def __str__(self) -> str:
    ''' 
    returns URL of API
    args: self
    return: returns API URL
    '''
    return self.api_url
    
  def getQuote(self):
    ''' 
    returns
    args: self
    return: returns breaking bad quote
    '''
    request = swagger_api.Swagger.get(self.api_url)
    return request[0]["quote"]
    
 