class Shaxs:
    def __init__(self, ism, familiya, yosh, tugilgan_yil, manzil, tel_raqam, email, orzu, qita):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
        self.tugilgan_yil = tugilgan_yil
        self.manzil = manzil
        self.tel_raqam = tel_raqam
        self.email = email
        self.orzu = orzu
        self.qita = qita

    def ism_familiya_aytish(self):
        return f"Ism va familiya: {self.ism} {self.familiya}"


    def yosh_aytish(self):
        return f"Yoshi: {self.yosh} yoshda"


    def yil_aytish(self):
        return f"Tug'ilgan yili: {self.tugilgan_yil}-yil"


    def manzil_aytish(self):
        return f"Yashash manzili: {self.manzil}"

    def tel_aytish(self):
        return f"Telefon raqami: {self.tel_raqam}"

    def email_aytish(self):
        return f"Email manzili: {self.email}"


    def bormoqchi_joy_aytish(self):
        return f"Bormoqchi bo'lgan joyi: {self.orzu }"


    def qita_aytish(self):
        return f"Yashayotgan qit'asi: {self.qita}"

foydalanuvchi = Shaxs(
    ism="Akbar",
    familiya="Anvarov",
    yosh=16,
    tugilgan_yil=2010,
    manzil="Surxondaryo",
    tel_raqam="+998885849339",
    email="akbarshokh18@gmail.com",
    orzu="amerika",
    qita="Osiyo"
)

print(foydalanuvchi.ism_familiya_aytish())
print(foydalanuvchi.yosh_aytish())
print(foydalanuvchi.yil_aytish())
print(foydalanuvchi.manzil_aytish())
print(foydalanuvchi.tel_aytish())
print(foydalanuvchi.email_aytish())
print(foydalanuvchi.bormoqchi_joy_aytish())
print(foydalanuvchi.qita_aytish())


    