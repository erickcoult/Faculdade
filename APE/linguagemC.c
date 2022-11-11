#include <stdio.h>
#include <stdlib.h>
int main(int argc, char** argv) {
    
    char nome[30];
    char endereco[30];
    int telefone [15];
    
    printf("digite seu nome: \n");
    fgets(nome, 30, stdin);
    
    printf("digite seu endereco\n");
    fgets(endereco, 30, stdin);
    
    printf("digite telefone \n");
    fgets(telefone, 15, stdin);
    
    printf("\n Nome: %s",nome );
    
    printf("\n Endereco: %s", endereco );
    
    printf("\n Telefone: %s", telefone );

    return (EXIT_SUCCESS);
}
 