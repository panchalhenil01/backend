#include<stdio.h>
#include<conio.h>

void main()
{
	double a,b,*p,*q;
	clrscr();
	a=10;
	p=&a;
	b=20;
	p=&b;
	printf("\na : %If",a);
	printf("\np : %u",p);
	printf("\n*p : %If",*p);
	printf("\nb : %If",b);
	printf("\nq : %u",q);
	printf("\n*q : %If",*q);
	getch();
}
