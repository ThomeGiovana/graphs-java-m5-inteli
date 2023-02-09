public class DiscreteDistribution {
    public static void main(String[] args) {
        int m = Integer.parseInt(args[0]);
        int[] sum = new int[args.length];
        sum[0] = 0;

        for (int i = 1; i < args.length; i++) {
            sum[i] = Integer.parseInt(args[i]) + sum[i - 1];
        }

        for (int i = 1; i <= m; i++) {
            double r = (Math.random());
        }
    }
}
