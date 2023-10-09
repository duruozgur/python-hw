from flask import Flask
import random

facts_list = ["Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
            "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası akıllı telefonlarına bağımlı olduğunu düşünüyor.",
            "Sosyal ağların olumlu ve olumsuz yanları var ve bu platformları kullanırken her ikisinin de farkında olmalıyız.",
            "Teknoloji bağımlılığı çalışması, modern bilimsel araştırmanın en alakalı alanlarından biridir."]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<a href="/ays">Rastgele bir gerçeği görüntüle!</a>'

@app.route("/ays")
def hello_ays():
    return f'<p>{random.choice(facts_list)}</p>'

app.run(debug=True)
