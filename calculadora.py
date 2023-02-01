class calculadora:
    def sumar(self,num1,num2):
        if isinstance(num1,float) or isinstance(num2,float):
            return 'Sólo números enteros'
        else:
            if num1 >= 0 and num2 >= 0:
                return num1 + num2
            else:
                return 'Sólo números positivos'