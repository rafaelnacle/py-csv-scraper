from indeed import search_indeed
from save import save_to_csv

search = 'python'

result_indeed = search_indeed(search)

save_to_csv(result_indeed)


