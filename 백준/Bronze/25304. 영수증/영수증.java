import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int play = sc.nextInt();
		int summary = 0;
		
		for(int i = 0; i < play; i++) {
		    int a = sc.nextInt();
		    int b = sc.nextInt();
		    summary = summary + (a * b);
		}
		if(summary == n) {
		    System.out.println("Yes");
		} else {
		    System.out.println("No");
		}
	}
}
