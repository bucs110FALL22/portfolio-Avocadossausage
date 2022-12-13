import bad_quotes_api
import swagger_api
import translate

def main():
  '''
  Executes the application
  args: n/a
  return: no return, but prints translated quote and untranslated quote along with text
  '''
  print("Here is your Breaking Bad quote:")
  breaking_bad_api = bad_quotes_api.BreakingBadQuotesAPI()
  quote = breaking_bad_api.getQuote()
  print(quote)

  translate_api = translate.TranslateAPI()
  translate_api.translate(quote)
    
main()