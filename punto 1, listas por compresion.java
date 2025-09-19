import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<String> combo = new ArrayList<>();
        String[] letras = {"a", "b"};
        int[] números = {1, 2, 3};
        for (String l : letras) {
            for (int n : números) {
                combo.add(l + n);
            }
        }
        System.out.println("Combinaciones: " + combo);
    }
}