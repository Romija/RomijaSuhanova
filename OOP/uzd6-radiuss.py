class Rinkis:
    def __init__(self,radiuss):
        self.radiuss = radiuss

    def iestatit_radiusu(self,radiuss):
        if radiuss <=0: #ja o vai ngatīvs,tad 1 ir noklusējuma rādiuss
            self.radiuss=1
        else:
            self.radiuss= radiuss

    def izvadit_radiusu(self):
        return self.radiuss #printā šeit būtu grūtāk, vnk vieglāk vērtību izņemt

    def diametrs(self):
        return self.radiuss*2

radiuss = float(input('Ievadiet radiusu: '))
rinkis=Rinkis(radiuss)

print("Riņķa rādiuss ir ",rinkis.izvadit_radiusu())
print("Riņķa diametrs ir ",rinkis.diametrs())
