import requests
import swagger_api

class TranslateAPI:
  def __init__(self) -> None:
    ''' 
    initializes 
    args: self
    return: n/a
    '''
    self.api_url =  "https://libretranslate.com/translate"
    self.languages = {"Chinese" : "zh", "Arabic" : "ar","Greek" : "el", "Russian" : "ru" }
    self.source_code = "en"
    self.api_key = "c9fdfca0-89b1-4098-9d1b-b3dfa44553fd"

  def __str__(self) -> str:
    ''' 
    returns URL of API
    args: self
    return: returns API URL
    '''
    return self.api_url
    
  def translate(self, quote = ""):
    ''' 
    Translates quote
    args: self, quote - breaking bad quote passed
    Prints translated text
    '''
    keys = self.languages.keys()
    print("Please choose a language and I will translate your quote:")
    num = 1

    for key in keys:
      print(str(num) + ". " + key)
      num += 1
    userInput = int(input(""))

    if userInput in range(1,5):
    
      language = list(keys)[userInput - 1]
      code = self.languages[language]

      params = {"q": quote, "source": self.source_code, "target": code, "api_key" : self.api_key}
      request = swagger_api.Swagger.post(self.api_url, params)
      print("Here is your Breaking Bad quote in " + language + ":")
      print(request["translatedText"])
    