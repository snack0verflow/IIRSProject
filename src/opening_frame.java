
import java.util.logging.Level;
import java.util.logging.Logger;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author trainee2017184
 */
public class opening_frame {
    
    public static void main(String args[]){
    Splash sp=new Splash();
    sp.setVisible(true);
try{
    for(int i=0;i<=100;i++){
        Thread.sleep(25);
    sp.percentage.setText(Integer.toString(i)+"%");
    sp.loadingbar.setValue(i);
    if(i==100){
        sp.setVisible(false);
        
       Home h=new Home();
       h.setVisible(true);
    }
       
    }
}       catch (InterruptedException ex) {
            Logger.getLogger(opening_frame.class.getName()).log(Level.SEVERE, null, ex);
        }
    
    
    
    }


}
