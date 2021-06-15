import fetch
import parser
from writer import write

def search(query):
    response = fetch.search(query+" review")
    output = parser.search(response)
    write(query, output)

search('surface laptop 4')


