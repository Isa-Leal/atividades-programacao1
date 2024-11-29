programa {
  funcao inicio()
  {
    inteiro num, fatorial = 1

    escreva("Digite um número inteiro positivo: ")
    leia(num)

    // Verifica se o número é positivo
    se (num >= 0)
    {
      para(inteiro i = 1; i <= num; i++)
      {
        fatorial = fatorial * i
      }
      escreva("O fatorial de ", num, " é: ", fatorial)
    }
    senao
    {
      escreva("Por favor, insira um número inteiro positivo.")
    }
  }
}
