
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author trainee2017184
 */
public class OSvalidation {
   private static String OS = System.getProperty("os.name").toLowerCase();

	

	public static void main(String[] args) {

		//System.out.println(OS);
if (isWindows()) {
			System.out.println("This is Windows");
		} 
		 else if (isUnix()) {
			System.out.println("This is Unix or Linux");
		} 
		
		} 
	

	public static boolean isWindows() {

		return (OS.contains("win"));

	}

	public static boolean isUnix() {

		return (OS.contains("nix") || OS.indexOf("nux") >= 0 || OS.indexOf("aix") > 0 );

	}


}
    

