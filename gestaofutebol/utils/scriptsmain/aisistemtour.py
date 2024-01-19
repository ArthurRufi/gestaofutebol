#sistema de mini inteligencia artificial que vai pegar a quantidade de time e gerar um tornei compativel, vamos treinar isso mais tarde
class TourneyPreview():

    def __init__(self, equipesparticipantes):
        self.is_impar = True
        self.codigo_verificador_quantidade = 0
        self.equipes_participantes = equipesparticipantes


    def imparoupar(self, qtde_quipes):
        #verifica se o numero é impar ou par
        if qtde_quipes % 2 == 1:
            self.is_imparimpar = True
            return True
        elif qtde_quipes % 2 == 0:
            self.is_impar = False
            return False
    

    def verficadordequantidade(self, qtde_quipes):
        
        if qtde_quipes == 3:
            #modelo curto pode ser por confronto direto ou mata mata com finalista direto
            #confronto direto time1 x time2, time2 x time 3, time1 x time3
            self.codigo_verificador_quantidade = 1001
            return 1001
        
        elif qtde_quipes >= 4 and qtde_quipes <=8:
            if self.imparoupar(qtde_quipes) == False and qtde_quipes != 6:
                #adicionar modelo para 4 e para 8
                self.codigo_verificador_quantidade = 2001
            
        elif qtde_quipes > 8 and qtde_quipes <=16:
            #modelo oitavas de final pode ser elegivel
            if qtde_quipes == 16:
                #chaveamento mata mata por oitavas de final
                self.codigo_verificador_quantidade = 3001
            elif qtde_quipes < 16:
                #ver outras opções
                if self.imparoupar(qtde_quipes) == True:
                    #montar modelos de pontos corridos
                    if qtde_quipes == 9:
                        #chaveamento com três opções, mata-mata formato persoanlizado, pontos corridos, fase de grupos.
                        self.codigo_verificador_quantidade = 3002
                elif self.imparoupar(qtde_quipes) == False:
                    #chaveamento por mata mata
                    if qtde_quipes == 10:
                        #dois grupos com 5 times onde se classifica 2 times de cada grupo
                        self.codigo_verificador_quantidade = 3003
                    

        elif qtde_quipes > 16 and qtde_quipes <32:
            #modelo pontos corridos ou mata mata personalizado

            pass
    

a = TourneyPreview(5)
print(a.imparoupar(a.equipes_participantes))