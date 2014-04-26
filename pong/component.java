package fras2560;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JComponent;
import javax.swing.Timer;
	
public class component extends JComponent implements ActionListener {
	//Graphics bufferGraphics;
	Image offScreen;
	model game;
	private int HEIGHT;
	private int WIDTH;
	public int p1d;
	public int p2d;
	
	public component(model m, int h, int w){
		game=m;
		HEIGHT=h;
		WIDTH=w;
		this.setSize(1000, 300);
		this.start();
	}
	
	public void paintComponent( Graphics g ) {  
		Graphics2D bufferGraphics=(Graphics2D) g;
		bufferGraphics.clearRect(0, 0, WIDTH, HEIGHT);
        bufferGraphics.setColor(Color.BLUE);
        bufferGraphics.fillRect(game.p1x, game.p1y, game.padWidth,game.padHeight);
        bufferGraphics.setColor(Color.GREEN);
        bufferGraphics.fillRect(game.p2x, game.p2y, game.padWidth,game.padHeight);
        bufferGraphics.setColor(Color.WHITE);
        bufferGraphics.fillRect(250,0,20,300);
        bufferGraphics.setColor(Color.red);
        bufferGraphics.fillRect(game.ballx,game.bally,game.lenBall,game.lenBall);
        bufferGraphics.setColor(Color.RED);
        bufferGraphics.drawString(game.p1Score+"", 30, 270);
        bufferGraphics.drawString(game.p2Score+"", 830, 270);
        Toolkit.getDefaultToolkit().sync();    
	}
	
	public void start(){
		Timer time=new Timer (5,this);
		time.start();		
	}
	
	@Override
	public void actionPerformed(ActionEvent arg0) {
		game.moveBall();
		game.collision();
		game.moveplayer(1, p1d);
		game.moveplayer(2, p2d);
		this.repaint();
	}
}
