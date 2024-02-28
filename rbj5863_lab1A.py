import random

class Maze:
    GOTO_final_position = 0
    # random = random.seed(0)
    output = []

    def main(args):
        print(" " * 28 + "AMAZING PROGRAM")
        print(" " * 15 + "CREATIVE COMPUTING MORRISTOWN, NEW JERSEY\n\n\n")
        while True:    
            try:    
                width,length = input("How much width and length you wish to have (width length): ").split(' ')
                width = int(width)
                length = int(length)
                break
            except ValueError:
                print("Invalid input. Please try again by providing 2 number having space.")
                continue

        Maze.amazing(width, length)
        for i in Maze.output:
            print(i, end="")

    def display(text):
        Maze.output.append(text)

    def rnd(count):
        return int((count * random.random())) + 1

    def amazing(width, length):
        del Maze.output[:]
        Maze.output.append("\n")
        h = width
        v = length
        if (h == 1 or v == 1):
            print("Meaningless Dimensions. Try Again.")
            Maze.GOTO_final_position = 100
            return
        wArray = [[0 for _ in range(v + 1)] for _ in range(h + 1)]

        i = 0
        while (i <= h):
            wArray[i] = [0] * (v + 1)
            i += 1
 
        vArray = [[0 for _ in range(v + 1)] for _ in range(h + 1)]
        i = 0
        while (i <= h):
            vArray[i] = [0] * (v + 1)
            i += 1
        q = 0
        z = 0
        x = Maze.rnd(h)
        # 130:170
        i = 1
        while (i <= h):
            if (i == x):
                Maze.display(".  ")
            else:
                Maze.display(".--")
            i += 1
        # 180
        Maze.display(".")
        Maze.output.append("\n")
        # 190
        c = 1
        wArray[x][1] = c
        c += 1
        # 200
        r = x
        s = 1
        Maze.GOTO_final_position = 270
        random.seed()
        while (Maze.GOTO_final_position != -1):
            if (Maze.GOTO_final_position == 210):
                if (r != h):
                    Maze.GOTO_final_position = 250
                else:
                    Maze.GOTO_final_position = 220
                continue
            elif (Maze.GOTO_final_position == 220):
                if (s != v):
                    Maze.GOTO_final_position = 240
                else:
                    Maze.GOTO_final_position = 230
                continue
            elif (Maze.GOTO_final_position == 230):
                r = 1
                s = 1
                Maze.GOTO_final_position = 260
                continue
            elif (Maze.GOTO_final_position == 240):
                r = 1
                s += 1
                Maze.GOTO_final_position = 260
                continue
            elif (Maze.GOTO_final_position == 250):
                r += 1
                Maze.GOTO_final_position = 260
                continue
            elif (Maze.GOTO_final_position == 260):
                if (wArray[r][s] == 0):
                    Maze.GOTO_final_position = 210
                else:
                    Maze.GOTO_final_position = 270
                continue
            elif (Maze.GOTO_final_position == 270):
                if (r - 1 == 0):
                    Maze.GOTO_final_position = 600
                else:
                    Maze.GOTO_final_position = 280
                continue
            elif (Maze.GOTO_final_position == 280):
                if (wArray[r - 1][s] != 0):
                    Maze.GOTO_final_position = 600
                else:
                    Maze.GOTO_final_position = 290
                continue
            elif (Maze.GOTO_final_position == 290):
                if (s - 1 == 0):
                    Maze.GOTO_final_position = 430
                else:
                    Maze.GOTO_final_position = 300
                continue
            elif (Maze.GOTO_final_position == 300):
                if (wArray[r][s - 1] != 0):
                    Maze.GOTO_final_position = 430
                else:
                    Maze.GOTO_final_position = 310
                continue
            elif (Maze.GOTO_final_position == 310):
                if (r == h):
                    Maze.GOTO_final_position = 350
                else:
                    Maze.GOTO_final_position = 320
                continue
            elif (Maze.GOTO_final_position == 320):
                if (wArray[r + 1][s] != 0):
                    Maze.GOTO_final_position = 350
                else:
                    Maze.GOTO_final_position = 330
                continue
            elif (Maze.GOTO_final_position == 330):
                x = Maze.rnd(3)
                Maze.GOTO_final_position = 340
                continue
            elif (Maze.GOTO_final_position == 340):
                if (x == 1):
                    Maze.GOTO_final_position = 940
                elif (x == 2):
                    Maze.GOTO_final_position = 980
                elif (x == 3):
                    Maze.GOTO_final_position = 1020
                else:
                    Maze.GOTO_final_position = 350
                continue
            elif (Maze.GOTO_final_position == 350):
                if (s != v):
                    Maze.GOTO_final_position = 380
                else:
                    Maze.GOTO_final_position = 360
                continue
            elif (Maze.GOTO_final_position == 360):
                if (z == 1):
                    Maze.GOTO_final_position = 410
                else:
                    Maze.GOTO_final_position = 370
                continue
            elif (Maze.GOTO_final_position == 370):
                q = 1
                Maze.GOTO_final_position = 390
                continue
            elif (Maze.GOTO_final_position == 380):
                if (wArray[r][s + 1] != 0):
                    Maze.GOTO_final_position = 410
                else:
                    Maze.GOTO_final_position = 390
                continue
            elif (Maze.GOTO_final_position == 390):
                x = Maze.rnd(3)
                Maze.GOTO_final_position = 400
                continue
            elif (Maze.GOTO_final_position == 400):
                if (x == 1):
                    Maze.GOTO_final_position = 940
                elif (x == 2):
                    Maze.GOTO_final_position = 980
                elif (x == 3):
                    Maze.GOTO_final_position = 1090
                else:
                    Maze.GOTO_final_position = 410
                continue
            elif (Maze.GOTO_final_position == 410):
                x = Maze.rnd(2)
                Maze.GOTO_final_position = 420
                continue
            elif (Maze.GOTO_final_position == 420):
                if (x == 1):
                    Maze.GOTO_final_position = 940
                elif (x == 2):
                    Maze.GOTO_final_position = 980
                else:
                    Maze.GOTO_final_position = 430
                continue
            elif (Maze.GOTO_final_position == 430):
                if (r == h):
                    Maze.GOTO_final_position = 530
                else:
                    Maze.GOTO_final_position = 440
                continue
            elif (Maze.GOTO_final_position == 440):
                if (wArray[r + 1][s] != 0):
                    Maze.GOTO_final_position = 530
                else:
                    Maze.GOTO_final_position = 450
                continue
            elif (Maze.GOTO_final_position == 450):
                if (s != v):
                    Maze.GOTO_final_position = 480
                else:
                    Maze.GOTO_final_position = 460
                continue
            elif (Maze.GOTO_final_position == 460):
                if (z == 1):
                    Maze.GOTO_final_position = 510
                else:
                    Maze.GOTO_final_position = 470
                continue
            elif (Maze.GOTO_final_position == 470):
                q = 1
                Maze.GOTO_final_position = 490
                continue
            elif (Maze.GOTO_final_position == 480):
                if (wArray[r][s + 1] != 0):
                    Maze.GOTO_final_position = 510
                else:
                    Maze.GOTO_final_position = 490
                continue
            elif (Maze.GOTO_final_position == 490):
                x = Maze.rnd(3)
                Maze.GOTO_final_position = 500
                continue
            elif (Maze.GOTO_final_position == 500):
                if (x == 1):
                    Maze.GOTO_final_position = 940
                elif (x == 2):
                    Maze.GOTO_final_position = 1020
                elif (x == 3):
                    Maze.GOTO_final_position = 1090
                else:
                    Maze.GOTO_final_position = 510
                continue
            elif (Maze.GOTO_final_position == 510):
                x = Maze.rnd(2)
                Maze.GOTO_final_position = 520
                continue
            elif (Maze.GOTO_final_position == 520):
                if (x == 1):
                    Maze.GOTO_final_position = 940
                elif (x == 2):
                    Maze.GOTO_final_position = 1020
                else:
                    Maze.GOTO_final_position = 530
                continue
            elif (Maze.GOTO_final_position == 530):
                if (s != v):
                    Maze.GOTO_final_position = 560
                else:
                    Maze.GOTO_final_position = 540
                continue
            elif (Maze.GOTO_final_position == 540):
                if (z == 1):
                    Maze.GOTO_final_position = 590
                else:
                    Maze.GOTO_final_position = 550
                continue
            elif (Maze.GOTO_final_position == 550):
                q = 1
                Maze.GOTO_final_position = 570
                continue
            elif (Maze.GOTO_final_position == 560):
                if (wArray[r][s + 1] != 0):
                    Maze.GOTO_final_position = 590
                else:
                    Maze.GOTO_final_position = 570
                continue
            elif (Maze.GOTO_final_position == 570):
                x = Maze.rnd(2)
                Maze.GOTO_final_position = 580
                continue
            elif (Maze.GOTO_final_position == 580):
                if (x == 1):
                    Maze.GOTO_final_position = 940
                elif (x == 2):
                    Maze.GOTO_final_position = 1090
                else:
                    Maze.GOTO_final_position = 590
                continue
            elif (Maze.GOTO_final_position == 590):
                Maze.GOTO_final_position = 940
                continue
            elif (Maze.GOTO_final_position == 600):
                if (s - 1 == 0):
                    Maze.GOTO_final_position = 790
                else:
                    Maze.GOTO_final_position = 610
                continue
            elif (Maze.GOTO_final_position == 610):
                if (wArray[r][s - 1] != 0):
                    Maze.GOTO_final_position = 790
                else:
                    Maze.GOTO_final_position = 620
                continue
            elif (Maze.GOTO_final_position == 620):
                if (r == h):
                    Maze.GOTO_final_position = 720
                else:
                    Maze.GOTO_final_position = 630
                continue
            elif (Maze.GOTO_final_position == 630):
                if (wArray[r + 1][s] != 0):
                    Maze.GOTO_final_position = 720
                else:
                    Maze.GOTO_final_position = 640
                continue
            elif (Maze.GOTO_final_position == 640):
                if (s != v):
                    Maze.GOTO_final_position = 670
                else:
                    Maze.GOTO_final_position = 650
                continue
            elif (Maze.GOTO_final_position == 650):
                if (z == 1):
                    Maze.GOTO_final_position = 700
                else:
                    Maze.GOTO_final_position = 660
                continue
            elif (Maze.GOTO_final_position == 660):
                q = 1
                Maze.GOTO_final_position = 680
                continue
            elif (Maze.GOTO_final_position == 670):
                if (wArray[r][s + 1] != 0):
                    Maze.GOTO_final_position = 700
                else:
                    Maze.GOTO_final_position = 680
                continue
            elif (Maze.GOTO_final_position == 680):
                x = Maze.rnd(3)
                Maze.GOTO_final_position = 690
                continue
            elif (Maze.GOTO_final_position == 690):
                if (x == 1):
                    Maze.GOTO_final_position = 980
                elif (x == 2):
                    Maze.GOTO_final_position = 1020
                elif (x == 3):
                    Maze.GOTO_final_position = 1090
                else:
                    Maze.GOTO_final_position = 700
                continue
            elif (Maze.GOTO_final_position == 700):
                x = Maze.rnd(2)
                Maze.GOTO_final_position = 710
                continue
            elif (Maze.GOTO_final_position == 710):
                if (x == 1):
                    Maze.GOTO_final_position = 980
                elif (x == 2):
                    Maze.GOTO_final_position = 1020
                else:
                    Maze.GOTO_final_position = 720
                continue
            elif (Maze.GOTO_final_position == 720):
                if (s != v):
                    Maze.GOTO_final_position = 750
                else:
                    Maze.GOTO_final_position = 730
                continue
            elif (Maze.GOTO_final_position == 730):
                if (z == 1):
                    Maze.GOTO_final_position = 780
                else:
                    Maze.GOTO_final_position = 740
                continue
            elif (Maze.GOTO_final_position == 740):
                q = 1
                Maze.GOTO_final_position = 760
                continue
            elif (Maze.GOTO_final_position == 750):
                if (wArray[r][s + 1] != 0):
                    Maze.GOTO_final_position = 780
                else:
                    Maze.GOTO_final_position = 760
                continue
            elif (Maze.GOTO_final_position == 760):
                x = Maze.rnd(2)
                Maze.GOTO_final_position = 770
                continue
            elif (Maze.GOTO_final_position == 770):
                if (x == 1):
                    Maze.GOTO_final_position = 980
                elif (x == 2):
                    Maze.GOTO_final_position = 1090
                else:
                    Maze.GOTO_final_position = 780
                continue
            elif (Maze.GOTO_final_position == 780):
                Maze.GOTO_final_position = 980
                continue
            elif (Maze.GOTO_final_position == 790):
                if (r == h):
                    Maze.GOTO_final_position = 880
                else:
                    Maze.GOTO_final_position = 800
                continue
            elif (Maze.GOTO_final_position == 800):
                if (wArray[r + 1][s] != 0):
                    Maze.GOTO_final_position = 880
                else:
                    Maze.GOTO_final_position = 810
                continue
            elif (Maze.GOTO_final_position == 810):
                if (s != v):
                    Maze.GOTO_final_position = 840
                else:
                    Maze.GOTO_final_position = 820
                continue
            elif (Maze.GOTO_final_position == 820):
                if (z == 1):
                    Maze.GOTO_final_position = 870
                else:
                    Maze.GOTO_final_position = 830
                continue
            elif (Maze.GOTO_final_position == 830):
                q = 1
                Maze.GOTO_final_position = 990
                continue
            elif (Maze.GOTO_final_position == 840):
                if (wArray[r][s + 1] != 0):
                    Maze.GOTO_final_position = 870
                else:
                    Maze.GOTO_final_position = 850
                continue
            elif (Maze.GOTO_final_position == 850):
                x = Maze.rnd(2)
                Maze.GOTO_final_position = 860
                continue
            elif (Maze.GOTO_final_position == 860):
                if (x == 1):
                    Maze.GOTO_final_position = 1020
                elif (x == 2):
                    Maze.GOTO_final_position = 1090
                else:
                    Maze.GOTO_final_position = 870
                continue
            elif (Maze.GOTO_final_position == 870):
                Maze.GOTO_final_position = 1020
                continue
            elif (Maze.GOTO_final_position == 880):
                if (s != v):
                    Maze.GOTO_final_position = 910
                else:
                    Maze.GOTO_final_position = 890
                continue
            elif (Maze.GOTO_final_position == 890):
                if (z == 1):
                    Maze.GOTO_final_position = 930
                else:
                    Maze.GOTO_final_position = 900
                continue
            elif (Maze.GOTO_final_position == 900):
                q = 1
                Maze.GOTO_final_position = 920
                continue
            elif (Maze.GOTO_final_position == 910):
                if (wArray[r][s + 1] != 0):
                    Maze.GOTO_final_position = 930
                else:
                    Maze.GOTO_final_position = 920
                continue
            elif (Maze.GOTO_final_position == 920):
                Maze.GOTO_final_position = 1090
                continue
            elif (Maze.GOTO_final_position == 930):
                Maze.GOTO_final_position = 1190
                continue
            elif (Maze.GOTO_final_position == 940):
                wArray[r - 1][s] = c
                Maze.GOTO_final_position = 950
                continue
            elif (Maze.GOTO_final_position == 950):
                c += 1
                vArray[r - 1][s] = 2
                r -= 1
                Maze.GOTO_final_position = 960
                continue
            elif (Maze.GOTO_final_position == 960):
                if (c == h * v + 1):
                    Maze.GOTO_final_position = 1200
                else:
                    Maze.GOTO_final_position = 970
                continue
            elif (Maze.GOTO_final_position == 970):
                q = 0
                Maze.GOTO_final_position = 270
                continue
            elif (Maze.GOTO_final_position == 980):
                wArray[r][s - 1] = c
                Maze.GOTO_final_position = 990
                continue
            elif (Maze.GOTO_final_position == 990):
                c += 1
                Maze.GOTO_final_position = 1000
                continue
            elif (Maze.GOTO_final_position == 1000):
                vArray[r][s - 1] = 1
                s -= 1
                if (c == h * v + 1):
                    Maze.GOTO_final_position = 1200
                else:
                    Maze.GOTO_final_position = 1010
                continue
            elif (Maze.GOTO_final_position == 1010):
                q = 0
                Maze.GOTO_final_position = 270
                continue
            elif (Maze.GOTO_final_position == 1020):
                wArray[r + 1][s] = c
                Maze.GOTO_final_position = 1030
                continue
            elif (Maze.GOTO_final_position == 1030):
                c += 1
                if (vArray[r][s] == 0):
                    Maze.GOTO_final_position = 1050
                else:
                    Maze.GOTO_final_position = 1040
                continue
            elif (Maze.GOTO_final_position == 1040):
                vArray[r][s] = 3
                Maze.GOTO_final_position = 1060
                continue
            elif (Maze.GOTO_final_position == 1050):
                vArray[r][s] = 2
                Maze.GOTO_final_position = 1060
                continue
            elif (Maze.GOTO_final_position == 1060):
                r += 1
                Maze.GOTO_final_position = 1070
                continue
            elif (Maze.GOTO_final_position == 1070):
                if (c == h * v + 1):
                    Maze.GOTO_final_position = 1200
                else:
                    Maze.GOTO_final_position = 1080
                continue
            elif (Maze.GOTO_final_position == 1080):
                Maze.GOTO_final_position = 600
                continue
            elif (Maze.GOTO_final_position == 1090):
                if (q == 1):
                    Maze.GOTO_final_position = 1150
                else:
                    Maze.GOTO_final_position = 1100
                continue
            elif (Maze.GOTO_final_position == 1100):
                wArray[r][s + 1] = c
                c += 1
                if (vArray[r][s] == 0):
                    Maze.GOTO_final_position = 1120
                else:
                    Maze.GOTO_final_position = 1110
                continue
            elif (Maze.GOTO_final_position == 1110):
                vArray[r][s] = 3
                Maze.GOTO_final_position = 1130
                continue
            elif (Maze.GOTO_final_position == 1120):
                vArray[r][s] = 1
                Maze.GOTO_final_position = 1130
                continue
            elif (Maze.GOTO_final_position == 1130):
                s += 1
                if (c == v * h + 1):
                    Maze.GOTO_final_position = 1200
                else:
                    Maze.GOTO_final_position = 1140
                continue
            elif (Maze.GOTO_final_position == 1140):
                Maze.GOTO_final_position = 270
                continue
            elif (Maze.GOTO_final_position == 1150):
                z = 1
                Maze.GOTO_final_position = 1160
                continue
            elif (Maze.GOTO_final_position == 1160):
                if (vArray[r][s] == 0):
                    Maze.GOTO_final_position = 1180
                else:
                    Maze.GOTO_final_position = 1170
                continue
            elif (Maze.GOTO_final_position == 1170):
                vArray[r][s] = 3
                q = 0
                Maze.GOTO_final_position = 1190
                continue
            elif (Maze.GOTO_final_position == 1180):
                vArray[r][s] = 1
                q = 0
                r = 1
                s = 1
                Maze.GOTO_final_position = 260
                continue
            elif (Maze.GOTO_final_position == 1190):
                Maze.GOTO_final_position = 210
                continue
            elif (Maze.GOTO_final_position == 1200):
                Maze.GOTO_final_position = -1
                continue
        # 1200:
        j = 1
        while (j <= v):
            Maze.display("I")
            # 1210
            i = 1
            while (i <= h):
                if (vArray[i][j] >= 2):
                    Maze.display("   ")
                else:
                    Maze.display("  I")
                i += 1
            Maze.display(" ")
            # 1280
            Maze.output.append("\n")
            i = 1
            while (i <= h):
                if (vArray[i][j] == 0):
                    Maze.display(".--")
                elif (vArray[i][j] == 2):
                    Maze.display(".--")
                else:
                    Maze.display(".  ")
                i += 1
            Maze.display(".")
            # 1360
            Maze.output.append("\n")
            j += 1


if __name__ == "__main__":
    Maze.main([])
    # print("\n")
