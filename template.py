from string import Template
from datetime import datetime

with open('template.html', 'r') as html:
    template = Template(html.read())
    now =  datetime.now().strftime('%d/%m/%Y')

    body_msg = template.substitute(nome='Vinicius', data=now)

# print(body_msg)
