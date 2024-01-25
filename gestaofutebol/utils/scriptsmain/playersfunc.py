from main.models import Players

class Player:
    def __init__(self) -> None:
        pass

    def converterfuncao(self, number):
        #criar dict para cada função
        if number == 1:
            jogador == 'GO'

        elif number > 1 and number <= 5:
            if number == 2:
                jogador = 'PE'
            elif number == 3:
                jogador = 'PD'
            elif number == 4:
                jogador = 'ATA'
            elif number == 5:
                jogador = 'SA'

        elif number >5 and number <=11:
            #meios campitas
            if number == 6:
                jogador = 'ME'
            elif number == 7:
                jogador = 'MD'
            elif number == 8:
                jogador = 'MC'
            elif number == 9:
                jogador = 'VOL'
            elif number == 10:
                jogador = 'MAT'
            elif number == 11:
                jogador = 'MM'

        if number == 0:
            p = 'que pena'