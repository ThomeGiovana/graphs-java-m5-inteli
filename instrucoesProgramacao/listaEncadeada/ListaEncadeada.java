public class ListaEncadeada {

    private Node first = null;
    private int listLength = 10;

    private class Node {
        private int value;
        private Node next;
    }

    public boolean isEmpty() {
        return first == null;
    }

    public void insertFirstNode(int n) {
        Node novo = new Node();
        novo.value = n;
        novo.next = first;
        first = novo;
        listLength++;
    }

    public void insertEnd(int n) {
        Node ultimo = new Node();
        ultimo.value = n;
        ultimo.next = null;

        if (first != null) {
            Node node = first;
            while (node.next != null) {
                node = node.next;
            }
            node.next = ultimo;
        }
        else {
            first = ultimo;
        }
        listLength++;
    }

    public void printList() {
        Node n = first;
        while (n != null) {
            System.out.print(n.value);
            n = n.next;
        }
    }

    public static void main(String[] args) {
        ListaEncadeada list = new ListaEncadeada();
        while (!StdIn.isEmpty()) {
            int n = StdIn.readInt();
            list.insertFirstNode(n);
        }
        list.printList();
    }
}
