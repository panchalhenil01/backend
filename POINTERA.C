#include<stdio.h>
#include<conio.h>

void main()
{
	int a[5],i,*p;
	clrscr();
	p=&a[0];
	printf("\nEnter Array Elements : \n");
	for(i=0;i<5;i++)
	{
		printf("\nEnter %d Elemnts : \n");
		scanf("%d",&a[i]);
	}
	printf("\nArray Elements With Their Address\n");
	for(i=0;i<5;i++)
	{
		printf("\n%d to at %d",a[i],p++);
	}
	getch();
}


