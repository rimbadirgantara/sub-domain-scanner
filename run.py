try:
    from bs4 import BeautifulSoup
    import requests as req
    from os import system as sy
    from sys import argv
except Exception as e:
    print(f'[ERROR] {e}')

sy('cls')
url, judul = argv[1], argv[1]
url = f'https://crt.sh/?q={url}'
print('''
███████╗██╗   ██╗██████╗     ██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗
██╔════╝██║   ██║██╔══██╗    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║
███████╗██║   ██║██████╔╝    ██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║
╚════██║██║   ██║██╔══██╗    ██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║
███████║╚██████╔╝██████╔╝    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
╚══════╝ ╚═════╝ ╚═════╝     ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗                   
██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗                  
███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝                  
╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗                  
███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║                  
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝  
Made By Rimba "cicak" Dirgantara
''')


def statco(url):
    return req.get(url).status_code


def simpan(data, judul):
    with open(f'result-{judul}.html', 'w') as f:
        for i in data:
            v = i.get_text().replace('*.', '')
            a = f'<a href="https://{v}" target="_blank">{v}</a><br>'
            f.write(a)
    f.close()
    print(f'[INFO] selesai !\n[INFO] hasil -> result-{judul}.html')


def run(url):
    print('[INFO] proses skening....')
    reqq = req.get(url)
    html = BeautifulSoup(reqq.text, 'html.parser')

    css = 'body table ~ table td.outer table tr:not(:nth-child(1)) td:nth-child(5)'
    data = html.select(css)
    return data

if 200 == statco(url):
    simpan(run(url), judul)
else:
    print(f'[INFO] {judul} not found')
    exit()
