#include<iostream.h>
#include<conio.h>

void main()
{
	int arr[]={10,5,20,8,30};
	int i,max=arr[0],min=arr[0];
	clrscr();
	for(i=1;i<5;i++)
	{
		if(arr[i] > max)
		{
			cout<<"\nMax = arr[i]";
			cin>>"max";
		}
		if(arr[i] < min)
		{
			cout<<"\Min = arr[i]";
			cin>>"min";
		}
	}
	cout<<"\nMax : %d \n Min : %d \n",max.min;
	getch();
}