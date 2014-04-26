/*
 * Name: Dallas Fraser
 * Date: 10/09/2013
 * Purpose: a simple tic tac toe game
 *
 */

//includes
#include <GL/glut.h>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

//function prototypes
void circlePlotPoints(GLint, GLint, GLint, GLint);
void drawCircle(GLint,GLint,GLint,GLint,GLfloat,GLfloat,GLfloat);
void drawList();
GLint findRow(GLint);
GLint findColumn(GLint);
void Motion(GLint, GLint);
void mouseDraw(GLint, GLint, GLint, GLint);
void winReshapeFcn(GLint, GLint);
void drawBox();
void drawX(GLint,GLint);
void drawO(GLint, GLint);
string intToString(GLint);
void renderBitmapString(GLfloat, GLfloat, void *,const char *);
GLboolean checkAvailable(GLint,GLint);
GLint checkZero(GLint);
void menu(GLint);
void newGame();
void beginnerMove(GLint, GLint);
void mediumMove(GLint, GLint);
void DallasMove(GLint, GLint);
GLint checkOver();
void playInthatRow(GLint);
void playInthatColumn(GLint);
void playDiagonal(GLint);
GLint sumColumn(GLint);
GLint sumRow(GLint);
GLint sumDiagonal(GLint);
GLint playWinningMove(GLint);
GLint playCorner();
void playerMove(GLint,GLint,GLint);
GLboolean checkIfcorner(GLint, GLint);

//Global Variables Settings
GLint winWidth = 300, winHeight = 300;
GLint windowId;
GLint squares [3][3];
GLint dividers = 100;
GLint border = 50;
GLint players;
GLint playerTurn;
GLint over = 0;
GLint difficulty = 1;
GLint turn = 0;
GLboolean strategy = true;

/*
 * newGame
 * 	a functions that resets the game
 * 	Parameters:
 * 		none
 * 	Returns:
 * 		none
 */
void newGame(){
	GLint row,col;
	for(row=0;row<3;row++){
		for(col=0;col<3;col++){
			squares[row][col] = 0;
		}
	}
	players = 1;
	playerTurn = 1;
	over = 0;
	turn = 0;
	strategy = true;
}

/*
 * init
 * a function to initialize the window and game settings
 * Parameters:
 * 	none
 * Returns:
 * 	none
 */
void init(){
	glClearColor(1.0, 1.0, 1.0, 0.0);
	glMatrixMode(GL_PROJECTION);
	gluOrtho2D(0.0, winWidth, winHeight, 0.0);
	glColor3f(1.0, 0.0, 0.0);
	glFlush();
	newGame();
}

/*
 * drawList
 * 		the main drawing function. Draws everything to the screen
 * 	Parameters:
 * 		none
 * 	Returns:
 * 		none
 *
 */
void drawList() {
	glClear(GL_COLOR_BUFFER_BIT); // Clear display window.

	if (over != 0){
		glPointSize(5.0);
		glColor3f(1.0, 0.0, 1.0);
		string player;
		if(over == 2){
			if(players == 2){
				player = "Winner:Player Two";
			}else {
				player = "Winner:Machine Dominates";
			}
		}else if (over == 1){
			player = "Winner:Player One";
		}else{
			player = "Tie: Cats Game";
		}
		string output = player;
		renderBitmapString(50,100,GLUT_BITMAP_8_BY_13, player.c_str());
		renderBitmapString(0,120,GLUT_BITMAP_8_BY_13, "Start new game by right clicking");
	}
	drawBox();
	GLint row,col, value;
	for(row=0;row<3;row++){
		for(col=0;col<3;col++){
			value = squares[row][col];
			if(value == 1){
				drawX(row,col);
			}else if(value == 10){
				drawO(row,col);
			}
		}
	}
	glFlush();

}

/*
 * intToString
 * 	a function that takes an integer and converts it to a string
 * 	Parameter:
 * 		num: the number to convert
 * 	Returns:
 * 		result: the string representation
 */
string intToString(GLint num){
	string result;
	ostringstream convert;
	convert << num;
	result = convert.str();
	return result;
}

/*
 * drawBox
 * 	a function that draws the game border/outline
 * 	Parameters:
 * 		none
 * 	Returns:
 * 		none
 *
 */
void drawBox(){
	glPointSize(5.0);
	glColor3f(0.0, 0.0, 0.0);
	glBegin(GL_LINES);
		glVertex2f(dividers, 0);
		glVertex2f(dividers, (dividers*3));
	glEnd();
	glBegin(GL_LINES);
			glVertex2f(dividers*2, 0);
			glVertex2f(dividers*2, (dividers*3));
	glEnd();
	glBegin(GL_LINES);
			glVertex2f(0, dividers);
			glVertex2f(3*dividers, (dividers));
	glEnd();
	glBegin(GL_LINES);
			glVertex2f(0, dividers*2);
			glVertex2f(3*dividers, (dividers*2));
	glEnd();
}

/*
 * Motion
 * 	the function that deals with motion
 * 	Not used at the moment
 */
void Motion(GLint x, GLint y) {

}

/*
 * findRow
 * a function that find the row that was played in
 * 	Parameters:
 * 		y: the y position
 * 	Returns:
 * 		row: the row position
 */
GLint findRow(GLint y){
	GLint row = (GLint) y / dividers;
	return row;
}

/*
 * findColumn
 * a function that find the column that was played in
 * 	Parameters:
 * 		x: the x position
 * 	Returns:
 * 		col: the column position
 */
GLint findColumn(GLint x){
	GLint col = (GLint) x / dividers;
	return col;
}

/*
 * playCorner
 * 	a function that play in the corner if possible
 * 	Parameters:
 * 		none
 * 	Returns
 * 		played: 0 if did not player otherwise 1
 *
 */
GLint playCorner(){
	GLint played = 1;
	if(checkAvailable(0,0) == true){
		//top left
		playerMove(0,0,2);
	}else if(checkAvailable(0,2) == true){
		//top right
		playerMove(0,2,2);
	}else if (checkAvailable(2,0) == true){
		//bottom left
		playerMove(2,0,2);
	}else if (checkAvailable(2,2) == true){
		// bottom right
		playerMove(2,2,2);
	}else{
		played = 0; //did not player
	}
	return played;
}


/*
 * drawO
 * a function to draw O
 * Parameters:
 * 	row: the row to draw in
 * 	column: the column to draw in
 * Returns:
 * 	none
 *
 */
void drawO(GLint row,GLint column){
	GLint x,y, trans;
	y = row * dividers;
	x = column * dividers;
	trans = (GLint) dividers / 2;
	drawCircle((x+trans),(y+trans), (x+2*trans), (y+trans), 0.0, 1.0, 0.0);
}

/*
 * drawX
 * a function to draw x
 * Parameters:
 * 	row: the row to draw in
 * 	column: the column to draw in
 * Returns:
 * 	none
 *
 */
void drawX(GLint row, GLint column){
	GLint x,y;
	y = row * dividers;
	x = column * dividers;
	glColor3f(1.0, 0.0, 0.0);
	glPointSize(5.0);
	glBegin(GL_LINES);
		glVertex2i(x+dividers,y);
		glVertex2i(x,y+dividers);
	glEnd();
	glBegin(GL_LINES);
		glVertex2i(x,y);
		glVertex2i(x+dividers,y+dividers);
	glEnd();
}

/*
* drawCircle
* a functions that draws a  non-filled circle using mid point circle algorithm
* Parameters:
* 			  	x1: the first x coordinate
* 			  	y1: the first y coordinate
* 			  	x2: the second x coordinate
* 			  	y2: the second y coordiante
* 			  	red: The amount of red in rectangle
* 			  	blue: the amount of blue in rectangle
* 			  	green: the amount of green in rectangle
*/
void drawCircle(GLint x1, GLint y1, GLint x2, GLint y2, GLfloat red,
				GLfloat blue, GLfloat green)
{
	glPointSize(1.0);
	glColor3f(red, green, blue);
	GLint dx = x2 - x1, dy = y2 - y1;
	dx = dx * dx;
	dy = dy * dy;
	GLint radius;
	GLint p, x, y;
	radius = (GLint)(fabs(sqrt( dx + dy )));
	p = 1 - radius;
	x = 0;
	y = radius;
	glBegin(GL_POINTS);
	while(x < y){
		if (p < 0){
			p += x + x +1;
		}else{
			y -= 1;
			p += x +x - y - y +1;
		}
		circlePlotPoints(x1, y1, x, y);
		x += 1;
	}
	glEnd();
}

/*
 * circlePlotPoints
 * 		a helper function that takes on point on the circle and draws it and all
 * 		7 other points on that circle
 * 	Parameters:
 * 		xc: the x center coordinate
 * 		yx: the y center coordinate
 * 		x: the distance to the x value on the circle
 * 		y: the distance to the y value on the circle
 *
 */
void circlePlotPoints(GLint xc, GLint yc, GLint x, GLint y){
	glVertex2i(xc+x, yc+y);
	glVertex2i(xc-x, yc+y);
	glVertex2i(xc+x, yc-y);
	glVertex2i(xc-x, yc-y);
	glVertex2i(xc+y, yc+x);
	glVertex2i(xc-y, yc+x);
	glVertex2i(xc+y, yc-x);
	glVertex2i(xc-y, yc-x);
}

/*
 * playerMove
 * a function plays the given p[layers move
 * 	Parameters:
 * 		row: the row to play in
 * 		column: the column to play in
 * 		player: the player to play
 */
void playerMove(GLint row, GLint column, GLint player){
	if(player == 2){
		printf("Played (%i,%i)\n",row,column);
	}
	if (player == 1){
		squares[row][column] = 1;
	}else{
		squares[row][column] = 10;
	}
}

/*
 * computerMove
 * 	a function that calls the appropriate algorithm based on difficulty
 * 	Parameters:
 * 		row:the row just played in by opponent
 * 		column: the column just played in by opponent
 * 	Returns:
 * 		none
 */
void computerMove(GLint row, GLint column){
	if (difficulty == 1){
		beginnerMove(row,column);
	}else if (difficulty == 2){
		mediumMove(row,column);
	}else if (difficulty == 3){
		DallasMove(row, column);
	}

}

/*
 * playInthatColumn
 * 	a function that plays in the column given
 * 	Parameters:
 * 		column: the column to play in
 * 	Returns:
 * 		none
 *
 */
void playInthatColumn(GLint column){
	GLint row;
	for(row=0;row<3;row++){
		if(checkAvailable(row,column) == true){
			playerMove(row,column, 2);
			return;
		}
	}
}

/*
 * playInthatRow
 * 	a function that plays in the row given
 * 	Parameters:
 * 		row: the row to play in
 * 	Returns:
 * 		none
 *
 */
void playInthatRow(GLint row){
	GLint column;
	for(column=0;column<3;column++){
		if(checkAvailable(row,column) == true){
			playerMove(row,column, 2);
			return;
		}
	}
}

/*
 * playDiagonal
 * 	a function that player in the diagonal spot
 * 	Parameters:
 * 		direction: the direction of the diagonal to play in
 * 	Returns:
 * 		none
 *
 */
void playDiagonal(GLint direction){
	GLint col,row;
	if (direction == 0){
		//forward
		row = 0;
		for(col=0;col<3;col++){
			if(checkAvailable(row,col) == true){
				playerMove(row,col,2);
				return;
			}
			row++;
		}
	}else{
		row = 2;
		for(col=0;col<3;col++){
			if(checkAvailable(row,col) == true){
				playerMove(row,col,2);
				return;
			}
			row --;
		}
	}
}

/*
 * playWinningMove
 * 	a function that plays a winning move if available or blocks a winning move
 * 	Parameters:
 * 		offense: 1 if playing offense else playing defense
 * 	Returns:
 * 		1 if a move was made
 * 		0 otherwise
 */
GLint playWinningMove(GLint offense){
	GLint c, r;
	GLint score;
	GLint sumCol[3];
	GLint sumRows[3];
	GLint player;
	if (offense == 1){
		player = 20;
	}else{
		player = 2;
	}
	for (c=0;c<3;c++){
		//sum all rows and columns
		sumCol[c] = sumColumn(c);
		sumRows[c] = sumRow(c);
	}

	for(c=0;c<3;c++){
		if (sumCol[c] == player){
			playInthatColumn(c);
			return 1;
		}
	}

	for(r=0;r<3;r++){
		if (sumRows[r] == player){
			playInthatRow(r);
			return 1;
		}
	}
	//check diagonals
	score = sumDiagonal(0);
	if(score == player){
		playDiagonal(0);
		return 1;
	}
	score = sumDiagonal(1);
	if(score == player){
		playDiagonal(1);
		return 1;
	}
	return 0;
}

/*
 * mediumMove
 * 	a algorithm Dallas Fraser made for the medium cpu difficulty
 * 	Parameters:
 * 		row: the row position the human just played on
 * 		column: the column position the human just played on
 * 	Returns:
 * 		none
 */
void mediumMove(GLint row, GLint column){
	//check to see if can win
	if(playWinningMove(1) == 0){
		//no winning offence move
		if(playWinningMove(0) == 0 ){
			//no needed defence move
			if(checkAvailable(1,1) == false){
				//middle if not available
				if(playCorner() == 0){
					//no corner available
					//so just play like a beginner
					// since most likely a cats game
					beginnerMove(row,column);
				}
			}else{
				//play center if available
				playerMove(1,1,0);
			}
		}
	}

}

/*
 *  checkIfCorner
 *  a function that check if last move in a corner spot
 *  Parameters:
 *  	row: the row that was played
 *  	column: the column that was played
 *  Returns:
 *  	GLboolean: true if it was a corner false otherwise
 *
 */
GLboolean checkIfcorner(GLint row, GLint column){
	GLboolean corner = false;
	if ( ((row == 0) or (row == 2)) and ((column == 0) or (column == 2)) ){
		corner = true;
	}
	return corner;
}

/*
 * DallasMove
 * 	a algorithm Dallas Fraser made for the hard cpu difficulty
 * 	Parameters:
 * 		row: the row position the human just played on
 * 		column: the column position the human just played on
 * 	Returns:
 * 		none
 *
 */
void DallasMove(GLint row, GLint column){
	if (turn == 0){
		if(checkIfcorner(row,column) == true){
			//cats game
			strategy = false;
			mediumMove(row,column);
		}else{
			//move beside the player
			if(row == 1){
				playerMove(row+1,column,2);
			}else{
				playerMove(row,column+1,2);
			}

		}
		turn ++;
	}else if(turn == 1 and strategy == true){
		//check to see if they blocked the move
		if(playWinningMove(1) == 0){
			GLint colToplay;
			if(column == 0){
				colToplay = 2;
			}else{
				colToplay = 0;
			}
			if(checkAvailable(1,colToplay) == true){
				playerMove(1,colToplay,2);
			}else{
				playerMove(2,1,2);
			}
		}
	}else if (turn == 2 and strategy == true){
		//guaranteed to win
		playWinningMove(1);
	}else{
		mediumMove(row,column);
	}
}

/*
 * beginnerMove
 * 	a function that uses a simple algorithm to play as the computer
 * 	Parameters:
 * 		row: the row position the human just played on
 * 		column: the column position the human just played on
 * 	Returns:
 * 		none
 *
 */
void beginnerMove(GLint row, GLint column){
	GLint spotx, spoty;
	if(checkAvailable(1,1) == true){
		//always player center space if available
		playerMove(1,1,2);
		return;
	}else{
		//strategy is always play one close to their last play
		spotx = row - 1;
		if (spotx < 0 or checkAvailable(spotx,column) == false){
			//not valid so move the other way
			spotx += 2;
			if (spotx < 3 and checkAvailable(spotx,column) == true){
				playerMove(spotx, column, 2);
				return;
			}
		}else{
			playerMove(spotx,column, 2);
			return;
		}
		spoty = column - 1;
		if (spoty < 0 or checkAvailable(row, spoty) == false ){
			//not a valid spot so move other way
			spoty += 2;
			if(spoty < 3 and checkAvailable(row,spoty) == true){
				playerMove(row,spoty,2);
				return;
			}
		}else{
			playerMove(row,spoty, 2);
			return;
		}
		//find a available spot
		for (spotx=0;spotx<3;spotx++){
			for(spoty=0;spoty<3;spoty++){
				printf("(%i, %i\n",spotx,spoty);
				if(checkAvailable(spotx,spoty) == true){
					playerMove(spotx,spoty,2);
					return;
				}
			}
		}
	}
}

/*
 * checkAvailable
 * a function that check if a position is available
 * Parameters:
 * 		row: the row position
 * 		column: the column position
 * 	Returns:
 * 		true if available
 * 		false otherwise
 *
 */
GLboolean checkAvailable(GLint row, GLint column){
	if(squares[row][column] == 0){
		return true;
	}else{
		return false;
	}
}

/*
 * sumDiagonal
 * 	a function that sums a diagonal squares
 * 	Parameters:
 * 		direction: 0 for forward direction
 * 				   1 for backward direction
 *
 */
GLint sumDiagonal(GLint direction){
	GLint sum,col,row;
	sum = 0;
	if (direction == 0){
		//forward
		row = 0;
		for(col=0;col<3;col++){
			sum += squares[row][col];
			row ++;
		}
	}else{
		row = 2;
		for(col=0;col<3;col++){
			sum += squares[row][col];
			row --;
		}
	}
	return sum;
}

/*
 * sumColumn
 * 	a function that sums a column
 * 	Parameters:
 * 		column: the column to sum
 * 	Returns:
 * 		sum: the sum of the column
 *
 */
GLint sumColumn(GLint column){
	GLint row;
	GLint sum = 0;
	for(row=0;row<3;row++){
		sum += squares[row][column];
	}
	return sum;
}

/*
 * sumRow
 * 	a function that sums the rows
 *	Parameters:
 *		row: the row to sum
 *	Returns:
 *		sum: the sum of the row
 *
 */
GLint sumRow(GLint row){
	GLint col;
	GLint sum = 0;
	for(col=0;col<3;col++){
		sum += squares[row][col];
	}
	return sum;
}

/*
 * checkZero
 * 	a function that counts the number of zeroes in the row
 * 	Parameters:
 * 		row: the row to count zeroes
 * 	Returns:
 * 		zero: the number of zeroes
 */
GLint checkZero(GLint row){
	GLint col;
	GLint zero = 0;
	for(col=0;col<3;col++){
		if(squares[row][col] == 0){
			zero += 1;
		}
	}
	return zero;
}

/*
 * checkWin
 * 	a function that checks if a player has won
 * 	Parameters:
 * 		none
 * 	Returns:
 * 		win:GLint 0 being no winner,
 * 			1 if player one won ,
 * 			2 if player two won
 */
GLint checkWin(){
	GLint win = 0;
	GLint row,col;
	GLint sum;
	for (row=0;row<3;row++){
		sum = sumRow(row);
		if (sum == 3){
			return 1;
		}else if(sum == 30){
			return 2;
		}
	}
	for (col=0;col<3;col++){
		sum = sumColumn(col);
		if (sum == 3){
			return 1;
		}else if(sum == 30){
			return 2;
		}
	}
	sum = sumDiagonal(0);
	if (sum == 3){
		return 1;
	}else if(sum == 30){
		return 2;
	}
	sum = sumDiagonal(1);
	if (sum == 3){
		return 1;
	}else if(sum == 30){
		return 2;
	}
	if (checkOver() == 1){
		win = 3;
	}
	return win;
}

/*
 * checkOver
 * 	a function to check if game is over (all spots are taken)
 * 	Parameters:
 * 		none
 * 	Returns:
 * 		gameover: an GLint 1 being game over and 0 being game not over
 *
 */
GLint checkOver(){
	GLint sum;
	GLint gameover = 1;
	GLint row = 0;
	while(row < 3){
		sum = checkZero(row);
		if(sum > 0){
			gameover = 0;
		}
		row += 1;
	}
	return gameover;
}

/*
 * displayWinner
 * 	a function to display the winner
 * 	Parameters:
 * 		winner: the player who won
 *
 */
void displayWinner(GLint winner){
	over = winner; //game over
}

/*
 * renderBitmapString
 * 		a function that prints the string at (x,y)
 * 	Parameters:
 * 		x: the x coordinate
 * 		y: the y coordinate
 * 		font: the glut bitmap font
 * 		string: the string to be printed
 */
void renderBitmapString(GLfloat x, GLfloat y, void *font,const char *string){
    const char *c;
    glRasterPos2f(x, y);
    for (c=string; *c != '\0'; c++) {
        glutBitmapCharacter(font, *c);
    }
}

/*
 * mouseDraw
 * the function called when a mouse click occurs
 * Parameters:
 * 	button: the button that was clicked
 * 	action: click down or let go
 * 	xMouse: the x mouse position
 * 	yMouse: the y mouse position
 */
void mouseDraw(GLint button, GLint action, GLint xMouse, GLint yMouse){
	if (action == GLUT_DOWN and button == GLUT_LEFT_BUTTON) {
		if (over == 0){
			GLint row = findRow(yMouse);
			GLint column = findColumn(xMouse);
			if(checkAvailable(row,column) == true){
				playerMove(row,column, playerTurn);
			}else{
				return;
			}
			GLint win = checkWin();
			if (win > 0){
				displayWinner(win);
			}else{
				if (players > 1){
					playerTurn = (playerTurn + 1) % 2; //alternate players
				}else{
					computerMove(row, column);
				}
				win = checkWin();
				if(win > 0){
					displayWinner(win);
				}
			}
			glutPostRedisplay();
		}
	}
}

/*
 * winReshapeFcn
 * 	the function that deals with window resize
 * 	Parameters:
 * 		newWidth: the new window width
 * 		newHeight: the new window height
 *
 */
void winReshapeFcn(GLint newWidth, GLint newHeight){

}

/*
 * menu
 * 	the function to deal with main menu
 * 	Parameters:
 * 		item: the menu item that was clicked
 */
void menu(GLint item){
	if (item == 1){
		newGame();
	}else if(item == 2){
		players = 1;
	}else if(item == 3){
		players = 2;
	}
	else if(item == 4){
		exit(0);
	}
}

/*
 * cpuLevelMenu
 * 	the function to change cpu difficulty level
 * 	Parameters:
 * 		item: the difficulty level
 * 	Returns:
 * 		none
 *
 */
void cpuLevelMenu(GLint item){
	if(item == 1){
		difficulty = 1; //easy
		newGame();
	}else if(item == 2){
		difficulty = 2; //medium
		newGame();
	}else if(item == 3){
		difficulty = 3; //hard
		newGame();
		playerMove(1,1,2); //play center square off the bat
		turn = 0;
		strategy = true;
	}
}

// main function
int main(int argc, char** argv) {
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowPosition(100, 100);
	glutInitWindowSize(winWidth, winHeight);
	windowId = glutCreateWindow(
			"Tic Tac Toe");

	GLint cpuMenuId = glutCreateMenu(cpuLevelMenu);
	glutAddMenuEntry("Easy", 1);
	glutAddMenuEntry("Medium", 2);
	glutAddMenuEntry("Hard", 3);

	//main menu
	glutCreateMenu(menu);
	glutAddMenuEntry("New", 1);
	glutAddMenuEntry("Vs Computer", 2);
	glutAddSubMenu("Cpu Level", cpuMenuId);
	glutAddMenuEntry("Vs Human", 3);
	glutAddMenuEntry("Quit", 4);

	//attach click to menu
	glutAttachMenu(GLUT_RIGHT_BUTTON);

	init();
	// register call back funtions
	glutDisplayFunc(drawList);
	glutReshapeFunc(winReshapeFcn);
	glutMouseFunc(mouseDraw);
	glutMotionFunc(Motion);
	glutMainLoop();
}

