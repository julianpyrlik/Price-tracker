import requests
from bs4 import BeautifulSoup
import smtplib
import os

product = 'https://www.amazon.com/Retainer-Cleaner-Denture-Cleanser-Discoloration/dp/B094P1W9PY/ref=sxin_14_pa_sp_search_thematic_sspa?content-id=amzn1.sym.d17ca69f-1a39-4f7d-a62f-e5dff4cfd6d8%3Aamzn1.sym.d17ca69f-1a39-4f7d-a62f-e5dff4cfd6d8&crid=1LWFVY1F9D86L&cv_ct_cx=retainer+cleaner&keywords=retainer+cleaner&pd_rd_i=B094P1W9PY&pd_rd_r=f939155f-e4e8-4b93-bddf-f885529e3bf0&pd_rd_w=uyuvl&pd_rd_wg=PnHoB&pf_rd_p=d17ca69f-1a39-4f7d-a62f-e5dff4cfd6d8&pf_rd_r=AMPRM7AC2NTNADRK1D2F&qid=1704007904&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=retain%2Caps%2C137&sr=1-2-364cf978-ce2a-480a-9bb0-bdb96faa0f61-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM&psc=1'

response = requests.get(product)
webpage = response.text

soup = BeautifulSoup(webpage, features='html.parser')

price = float(soup.find(name='span', class_='a-offscreen').getText().split('$')[1])

maximum_price = 100

# -------------------------------------------Email------------------------------
my_email = "julianpythontest@gmail.com"
password = os.environ.get("PASSWORD")

text = f'The price of your product just dropped to ${price}. Go here to buy:\n\n{product}'

if price <= maximum_price:
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='julian-pyrlik@gmx.de', msg=f'Subject: Price Alert\n\n{text}')
