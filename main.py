from indeed import search_indeed
# from save import save_to_csv
from googlesheet import save_csv_cloud

search = 'python'
result_indeed = search_indeed(search)

# save_to_csv(result_indeed)
save_csv_cloud(result_indeed)