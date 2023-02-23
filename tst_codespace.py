if __name__ == '__main__':
    print("Hello World!!")
    
    #### Agora vamos adicionar mais coisas ####

        #### Madlibs ####
    from random import randint as rr


    numero = rr(0, 6)
    num = input("Adivinhe o número (de 1 a 6): ")
    madlib = f"Você escolheu o número: {num}\n" \
             f"E o número sorteado é: {numero}."
    print(madlib)
    if num == numero:
        print("Parabéns!!")
    else:
        print("Você perdeu.")
    