# 7. Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para
# ser aprovado, todas as médias do aluno devem ser maiores que 7. Considere que o aluno cursa
# apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1,
# matéria2 e matéria3.
matéria1=float(input("Informe a média da matéria 1: "))
matéria2=float(input("Informe a média da matéria 2: "))
matéria3=float(input("Informe a média da matéria 3: "))
média_individual= matéria1 >=7 and matéria2 >=7 and matéria3 >=7
print ("aprovado", média_individual)

8
média_geral= (matéria1+matéria2+matéria3)/3
print ("Média geral é ", média_geral)