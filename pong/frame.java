package fras2560;

import java.awt.Color;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JFrame;

public class frame extends JFrame {
	model game;
	component c;
	public frame(){
		this.setSize(1000,300);
		game=new model(50, 950,200,200,1000,300);
		c=new component(game,300,1000);
		this.add(c);
		this.addKeyListener(new key());
	}
	public static void main(final String args[]) {
		final frame view = new frame();
		view.setSize(1000, 300);
		view.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		view.setResizable(false);
		view.setVisible(true);
	}
	private class key implements KeyListener{

		@Override
		public void keyPressed(KeyEvent e) {
			switch (e.getKeyCode())
			{
		    case KeyEvent.VK_W :
		            frame.this.c.p1d = 1;
		            break;
		    case KeyEvent.VK_S : 
		            frame.this.c.p1d = -1;
		            break;
		    case KeyEvent.VK_UP:
		            frame.this.c.p2d=1;
		            break;
		    case KeyEvent.VK_DOWN:
		       		frame.this.c.p2d=-1;
		            break;
			}
			
		}
		
		@Override
		public void keyReleased(KeyEvent e) {
			switch (e.getKeyCode())
			{
		    case KeyEvent.VK_W :
		            frame.this.c.p1d = 0;
		            break;
		    case KeyEvent.VK_S : 
		            frame.this.c.p1d = 0;
		            break;
		    case KeyEvent.VK_UP:
		            frame.this.c.p2d=0;
		            break;
		    case KeyEvent.VK_DOWN:
		       		frame.this.c.p2d=0;
		            break;
			}
		}

		@Override
		public void keyTyped(KeyEvent arg0) {
			// not needed
		}
	}
}
