#sistema de mini inteligencia artificial que vai pegar a quantidade de time e gerar um tornei compativel, vamos treinar isso mais tarde
class Tourney():

    def __init__(self):
        impar = False
        codigoverificadorquantidade = 0

    def imparoupar(self, qtdequipes):
        if qtdequipes % 2 == 1:
            self.impar = True
        elif qtdequipes % 2 == 0:
            self.impar = False
    


    def verficadordequantidade(self, qtdequipes):
        if qtdequipes < 4:
            #modelo curto
            pass
        elif qtdequipes >= 4 and qtdequipes <=8:
            #outro modelo
            pass
        elif qtdequipes >= 8 and qtdequipes <=16:
            #modelo oitavas de final pode ser elegivel
            if qtdequipes == 16:
                #chaveamento mata-mata pode ser elegivel
                pass
            elif qtdequipes < 16:
                #ver outras opções
                pass
        elif qtdequipes > 16:
            #modelo pontos corridos ou mata mata personalizado
            pass
    

