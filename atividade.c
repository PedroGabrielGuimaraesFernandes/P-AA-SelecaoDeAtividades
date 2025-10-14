#include <stdio.h>

// Função recursiva para selecionar atividades
void seleciona_atividades_recursivo(int inicio[], int fim[], int ultima_escolhida, int total) {
    int proxima = ultima_escolhida + 1;

    // Encontra a próxima atividade que não conflita com a última escolhida
    while (proxima <= total && inicio[proxima] < fim[ultima_escolhida]) {
        proxima++;
    }

    // Se ainda há atividades válidas
    if (proxima <= total) {
        printf("Atividade %d selecionada (inicio=%d, fim=%d)\n", proxima, inicio[proxima], fim[proxima]);
        // Chama recursivamente para continuar selecionando a partir da próxima
        seleciona_atividades_recursivo(inicio, fim, proxima, total);
    }
    // Caso contrário, termina (caso base)
}

int main() {
    // Vetores de início e fim (índice 0 reservado como sentinela)
    int inicio[] = {0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12};
    int fim[]    = {0, 4, 5, 6, 7, 9, 9,10,11,12,14,16};

    int total = 11; // Número total de atividades (sem contar o índice 0)

    printf("Atividades selecionadas:\n");
    seleciona_atividades_recursivo(inicio, fim, 0, total);

    return 0;
}
