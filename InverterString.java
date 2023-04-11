//Exercicio 05
import java.util.Scanner;

public class InverterString{
    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);
        String entrada = leitor.next();
        String saida = "";

        for(int i = entrada.length() -1; i >= 0; i--) {
            saida += entrada.charAt(i);
        }
        System.out.println(saida);
    }
}