#include <cstdlib>
#include <cstdio>
#include <cmath>

using namespace std;


//��� ��������������� �������

double lmtr(void)
{    //���������� ����� ���������� ��������
	double eps = 1e-8, x = 1.22, y = -1;       
    while (y<0)
	{
        y=x*x*x*x-x-1;
        x=x+eps;
    }
    return x-eps;
} 

double lm(void)
{    //���������� ����� ������ ����������
	double eps = 1e-8, x = 1.24, y = -1;      
    while (y<0)
	{
        y=x*x*x+x*x-2*x-1;
        x=x+eps;
    }
    return x-eps;
} 

double kor(double x, int n)
{        //���������� ����� �� x n-�� ������� 
    double eps = 1e-8, y = 1.22, t = 1;               
	for (int i = 0; i<n; ++i) 
		t*=y;
    if (t<x) 
		y=y+eps;
    else
		return y-eps;
}

int rec(double q0, double q1, double q2, double q3, 
           int it, int n, int r, double *cur, double l)
{
//����������� ���������� ���������� �������� ������������������ �� ���� ���������
//     q0, q1, q2, q3 - ��������� 4 ��������� �������� 
//     it - ���������� ����� �������, n - ���������� ����� �������� ������� �������� ������
//     r - ����������� �� ������ ������� �� ���������� ���� 
//     ���� �� ���� ������, ������� �� ���������, �� ��� ������� ���������� ��������
//     cur - ������ ������� ��������� ���� ��������� �� N, ������������, ����� �� ������� ���
//     �������  n ������, l - ����� �� (1,2) 
	 
     if(q3<cur[it+3]) 
		cur[it+3]=q3;     
									 //��������� �� ������-�� �������� - 
                                     //���������� � ������� ��������� 

    if(it<n-3)
	{  								 //������, ����� ��� ���� ������� ��������� ��������: ���������� ��� �����������
		double t = l*q1;                  
        double x = q0+q1;
        if (t<q2) 
			t = q2;
			
        double u = q3;
        if (u<t) 
			u=t;
        if (x<u) 
			x=u;                         
        
		rec(q1,t,u,x,it+1,n,0,cur,l);
		if (it<3) 
			printf("+");                                                    
                            
        x = q0+q1;
        t = (2-l)*q1+q0;
        if (t<q3) 
			t=q3;
        if (x<t) 
			x=t;
        
		rec(q1,q2,t,x,it+1,n,0,cur,l);                                       
		if(it<3) 
			printf("+");                             
   
        if (r==0)
		{                       
            t = q0+q2;
            if (t<q3) 
				t=q3;
            rec(q1,q2,q3,t,it+1,n,1,cur,l);
        }
     }
                    
     return 0;     
}
                    

int main(void)
{
	double *m; 
	m = new double [100];
	
	for(int i=0; i<100; ++i) 
		m[i] = 66666666;     
   
	double la = lm(); 
	double tet = lmtr();
	printf("    tet=%lf   la=%lf  \n    N=",tet,la);
	
	int n;
	scanf("%d",&n);
   
	double l = la;                //����� �� (1,2), ���� 1.2469..., ���� ����������� ����� � ����������
//	double l = 1.298;             //� ���� �������, �� ������� � ���������� ������ �������� �����
//	double l = 1.293;
	
	double t = tet;               //�������� ���� (q_0=1, q_1=t, q_2=t*t, q_3=t*t*t)
//	double t = 1.22785;           //�������� ����� ������ �� 1.220 �� ...
   
	printf("    l=%.6lf  t=%.6lf  \n \n",l,t);
	printf("                                                ________________________\n");
	printf("                                                ");
	
	//C������ �� ��������� N   
	rec(1,t,t*t,t*t*t,0,n,0,m,l);
	printf("   \n\n");   
      
	for (int i=3; i<n+1; ++i)
	{   
		printf("  n=%d  min(q_n)=  %.6lf  |",i,m[i]);
		double ep = kor(m[i],i);
		printf("  (min(q_n))^(1/n)=  %.6lf  \n",ep);
	}
         
	scanf("%d",&n);
	return 0;
}
 
 