# -*- coding: utf-8 -*-

def writeCommentFile(name, comment):
    comment_file = open(name + ".txt", "x")
    comment_file.write(comment)
    comment_file.close()

def makeComment(data):
    lab = data[0]
    name = data[1]
    general_comment = data[2]
    positive_comments = getPositive(data[3])
    negative_comments = getNegative(data[4])
    grade = data[5]

    comment = "Olá, " + name + ", tudo bem? Fui o monitor responsável" \
        + " pela correção do teu " + lab + ".\n\n" + general_comment
    
    comment += "\n\nPontos positivos:\n"
    for positive in positive_comments:
        comment += "- " + positive + "\n"
    comment += "\n"

    comment += "Pontos para prestar atenção:\n"
    for negative in negative_comments:
        comment += "- " + negative + "\n"
    comment += "\n"
    
    comment += "Sua nota do " + lab + " foi *" + str(grade) + "*! Na " \
        + "próxima semana, os professores divulgarão a planilha com as notas" \
        + " finais."

    return comment

def getNegative(number_neg):
    print("COMENTÁRIOS NEGATIVOS\n")

    negative_coments = []

    for i in range(number_neg):
        comment = input("Comentário negativo número " + str(i + 1) + ": ")
        negative_coments.append(comment)
    
    return negative_coments

def getPositive(number_pos):
    print("COMENTÁRIOS POSITIVOS\n")

    positive_coments = []

    for i in range(number_pos):
        comment = input("Comentário positivo número " + str(i + 1) + ": ")
        positive_coments.append(comment)
    
    return positive_coments

def getInputs():
    lab = input("Digite o nome da atividade (LAB2, LAB3, ...): ")
    name = input("Digite o nome do aluno: ")
    general_comment = input("Faça um comentário geral sobre o lab de " \
        + name + ": ")
    number_pos = int(input("Digite o número de comentários positivos: "))
    number_neg = int(input("Digite o número de comentários negativos: "))
    grade = float(input("Digite a nota do aluno neste lab: "))

    return (lab, name, general_comment, number_pos, number_neg, grade)

def main():
    data = getInputs()
    comment = makeComment(data)
    writeCommentFile(data[1], comment)

if __name__ == "__main__":
    main()