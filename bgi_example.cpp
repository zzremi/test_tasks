// Test task for usage of Borland graphics
// It works in this IDE: https://github.com/maifeeulasad/codeblocks-ep


#define _USE_MATH_DEFINES

#include<cmath>
#include<iostream>
#include<graphics.h>

using namespace std;


class Figure
{
protected:
    int centr_x;
    int centr_y;
    int rad;

public:
    virtual void draw() = 0;
    void readParameters()
    {
        cout << "Enter horizontal x position of center point" << endl;
        cin >> centr_x;
        cout << "Enter vertical position of center point" << endl;
        cin >> centr_y;
        cout << "Enter radius" << endl;
        cin >> rad;
    }
};

class Circle: public Figure
{
public:
    Circle() {readParameters();}
    virtual ~Circle() {}

    void draw()
    {
        circle(centr_x,centr_y,rad);
    }
};

class Square: public Figure
{
public:
    Square() {readParameters();}
    virtual ~Square() {}

    void draw()
    {
        int node_00_x = centr_x - rad;
        int node_00_y = centr_y - rad;
        int node_01_x = centr_x + rad;
        int node_01_y = centr_y - rad;
        int node_10_x = centr_x - rad;
        int node_10_y = centr_y + rad;
        int node_11_x = centr_x + rad;
        int node_11_y = centr_y + rad;

        line(node_00_x,node_00_y,node_01_x,node_01_y);
        line(node_01_x,node_01_y,node_11_x,node_11_y);
        line(node_11_x,node_11_y,node_10_x,node_10_y);
        line(node_10_x,node_10_y,node_00_x,node_00_y);
    }
};

class Triangle: public Figure
{
public:
    Triangle() {readParameters();}
    virtual ~Triangle() {}

    void draw()
    {
        double node_0_x = centr_x;
        double node_0_y = centr_y - rad;
        double node_1_x = centr_x + rad * sin(M_PI / 3);
        double node_1_y = centr_y + rad * 0.5;
        double node_2_x = centr_x - rad * sin(M_PI / 3);;
        double node_2_y = centr_y + rad * 0.5;

        line(node_0_x,node_0_y,node_1_x,node_1_y);
        line(node_1_x,node_1_y,node_2_x,node_2_y);
        line(node_2_x,node_2_y,node_0_x,node_0_y);
    }
};


class MyPolygon: public Figure
{
protected:
    int num;
    int angle;

public:
    MyPolygon()
    {
        readParameters();

        cout << "Enter number points" << endl;
        cin >> num;
        cout << "Enter angle" << endl;
        cin >> angle;
    }

    MyPolygon(int c_x, int c_y, int r, int n, int a = 0)
    {
        centr_x = c_x;
        centr_y = c_y;
        rad = r;
        num = n;
        angle = a;
    }

    virtual ~MyPolygon() {}

    void draw()
    {
        if (num > 2)
        {
            double a0 = M_PI * angle / 180;
            double a1 = 0;

            for (int i = 0; i < num; ++i)
            {
                a1 = a0 + 2 * M_PI / num;
                int p0_x = centr_x + rad * cos(a0);
                int p0_y = centr_y + rad * sin(a0);
                int p1_x = centr_x + rad * cos(a1);
                int p1_y = centr_y + rad * sin(a1);
                a0 = a1;

                line(p0_x,p0_y,p1_x,p1_y);
            }
        }
    }

};

int main()
{
    //first test

    int gd = DETECT, gm;
    initgraph(&gd, &gm, "c:\\tc\\bgi");
    setbkcolor(9);
    cout << gd << " " << gm << endl;

    int option = 0;

    while (option > -1)
    {
        cout << "\n Enter option what to draw: 0 - circle, 1 - square, 2 - triangle, -1 - exit: " << endl;
        cin >> option;

        switch (option)
        {
            case 0:
                {
                    Circle fig;
                    fig.draw();
                    break;
                }
            case 1:
                {
                    Square fig;
                    fig.draw();
                    break;
                }
            case 2:
                {
                    Triangle fig;
                    fig.draw();
                    break;
                }
            default:
                break;
        }
    }

    closegraph();


    //second test

    initgraph(&gd, &gm, "c:\\tc\\bgi");
    setbkcolor(9);
    cout << gd << " " << gm << endl;

//    MyPolygon p;
//    p.draw();

    int num, rad, angle;
    int n_m = 1;

    while (n_m > 0)
    {
        cout << "\n Enter num: " << endl;
        cin >> n_m;

        for (int i = 3; i < n_m + 1; ++i)
        {
            MyPolygon p(250, 250, 200, i, 90);
            p.draw();
        }
    }

    closegraph();

    return 0;
}
