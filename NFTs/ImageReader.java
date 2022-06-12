import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.JPanel;
//import javax.swing.SwingUtilities;
import java.util.Scanner;

public class Main extends JPanel{
  BufferedImage img;
  static int width;
  static int height;
  Scanner sc = new Scanner(System.in);
  String url = sc.nextLine();
  public Main(){
    //setSize(5,5);
    setVisible(true);
    loadImage(url);
  }

  public void loadImage(String URL){
    try{
      img = ImageIO.read(Main.class.getResource(URL));
      width = img.getWidth();
      height = img.getHeight();
      System.out.println("Read complete.");
    }
    catch(IOException e){
      e.printStackTrace();
    }
  }
  /*
  static final int PIXEL_SIZE = 20;
  static final int SCREEN_WIDTH = width;
  static final int SCREEN_HEIGHT = height;
  static final int ALL_PIXELS = (SCREEN_WIDTH*SCREEN_HEIGHT)/PIXEL_SIZE;
  */
  
  protected void paintComponent(Graphics g){
    super.paintComponent(g);
    //g.drawImage(img,0,0,width,height,this);
    //System.out.println("Print complete.");
    //draw(g,rgb,x,y);
    printImage(g);
    //draw(g,rgb,x,y);
    System.out.println("Print complete.");
  }

  static final int PIXEL_SIZE = 1;
  static int SCREEN_WIDTH = width;
  static int SCREEN_HEIGHT = height;
  static int ALL_PIXELS = (SCREEN_WIDTH*SCREEN_HEIGHT)/PIXEL_SIZE;

  /*
   public void draw(Graphics g, int[] rgb1, int x1, int y1){
        //if the game is on draw these lines that make up the grid
    //super.draw(g);
    
      g.setColor(Color.RED);
      g.fillRect(x,y,10,10);
      System.out.println("YEEHAW");
      //g.drawLine(i*PIXEL_SIZE, 0, i*PIXEL_SIZE, SCREEN_HEIGHT);
      //g.drawLine(0,i*PIXEL_SIZE, SCREEN_WIDTH, i*PIXEL_SIZE);
    
  }
  */

  int[] getActualRGB(int color){
    return new int[]{
      (color & 0xff0000) >> 16,
      (color & 0xff00) >> 8,
      color & 0xff
    };
  }
  /*
  public void draw1(Graphics g,int[] rgb,int row, int column){
    g.setColor(Color.red);
    int x = column;
    int y= row;
    g.fillRect(x,y,1,1);
  }
  */
  int[] rgb = new int[3];

  public void printImage(Graphics g){
    //EXTERNAL
    int SQUARELENGTH = 2;
    for (int row = 0; row < SCREEN_HEIGHT -1; row += SQUARELENGTH){
      // EVERY COLUMN
      for (int col = 0; col < SCREEN_WIDTH-1; col+=SQUARELENGTH){
        long average = 0;
        int denominator = 0;

        // INTERNAL
        for (int row1 = 0; row1 < SQUARELENGTH; row1++){
          for (int col1 = 0; col1 < SQUARELENGTH; col1++){


            
            try{
              if (!(row+row1>=SCREEN_HEIGHT) && !(col+col1>=SCREEN_WIDTH)){
              average+= img.getRGB( col+col1, row+row1);
              denominator+=1;
                }
            } catch (Exception e){
              System.out.println("ERROR:\n"+SCREEN_HEIGHT+"\n"+SCREEN_WIDTH+"\n"+(row+row1)+"\n" + (col+col1) + "\n=======");
            }
          }
        }

        
        rgb = getActualRGB((int)average);
        //int grays = (rgb[0] + rgb[1] + rgb[2])/3;
        //This is in color ====== 
        
        g.setColor(new Color(rgb[0],rgb[1],rgb[2]));
        //g.setColor(new Color(grays,grays,grays));
        g.fillRect(col,row,1,1);
        
        /*
        if (rgb[0] >= 125 && rgb[1] >= 125 && rgb[2] >= 1) System.out.print(" ");
        else {System.out.print("#");}
        // System.out.println("Average NOW: " + average);
        */
      }
      //System.out.println();
      
    }
  }

  public static void main(String[] args){
    System.out.println("Image URL: ");
    JFrame frm = new JFrame();
    frm.setVisible(true);
    frm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frm.add(new Main());
    frm.setSize(width,height);
    SCREEN_WIDTH = width;
    SCREEN_HEIGHT = height;
    //System.out.println(SCREEN_WIDTH);
    //System.out.println(SCREEN_HEIGHT);
    ALL_PIXELS = (SCREEN_WIDTH*SCREEN_HEIGHT)/PIXEL_SIZE;
    
    
  }
}
