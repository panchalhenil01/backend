#include<stdio.h>
#include<conio.h>

void main()
{
	int arr[]={10,5,20,8,30};
	int i,max=arr[0],min=arr[0];
	for(i=1;i<5;i++)
	{
		if(arr[i] > max)
		{
			max = arr[i];
		}
		if(arr[i] < min)
		{
			min = arr[i];
		}
	}
	printf("Max : %d \n min: %d \n",max,min);
	getch();
}