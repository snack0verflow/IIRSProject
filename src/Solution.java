import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.next();
        char[] ar=s.toCharArray();
        int i=0;
        boolean flag;
        do{
            flag=Character.isLowerCase(ar[i]);
               i++;
            System.out.println(i+" "+ar[i]);
        }while(flag);
       
            
    }
}