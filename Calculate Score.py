import random
from faker import Faker  #faker framework'unu pip ile indirip import ettik

#Faker modulunu calistirmak icin degiskene atiyoruz

fake_data = Faker()

#olusturacagimiz fake ogrencileri kaydetmek icin bir liste yaratiyoruz

classroom = list()

#10 defa calisacak bir donguyle fake ogrenciler yaratalim
##fake_data.name() her turda  bir fake isim dondurecek

for name in range(10):
    classroom.append(fake_data.name())

#notlari tutacagimiz sozlugu yaratalim

st = dict()

for student in classroom:
    st[student] = dict()
    st[student]['not1'] = random.randrange(0,100)
    st[student]['not2'] = random.randrange(0,100)
    st[student]['not3'] = random.randrange(0,100)
    print('*' * 30)
    print(student, "=", int((st[student]['not1'] + st[student]['not2'] + st[student]['not3'])/3))

#yukaridaki dongude ilk satirda her ogrenci icin bir dongu olusturuyor sonraki satirlarda
# o ogrenci icin notlari random.randrange ile olusturuyoruz
#random.randrange bize belirtilen aralikta bir rakam seciyor.
#ve bu notlari her ogrenci icin sozluk icinde sozluk olusturarak not1, not2, not3 olarak kaydediyoruz
#son satirda ise ortalama aliyoruz


#genel gorunum icin sozlugumuzu yazdiralim
print(st)


