public class Cachorro {
    private String nome;
    private int idade;
    private String cor;
    private double peso;
    private double posicaoX;
    private double posicaoY;

    // constructor method
    // nomei = input do nome
    public Cachorro(String nomei, int idadei) {
        this.nome = nomei;
        this.idade = idadei;
    }

    public void setCor(String c) {
        this.cor = c;
    }

    public static void main(String[] args) {
        Cachorro c1 = new Cachorro("Blu", 3);
        c1.setCor(args[0]);
        System.out.println(c1.nome);
    }
}
