class Televisao:
    def __init__(self):
        self.ligada = True
        self.canal = 5
    
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal +=1
    
    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

televisao = Televisao()

if __name__ == '__main__':
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    print('canal: {}'. format(televisao.canal))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('canal: {}'.format(televisao.canal))

