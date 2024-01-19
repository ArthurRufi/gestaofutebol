#sistema de mini inteligencia artificial que vai pegar a quantidade de time e gerar um tornei compativel, vamos treinar isso mais tarde
class TourneyPreview():

    def __init__(self, equipesparticipantes):
        self.impar = True
        self.codigoverificadorquantidade = 0
        self.equipesparticipantes = equipesparticipantes


    def imparoupar(self, qtdequipes):
        #verifica se o numero é impar ou par
        if qtdequipes % 2 == 1:
            self.impar = True
            return True
        elif qtdequipes % 2 == 0:
            self.impar = False
            return False
    

    def verficadordequantidade(self, qtdequipes):
        
        if qtdequipes == 3:
            #modelo curto pode ser por confronto direto ou mata mata com finalista direto
            #confronto direto time1 x time2, time2 x time 3, time1 x time3
            self.codigoverificadorquantidade = 1001
            return 1001
        
        elif qtdequipes >= 4 and qtdequipes <=8:
            if self.imparoupar(qtdequipes) == False and qtdequipes != 6:
                #adicionar modelo para 4 e para 8
                self.codigoverificadorquantidade = 2001
            
        elif qtdequipes > 8 and qtdequipes <=16:
            #modelo oitavas de final pode ser elegivel
            if qtdequipes == 16:
                #chaveamento mata mata por oitavas de final
                self.codigoverificadorquantidade = 3001
            elif qtdequipes < 16:
                #ver outras opções
                if self.imparoupar(qtdequipes) == True:
                    #montar modelos de pontos corridos
                    if qtdequipes == 9:
                        #chaveamento com três opções, mata-mata formato persoanlizado, pontos corridos, fase de grupos.
                        self.codigoverificadorquantidade = 3002
                elif self.imparoupar(qtdequipes) == False:
                    #chaveamento por mata mata
                    if qtdequipes == 10:
                        #dois grupos com 5 times onde se classifica 2 times de cada grupo
                        self.codigoverificadorquantidade = 3003
                    

        elif qtdequipes > 16 and qtdequipes <32:
            #modelo pontos corridos ou mata mata personalizado

            pass
    

a = TourneyPreview(5)
print(a.imparoupar(a.equipesparticipantes))