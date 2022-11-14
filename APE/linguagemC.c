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

<<<<<<< HEAD
/*
 * 
 */
int main(int argc, char** argv) {
    
    char nome[30];
    char endereco[30];
    Char telefone [15];
    
    printf("digite seu nome: \n");
    scanf("%s", &nome);
    
    printf("digite seu endereco\n");
    scanf("%s", &endereco);
    
    printf("digite telefone \n");
    scanf("%d", &telefone);
    
    printf("\n Nome: %s",nome );
    
    printf("\n Endereco: %s", endereco);
    
    printf("\n telefone: %d", telefone);

    return (EXIT_SUCCESS);
}
=======
    return (EXIT_SUCCESS);
}
 
>>>>>>> d6b582c5cdd5d6288e04a097cf3ad3180ff82113
