article = "I am testing"
substitutions = {
  "testing":"a line of code",
  "am": "tested"
}

for key, value in substitutions.items():
  article = article.replace(key, value)

print(article)

