import gspread


def save_csv_cloud(results):
    gc = gspread.service_account(filename='credentials.json')
    sh = '1v6GXPzQtVLse2bGunqyc6DoMebTQtuy0KNXhcjb_728'
    content = open('jobs.csv', 'r').read().encode('utf-8')
    gc.import_csv(sh, content)

    worksheet = sh.sheet1

    for result in results:
        worksheet.append_row(result)
