import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // ===== Ejercicio 1 =====
        System.out.print("Ingrese un número: ");
        int num = sc.nextInt();
        if(num > 0){
            System.out.println("El número es positivo");
        } else if(num == 0){
            System.out.println("El número es cero");
        } else {
            System.out.println("El número es negativo");
        }

        // ===== Ejercicio 2 =====
        System.out.print("\nIngrese su edad: ");
        int edad = sc.nextInt();
        if(edad > 18){
            System.out.println("Es mayor de edad");
        } else if(edad == 18){
            System.out.println("Tiene exactamente 18 años");
        } else {
            System.out.println("Es menor de edad");
        }

        // ===== Ejercicio 3 =====
        System.out.print("\nIngrese el primer número: ");
        int a = sc.nextInt();
        System.out.print("Ingrese el segundo número: ");
        int b = sc.nextInt();
        if(a > b){
            System.out.println("El mayor es: " + a);
        } else if(b > a){
            System.out.println("El mayor es: " + b);
        } else {
            System.out.println("Son iguales");
        }

        // ===== Ejercicio 4 =====
        System.out.print("\nIngrese calificación (0-100): ");
        int nota = sc.nextInt();
        if(nota >= 90){
            System.out.println("Excelente");
        } else if(nota >= 60){
            System.out.println("Aprobado");
        } else {
            System.out.println("Reprobado");
        }

        // ===== Ejercicio 5 =====
        System.out.print("\nIngrese un número: ");
        int num2 = sc.nextInt();
        if(num2 % 2 == 0){
            System.out.println("Es par");
        } else if(num2 % 2 != 0){
            System.out.println("Es impar");
        } else {
            System.out.println("Número inválido");
        }

        // ===== Ejercicio 6 =====
        System.out.print("\nIngrese tres números: ");
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();
        int n3 = sc.nextInt();
        if(n1 >= n2 && n1 >= n3){
            System.out.println("El mayor es: " + n1);
        } else if(n2 >= n1 && n2 >= n3){
            System.out.println("El mayor es: " + n2);
        } else {
            System.out.println("El mayor es: " + n3);
        }

        // ===== Ejercicio 7 =====
        System.out.print("\nIngrese un año: ");
        int anio = sc.nextInt();
        if((anio % 400 == 0)){
            System.out.println("Es bisiesto");
        } else if(anio % 4 == 0 && anio % 100 != 0){
            System.out.println("Es bisiesto");
        } else {
            System.out.println("No es bisiesto");
        }

        // ===== Ejercicio 8 =====
        System.out.print("\nIngrese una contraseña: ");
        sc.nextLine(); // limpiar buffer
        String pass = sc.nextLine();
        boolean largo = pass.length() > 8;
        boolean tieneNum = pass.matches(".\\d.");
        boolean tieneMayus = pass.matches(".[A-Z].");
        if(!largo){
            System.out.println("Contraseña inválida: debe tener más de 8 caracteres");
        } else if(!tieneNum){
            System.out.println("Contraseña inválida: debe contener un número");
        } else if(!tieneMayus){
            System.out.println("Contraseña inválida: debe contener una mayúscula");
        } else {
            System.out.println("Contraseña válida");
        }

        // ===== Ejercicio 9 =====
        System.out.print("\nIngrese un número: ");
        int fizz = sc.nextInt();
        if(fizz % 3 == 0 && fizz % 5 == 0){
            System.out.println("FizzBuzz");
        } else if(fizz % 3 == 0){
            System.out.println("Fizz");
        } else if(fizz % 5 == 0){
            System.out.println("Buzz");
        } else {
            System.out.println(fizz);
        }

        // ===== Ejercicio 10 =====
        int saldo = 1000; // saldo fijo
        System.out.print("\nIngrese monto a retirar: ");
        int retiro = sc.nextInt();
        if(retiro < 0){
            System.out.println("Monto inválido");
        } else if(retiro == 0){
            System.out.println("No retiró nada");
        } else if(retiro <= saldo){
            System.out.println("Retiro exitoso. Saldo restante: " + (saldo - retiro));
        } else {
            System.out.println("Fondos insuficientes");
        }

        sc.close();
    }
}