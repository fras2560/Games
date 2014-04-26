package fras2560;

import javax.swing.JComponent;
import javax.swing.Timer;

public class model {
public int ballx;
public int bally;
public int ballxspeed=3;
public int ballyspeed=3;
public int lenBall =10;
public int p1x;
public int p1y;
public int p1Score;
public int p2x;
public int p2y;
public int p2Score;
public static final int padHeight =30;
public static final int movement=5;
public static final int padWidth =10;
public static final int start=500;
private int HEIGHT;
private int WIDTH;
private int HEIGHT_NOT_SEEN=35;
private frame gc;

	public model(int x1, int x2, int y1, int y2,int w,int h){
		this.p1x=x1;
		this.p2x=x2;
		this.p1y=y1;
		this.p2y=y1;
		ballx=500;
		bally=100;
		HEIGHT=h-HEIGHT_NOT_SEEN;
		WIDTH=w;
		p2Score=0;
		p1Score=0;
	}
	
	public void moveplayer(int player,int direction){
		if (player==1){
			if((direction>0)&& ((this.p1y-movement)>0)){
				p1y=p1y-movement;
			}else if ((direction<0)&&((this.p1y+movement)<HEIGHT)){
				p1y=p1y+movement;
			}
		}else{
			
			if((direction>0)&& ((this.p2y-movement)>0)){
				p2y=p2y-movement;
			}else if((direction<0)&&((this.p2y+movement)<HEIGHT)){
				p2y=p2y+movement;
			}
		}
	}

	public void moveBall(){
		if(ballx<0){
			ballx=start;
			p2Score=p2Score+1;
		}else if (ballx>WIDTH){
			ballx=start;
			p1Score=p1Score+1;
		}else{
			ballx=ballx+ballxspeed;	
		}
		if((bally<0)||(bally>HEIGHT)){
			ballyspeed=-1*ballyspeed;
			bally=bally+ballyspeed;
		}else{
			bally=bally+ballyspeed;
		}
	}

	public void collision(){
		if((inRange(ballx,p1x,p1x+padWidth)&&(inRange(bally,p1y,p1y+padHeight)))){
			ballxspeed=-ballxspeed;
			ballx=ballx+ballxspeed;
		}else if ((inRange(ballx,p1x,p1x+padWidth)&&(inRange(bally+lenBall,p1y,p1y+padHeight)))){
			ballxspeed=-ballxspeed;
			ballx=ballx+ballxspeed;
		}
		if((inRange(ballx+padWidth,p2x,p2x+padWidth)&&(inRange(bally,p2y,p2y+padHeight)))){
			ballx=p2x-padWidth;
			ballxspeed=-ballxspeed;
		}else if ((inRange(ballx+padWidth,p2x,p2x+padWidth)&&(inRange(bally+lenBall,p2y,p2y+padHeight)))){
			ballx=p2x-padWidth;
			ballxspeed=-ballxspeed;
		}	
	}

	public boolean inRange(int value, int startingRange, int endingRange){
		boolean result=false;
		if ((value>=startingRange)&&(value<=endingRange)){
			result=true;	
		}
		return result;
	}
}
