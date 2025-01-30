import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int X = sc.nextInt();
		
		StringBuilder result = new StringBuilder();
		
		for(int i = 0; i < N; i++) {
		    int num = sc.nextInt();
		    
		    if(num < X) {
		        result.append(num+" ");
		    }
		}
		
		System.out.println(result);
	}
}
