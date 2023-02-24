import java.util.Arrays;

public class MergeSort {
    public static void intercalar(int[] v, int[] aux, int ini, int meio, int fim) {
        for (int k = ini; k <= fim; k++) {
            aux[k] = v[k];
        }
        int i = ini;
        int j = meio + 1;

        for (int k = ini; k <= fim; k++) {
            if (i > meio) v[k] = aux[j++];
            else if (j > fim) v[k] = aux[i++];
            else if (aux[i] < aux[j]) v[k] = aux[i++];
            else v[k] = aux[j];
        }
    }

    public static void mergeSort(int[] v, int[] aux, int ini, int fim) {
        if (ini < fim) {
            int meio = (ini + fim) / 2;
            mergeSort(v, aux, ini, meio);
            mergeSort(v, aux, meio + 1, fim);
            intercalar(v, aux, ini, meio, fim);
        }
    }

    public static void main(String[] args) {
        int[] v = { 4, 6, 7, 3, 5, 1, 2, 8 };
        int[] aux = new int[v.length];

        mergeSort(v, aux, 0, v.length - 1);
        System.out.println(Arrays.toString(v));
    }
}
