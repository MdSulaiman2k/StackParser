
import java.util.*;
import java.util.regex.*;


// Write your code here. DO NOT use an access modifier in your class declaration.
class Parser{
    static Scanner kbd = new Scanner(System.in) ;
    static int  top = 0 ;
     static void push(char[] stack , char v){
         stack[top] = v ;
         top++;
     }
     static boolean pop(char [] stack , char v){
         if(top <= 0)
            return false ;
         top--;
         return ((stack[top] == '{' && v == '}') || (stack[top] == '(' && v == ')')) ;
         
     }
     
     static boolean isBalanced(String st){
         boolean check = true ;
         
         char [] stack  =  new char[st.length()] ;
         Arrays.fill(stack , 'a' ) ;
         for(int i = 0 ; i < st.length() && check ; i++){
             if(st.charAt(i) == '{' || st.charAt(i) == '(') {
                 push(stack , st.charAt(i)) ;
             } 
             else{
                 check =  pop(stack , st.charAt(i)) ;
             }
         }
         if(top != 0)
             check = false ;
         top = 0 ;
         return check ;
     }
}
class Main {
     
	
	public static void main(String[] args) {
		Parser parser = new Parser();
        
		Scanner in = new Scanner(System.in);

		while (in.hasNext()) {
			System.out.println(parser.isBalanced(in.next()));
		}
        
		in.close();
	}
}
