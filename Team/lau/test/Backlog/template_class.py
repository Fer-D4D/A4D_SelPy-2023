class RecetaPan:

    def __init__(self, harina_grs=0,
                 azucar_grs=0,
                 huevo_piezas=0,
                 sal_grs=0,
                 mantequilla_grs=0,
                 leche_ml=0,
                 levadura_grs=0,
                 chocolate_gr=0,
                 vainilla_ml=0):

        self.harina_grs = harina_grs
        self.azucar_grs = azucar_grs
        self.huevo_piezas = huevo_piezas
        self.sal_grs = sal_grs
        self.mantequilla_grs = mantequilla_grs
        self.leche_ml = leche_ml
        self.levadura_grs = levadura_grs
        self.chocolate_gr = chocolate_gr
        self.vainilla_ml = vainilla_ml

    def mezclar_ingredientes(self):
        return self.harina_grs + self.azucar_grs

    def receta_fer(self, harina, huevo):
        self.harina_grs = harina
        self.huevo_piezas = huevo

    def receta_laura(self, harina, huevo, azucar, chocolate):
        self.harina_grs = harina
        self.huevo_piezas = huevo
        self.azucar_grs = azucar
        self.chocolate_gr = chocolate


if __name__ == "__main__":
    empanada = RecetaPan()
    print("Cantidad de huevos: " + str(empanada.huevo_piezas))
    print("Cantidad de harina: " + str(empanada.harina_grs))
    empanada.receta_laura(500, 4, 200, 3000)
    print("Cantidad de huevos: " + str(empanada.huevo_piezas))
    print("Cantidad de harina: " + str(empanada.harina_grs))
    empanada.receta_fer(400, 6)
    print("Cantidad de huevos: " + str(empanada.huevo_piezas))
    print("Cantidad de harina: " + str(empanada.harina_grs))

    muffin = RecetaPan()
    muffin.receta_laura(500, 4, 200, 3000)
    print("Cantidad de huevos: " + str(muffin.huevo_piezas))
    print("Cantidad de harina: " + str(muffin.harina_grs))
