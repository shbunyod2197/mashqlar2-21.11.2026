class Mahsulot:
    def __init__(self, nomi, narxi):
        self.nomi = nomi
        self.narxi = narxi

    def malumot(self):
        print(f"Mahsulot: {self.nomi}")
        print(f"Narxi: {self.narxi} so'm")

    def chegirma(self):
        print("Mahsulotga chegirma berildi.")


class Elektronika(Mahsulot):
    def __init__(self, nomi, narxi, kafolat):
        super().__init__(nomi, narxi)
        self.kafolat = kafolat

    def malumot(self):
        super().malumot()
        print(f"Kafolat: {self.kafolat} oy")

    def chegirma(self):
        super().chegirma()
        yangi_narx = self.narxi - (self.narxi * 10 // 100)
        print(f"Chegirmadan keyingi narx: {yangi_narx} so'm")


mahsulot = Elektronika("Noutbuk", 8000000, 12)

mahsulot.malumot()
mahsulot.chegirma()
