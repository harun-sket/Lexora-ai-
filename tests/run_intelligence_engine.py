from languages.tamil.token import TamilToken
from languages.tamil.intelligence import enrich

token = TamilToken("தம்ழி")

token = enrich(token)

print(token.to_dict())
