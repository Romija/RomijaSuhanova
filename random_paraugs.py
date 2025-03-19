class Kaste:
    def __init__(self,malas_garums, krasa):
        #malas garums var būt no 2-10, ja neatbilst, tad uzstādīt default uz 2
        if malas_garums>=2 and malas_garums<=10:
            self.malas_gaurums = malas_garums
        else:
            print("Malas garums neatbilst")
            self.malas_gaurums = 2
        self.krasa = krasa