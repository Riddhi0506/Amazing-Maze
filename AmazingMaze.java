import java.util.Random;
import java.util.Scanner;

public class AmazingMaze {
 public static void amazing_Maze(int width, int length) {
        clear();
        print("AMAZING MAZE PROGRAM");
       println();
       //converting program
        int w = width;
        int l = length;
        if (w == 1 || l == 1) return;
        int[][] carry = new int[w + 1][l + 1]; // array declarations
        for (int i = 0; i <= w; i++) {
            carry[i] = new int[l + 1];
        }
        int[][] larr = new int[w + 1][l + 1]; //array declarartion 
        for (int i = 0; i <= w; i++) {
            larr[i] = new int[l + 1];
        }
        int q = 0;
        int z = 0;
        int x = rnd(w);  // #130: #170
        for (int i = 1; i <= w; i++) {  //loop to draw the upper boundary
            if (i == x)
                print(".  ");
            else
                print(".--");
        } // #180
        print(".");
        println(); //#190
        int c = 1;
        carry[x][1] = c;
        c++;//#200
        int p = x;
        int y = 1;
        GOTO(270); //#270
        while (res != -1) {   //loop for case
            switch (res) {       					//Switch-case as per conditions
                case 210:
                    if (p != w)
                        GOTO(250);
                    else
                        GOTO(220);
                    continue;
                case 220:
                    if (y != l)
                        GOTO(240);
                    else
                        GOTO(230);
                    continue;
                case 230:
                    p = 1;
                    y = 1;
                    GOTO(260);
                    continue;
                case 240:
                    p = 1;
                    y++;
                    GOTO(260);
                    continue;
                case 250:
                    p++;
                    GOTO(260);
                    continue;
                case 260:
                    if (carry[p][y] == 0)
                        GOTO(210);
                    else
                        GOTO(270);
                    continue;
                case 270:
                    if (p - 1 == 0)
                        GOTO(600);
                    else
                        GOTO(280);
                    continue;
                case 280:
                    if (carry[p - 1][y] != 0)
                        GOTO(600);
                    else
                        GOTO(290);
                    continue;
                case 290:
                    if (y - 1 == 0)
                        GOTO(430);
                    else
                        GOTO(300);
                    continue;
                case 300:
                    if (carry[p][y - 1] != 0)
                        GOTO(430);
                    else
                        GOTO(310);
                    continue;
                case 310:
                    if (p == w)
                        GOTO(350);
                    else
                        GOTO(320);
                    continue;
                case 320:
                    if (carry[p + 1][y] != 0)
                        GOTO(350);
                    else
                        GOTO(330);
                    continue;
                case 330:
                    x = rnd(3);
                    GOTO(340);
                    continue;
                case 340:
                    if (x == 1)
                        GOTO(940);
                    else if (x == 2)
                        GOTO(980);
                    else if (x == 3)
                        GOTO(1020);
                    else
                        GOTO(350);
                    continue;
                case 350:
                    if (y != l)
                        GOTO(380);
                    else
                        GOTO(360);
                    continue;
                case 360:
                    if (z == 1)
                        GOTO(410);
                    else
                        GOTO(370);
                    continue;
                case 370:
                    q = 1;
                    GOTO(390);
                    continue;
                case 380:
                    if (carry[p][y + 1] != 0)
                        GOTO(410);
                    else
                        GOTO(390);
                    continue;
                case 390:
                    x = rnd(3);
                    GOTO(400);
                    continue;
                case 400:
                    if (x == 1)
                        GOTO(940);
                    else if (x == 2)
                        GOTO(980);
                    else if (x == 3)
                        GOTO(1090);
                    else
                        GOTO(410);
                    continue;
                case 410:
                    x = rnd(2);
                    GOTO(420);
                    continue;
                case 420:
                    if (x == 1)
                        GOTO(940);
                    else if (x == 2)
                        GOTO(980);
                    else
                        GOTO(430);
                    continue;
                case 430:
                    if (p == w)
                        GOTO(530);
                    else
                        GOTO(440);
                    continue;
                case 440:
                    if (carry[p + 1][y] != 0)
                        GOTO(530);
                    else
                        GOTO(450);
                    continue;
                case 450:
                    if (y != l)
                        GOTO(480);
                    else
                        GOTO(460);
                    continue;
                case 460:
                    if (z == 1)
                        GOTO(510);
                    else
                        GOTO(470);
                    continue;
                case 470:
                    q = 1;
                    GOTO(490);
                    continue;
                case 480:
                    if (carry[p][y + 1] != 0)
                        GOTO(510);
                    else
                        GOTO(490);
                    continue;
                case 490:
                    x = rnd(3);
                    GOTO(500);
                    continue;
                case 500:
                    if (x == 1)
                        GOTO(940);
                    else if (x == 2)
                        GOTO(1020);
                    else if (x == 3)
                        GOTO(1090);
                    else
                        GOTO(510);
                    continue;
                case 510:
                    x = rnd(2);
                    GOTO(520);
                    continue;
                case 520:
                    if (x == 1)
                        GOTO(940);
                    else if (x == 2)
                        GOTO(1020);
                    else
                        GOTO(530);
                    continue;
                case 530:
                    if (y != l)
                        GOTO(560);
                    else
                        GOTO(540);
                    continue;
                case 540:
                    if (z == 1)
                        GOTO(590);
                    else
                        GOTO(550);
                    continue;
                case 550:
                    q = 1;
                    GOTO(570);
                    continue;
                case 560:
                    if (carry[p][y + 1] != 0)
                        GOTO(590);
                    else
                        GOTO(570);
                    continue;
                case 570:
                    x = rnd(2);
                    GOTO(580);
                    continue;
                case 580:
                    if (x == 1)
                        GOTO(940);
                    else if (x == 2)
                        GOTO(1090);
                    else
                        GOTO(590);
                    continue;
                case 590:
                    GOTO(940);
                    continue;
                case 600:
                    if (y - 1 == 0)
                        GOTO(790);
                    else
                        GOTO(610);
                    continue;
                case 610:
                    if (carry[p][y - 1] != 0)
                        GOTO(790);
                    else
                        GOTO(620);
                    continue;
                case 620:
                    if (p == w)
                        GOTO(720);
                    else
                        GOTO(630);
                    continue;
                case 630:
                    if (carry[p + 1][y] != 0)
                        GOTO(720);
                    else
                        GOTO(640);
                    continue;
                case 640:
                    if (y != l)
                        GOTO(670);
                    else
                        GOTO(650);
                    continue;
                case 650:
                    if (z == 1)
                        GOTO(700);
                    else
                        GOTO(660);
                    continue;
                case 660:
                    q = 1;
                    GOTO(680);
                    continue;
                case 670:
                    if (carry[p][y + 1] != 0)
                        GOTO(700);
                    else
                        GOTO(680);
                    continue;
                case 680:
                    x = rnd(3);
                    GOTO(690);
                    continue;
                case 690:
                    if (x == 1)
                        GOTO(980);
                    else if (x == 2)
                        GOTO(1020);
                    else if (x == 3)
                        GOTO(1090);
                    else
                        GOTO(700);
                    continue;
                case 700:
                    x = rnd(2);
                    GOTO(710);
                    continue;
                case 710:
                    if (x == 1)
                        GOTO(980);
                    else if (x == 2)
                        GOTO(1020);
                    else
                        GOTO(720);
                    continue;
                case 720:
                    if (y != l)
                        GOTO(750);
                    else
                        GOTO(730);
                    continue;
                case 730:
                    if (z == 1)
                        GOTO(780);
                    else
                        GOTO(740);
                    continue;
                case 740:
                    q = 1;
                    GOTO(760);
                    continue;
                case 750:
                    if (carry[p][y + 1] != 0)
                        GOTO(780);
                    else
                        GOTO(760);
                    continue;
                case 760:
                    x = rnd(2);
                    GOTO(770);
                    continue;
                case 770:
                    if (x == 1)
                        GOTO(980);
                    else if (x == 2)
                        GOTO(1090);
                    else
                        GOTO(780);
                    continue;
                case 780:
                    GOTO(980);
                    continue;
                case 790:
                    if (p == w)
                        GOTO(880);
                    else
                        GOTO(800);
                    continue;
                case 800:
                    if (carry[p + 1][y] != 0)
                        GOTO(880);
                    else
                        GOTO(810);
                    continue;
                case 810:
                    if (y != l)
                        GOTO(840);
                    else
                        GOTO(820);
                    continue;
                case 820:
                    if (z == 1)
                        GOTO(870);
                    else
                        GOTO(830);
                    continue;
                case 830:
                    q = 1;
                    GOTO(990);
                    continue;
                case 840:
                    if (carry[p][y + 1] != 0)
                        GOTO(870);
                    else
                        GOTO(850);
                    continue;
                case 850:
                    x = rnd(2);
                    GOTO(860);
                    continue;
                case 860:
                    if (x == 1)
                        GOTO(1020);
                    else if (x == 2)
                        GOTO(1090);
                    else
                        GOTO(870);
                    continue;
                case 870:
                    GOTO(1020);
                    continue;
                case 880:
                    if (y != l)
                        GOTO(910);
                    else
                        GOTO(890);
                    continue;
                case 890:
                    if (z == 1)
                        GOTO(930);
                    else
                        GOTO(900);
                    continue;
                case 900:
                    q = 1;
                    GOTO(920);
                    continue;
                case 910:
                    if (carry[p][y + 1] != 0)
                        GOTO(930);
                    else
                        GOTO(920);
                    continue;
                case 920:
                    GOTO(1090);
                    continue;
                case 930:
                    GOTO(1190);
                    continue;
                case 940:
                    carry[p - 1][y] = c;
                    GOTO(950);
                    continue;
                case 950:
                    c++;
                    larr[p - 1][y] = 2;
                    p--;
                    GOTO(960);
                    continue;
                case 960:
                    if (c == w * l + 1)
                        GOTO(1200);
                    else
                        GOTO(970);
                    continue;
                case 970:
                    q = 0;
                    GOTO(270);
                    continue;
                case 980:
                   carry[p][y - 1] = c;
                    GOTO(990);
                    continue;
                case 990:
                    c++;
                    GOTO(1000);
                    continue;
                case 1000:
                    larr[p][y - 1] = 1;
                    y--;
                    if (c == w * l + 1)
                        GOTO(1200);
                    else
                        GOTO(1010);
                    continue;
                case 1010:
                    q = 0;
                    GOTO(270);
                    continue;
                case 1020:
                   carry[p + 1][y] = c;
                    GOTO(1030);
                    continue;
                case 1030:
                    c++;
                    if (larr[p][y] == 0)
                        GOTO(1050);
                    else
                        GOTO(1040);
                    continue;
                case 1040:
                    larr[p][y] = 3;
                    GOTO(1060);
                    continue;
                case 1050:
                    larr[p][y] = 2;
                    GOTO(1060);
                    continue;
                case 1060:
                    p++;
                    GOTO(1070);
                    continue;
                case 1070:
                    if (c == w * l + 1)
                        GOTO(1200);
                    else
                        GOTO(1080);
                    continue;
                case 1080:
                    GOTO(600);
                    continue;
                case 1090:
                    if (q == 1)
                        GOTO(1150);
                    else
                        GOTO(1100);
                    continue;
                case 1100:
                	carry[p][y + 1] = c;
                    c++;
                    if (larr[p][y] == 0)
                        GOTO(1120);
                    else
                        GOTO(1110);
                    continue;
                case 1110:
                    larr[p][y] = 3;
                    GOTO(1130);
                    continue;
                case 1120:
                    larr[p][y] = 1;
                    GOTO(1130);
                    continue;
                case 1130:
                    y++;
                    if (c == l * w + 1)
                        GOTO(1200);
                    else
                        GOTO(1140);
                    continue;
                case 1140:
                    GOTO(270);
                    continue;
                case 1150:
                    z = 1;
                    GOTO(1160);
                    continue;
                case 1160:
                    if (larr[p][y] == 0)
                        GOTO(1180);
                    else
                        GOTO(1170);
                    continue;
                case 1170:
                    larr[p][y] = 3;
                    q = 0;
                    GOTO(1190);
                    continue;
                case 1180:
                    larr[p][y] = 1;
                    q = 0;
                    p = 1;
                    y = 1;
                    GOTO(260);
                    continue;
                case 1190:
                    GOTO(210);
                    continue;
                case 1200:
                    res = -1;
                    continue;
            }
        }// #1200:
        for (int j = 1; j <= l; j++) {  //loop to indicate border
            print("I");// #1210

            for (int i = 1; i <= w; i++) {
                if (larr[i][j] >= 2)
                    print("   ");  // #1240
                else
                    print("  I");  // #1260
            }
            print(" "); // #1280
            println();
            for (int i = 1; i <= w; i++) {
                if (larr[i][j] == 0)
                    print(":--");   // #1300, #1340
                else if (larr[i][j] == 2)
                    print(":--");  // #1310, #1340
                else
                    print(":  "); // #1320
            }
            print(":");// #1360
            println();
        }
    }
 static int res = 0;      // where GOTO goes
 public static Random an = new Random(0);
 static StringBuffer sb = new StringBuffer(); // creating object 
 private static void clear() {
     sb.setLength(0);
 }
 private static void println() {
     sb.append("\n");    
 }
 public static void print(String in) {
     sb.append(in); // appending text
 }
 public static int rnd(int cnt) {
     return (int) (cnt * an.nextFloat()) + 1;
 }
 public static void GOTO(int l_no) {
     res = l_no;
 }
    public static void main(String[] args) {
    	Scanner sc= new Scanner(System.in);  //System.in is a standard input stream  and take input
    	int hori, veri;
    	while(true) {
    	System.out.println("WHAT ARE YOUR WIDTH AND LENGTH:   ");  
    	 hori= sc.nextInt(); 
    	 veri=sc.nextInt();
    	if(hori<=1 && veri<=1) {
    		System.out.println("MEANINGLESS DIMENSIONS....TRY AGAIN");
    		}
    	else {break;}}   	
    	amazing_Maze(hori, veri);
        System.out.println(sb);   	
    }
}
