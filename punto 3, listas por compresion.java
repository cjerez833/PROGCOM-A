import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<String> palabras = Arrays.asList("sol", "estrella", "mar", "planeta");
        List<String> letras = new ArrayList<>();
        for (String a : palabras) {
            if (a.length() > 4) {
                letras.add(a);
            }
        }
        System.out.println("Las palabras con más de 4 letras son: " + letras);
    }
}