from flask import Flask
import random

app = Flask(__name__)

rastgelebilgi = ["Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.","Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız","2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.","2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.","Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.","Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.","Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.","Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor."]

@app.route("/")
def hello_world():
    bilgi=random.choice(rastgelebilgi)
    return f"<h1>RASTGELE BİLGİ:{bilgi}</h1>"

@app.route("/rastgeletoplam")
def toplam():
    x =random.randint(1,100)
    y =random.randint(1,100)
    toplam=x+y
    return f'rastgele oluşturulan iki sayının toplamı={toplam}' 

@app.route("/sifreolusturucu")
def generate_password(length=9):
    characters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    password = ''.join(random.choices(characters, k=length))
    return f'rastgele oluşturulan şifre={password}'
    

app.run(debug=True)
