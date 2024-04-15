# to remember while selecting the index of the number to be swapped we select the
    # numeber that is one less than the number of the index

def main(lista,index):
    if len(lista)//2  < index:
        print(lista)
        return lista

    lista[index] , lista[len(lista)-index-1] = lista[len(lista)-index-1], lista[index]
    main(lista,index+1)


print(main([1,23,4,5,66,77,88],0))

#we first choose the index to be swapped and then til lthe point it will be
# done we have choosen a mid point for the same as the end condition to be meet
# to end the loop
