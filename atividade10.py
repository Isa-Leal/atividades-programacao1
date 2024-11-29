programa {
  funcao inicio()
  {
    inteiro num, contador = 0

    // Laço para solicitar os 5 números
    para(inteiro i = 1; i <= 5; i++)
    {
      escreva("Digite o número ", i, ": ")
      leia(num)

      // Verifica se o número é positivo
      se (num > 0)
      {
        contador++  // Incrementa o contador se o número for positivo
      }
    }

    // Exibe a quantidade de números positivos digitados
    escreva("Você digitou ", contador, " números positivos.")
  }
}
