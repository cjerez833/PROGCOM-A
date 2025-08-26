import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // ===== Ejercicio 1 =====
        System.out.print("Ingrese un número: ");
        int num = sc.nextInt();
        String mensaje1 = (num > 0) ? "El número es positivo" : (num == 0 ? "El número es cero" : "El número es negativo");
        System.out.println(mensaje1);

        // ===== Ejercicio 2 =====
        System.out.print("\nIngrese su edad: ");
        int edad = sc.nextInt();
        String mensaje2 = (edad > 18) ? "Es mayor de edad" : (edad == 18 ? "Tiene exactamente 18 años" : "Es menor de edad");
        System.out.println(mensaje2);

        // ===== Ejercicio 3 =====
        System.out.print("\nIngrese el primer número: ");
        int a = sc.nextInt();
        System.out.print("Ingrese el segundo número: ");
        int b = sc.nextInt();
        String mensaje3 = (a > b) ? "El mayor es: " + a : (b > a ? "El mayor es: " + b : "Son iguales");
        System.out.println(mensaje3);

        // ===== Ejercicio 4 =====
        System.out.print("\nIngrese calificación (0-100): ");
        int nota = sc.nextInt();
        String mensaje4 = (nota >= 90) ? "Excelente" : (nota >= 60 ? "Aprobado" : "Reprobado");
        System.out.println(mensaje4);

        // ===== Ejercicio 5 =====
        System.out.print("\nIngrese un número: ");
        int num2 = sc.nextInt();
        String mensaje5 = (num2 % 2 == 0) ? "Es par" : "Es impar";
        System.out.println(mensaje5);

        // ===== Ejercicio 6 =====
        System.out.print("\nIngrese tres números: ");
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();
        int n3 = sc.nextInt();
        int mayor = (n1 >= n2 && n1 >= n3) ? n1 : ((n2 >= n1 && n2 >= n3) ? n2 : n3);
        System.out.println("El mayor es: " + mayor);

        // ===== Ejercicio 7 =====
        System.out.print("\nIngrese un año: ");
        int anio = sc.nextInt();
        String mensaje7 = ((anio % 400 == 0) || (anio % 4 == 0 && anio % 100 != 0)) ? "Es bisiesto" : "No es bisiesto";
        System.out.println(mensaje7);

        // ===== Ejercicio 8 =====
        System.out.print("\nIngrese una contraseña: ");
        sc.nextLine(); // limpiar buffer
        String pass = sc.nextLine();
        boolean largo = pass.length() > 8;
        boolean tieneNum = pass.matches(".\\d.");
        boolean tieneMayus = pass.matches(".[A-Z].");
        String mensaje8 = (largo && tieneNum && tieneMayus) ? "Contraseña válida" : "Contraseña inválida";
        System.out.println(mensaje8);

        // ===== Ejercicio 9 =====
        System.out.print("\nIngrese un número: ");
        int fizz = sc.nextInt();
        String mensaje9 = (fizz % 3 == 0 && fizz % 5 == 0) ? "FizzBuzz" :
                          (fizz % 3 == 0 ? "Fizz" :
                          (fizz % 5 == 0 ? "Buzz" : String.valueOf(fizz)));
        System.out.println(mensaje9);

        // ===== Ejercicio 10 =====
        int saldo = 1000; // saldo fijo
        System.out.print("\nIngrese monto a retirar: ");
        int retiro = sc.nextInt();
        String mensaje10 = (retiro < 0) ? "Monto inválido" :
                           (retiro == 0) ? "No retiró nada" :
                           (retiro <= saldo ? "Retiro exitoso. Saldo restante: " + (saldo - retiro) : "Fondos insuficientes");
        System.out.println(mensaje10);

        sc.close();
    }
}