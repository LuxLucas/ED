<<<<<<< HEAD
//Incompleto

import java.util.Scanner;

public class Menu{

    private Scanner Leitor = new Scanner(System.in);
    private String Comando;

    public void LimparConsole(){

    }

    public String opcaoPrincipal(){
        System.out.println("1 - Criar pilha");
        System.out.println("2 - Adicionar elementos");
        System.out.println("3 - Remover último elemento");
        System.out.println("4 - Imprimir pilha");
        System.out.println("5 - Pilha cheia");
        System.out.println("6 - Pilha vazia");
        System.out.println("7 - Quantidade de elementos");
        System.out.println("0 - Sair do programa");

        System.out.println('\n');
        System.out.println("Seu comando: ");

        this.Comando = Leitor.nextLine();
        return this.Comando;
    }

    public String receberTamanhoPilha(){

    }

=======
//Incompleto

import java.util.Scanner;

public class Menu{

    private Scanner Leitor = new Scanner(System.in);
    private String Comando;

    public void LimparConsole(){

    }

    public String opcaoPrincipal(){
        System.out.println("1 - Criar pilha");
        System.out.println("2 - Adicionar elementos");
        System.out.println("3 - Remover último elemento");
        System.out.println("4 - Imprimir pilha");
        System.out.println("5 - Pilha cheia");
        System.out.println("6 - Pilha vazia");
        System.out.println("7 - Quantidade de elementos");
        System.out.println("0 - Sair do programa");

        System.out.println('\n');
        System.out.println("Seu comando: ");

        this.Comando = Leitor.nextLine();
        return this.Comando;
    }

    public String receberTamanhoPilha(){

    }

>>>>>>> fbe8aacedfd0e9bde2aaf0c26a699d9fa5cbf0ca
}