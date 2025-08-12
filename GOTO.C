#include<stdio.h>
#include<conio.h>

void main()
{
	int x;
	clrscr();
	Rangai:
	printf("\nEnter x : ");
	scanf("%d",&x);
	if(x>0)
	{
		printf("\nSquare of %d is %d",x,x*x);
	}
	else
	{
		goto Rangai;
	}

	getch();
}