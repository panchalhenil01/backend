#include<iostream.h>
#include<conio.h>

void main()
{
	int a[5],i,j,temp;
	clrscr();
	for(i=0;i<5;i++)
	{
		cout<<"\nEnter Value A[%d]:",i;
		cin>>a[i];
	}
	for(i=0;i<5;i++)
	{
		for(j=i+1;j<5;j++)
		{
			if(a[i]<a[j]);
			{
				temp=a[i];
				a[i]=a[j];
				a[j]=temp;
		       }
		}
	}
	cout<<"\nArray Element In Assending order : \n";
	cin>>a[i],a[j];
	getch();
}