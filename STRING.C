#include<stdio.h>
#include<conio.h>
#include<string.h>

void main()
{
	char s1[50];
	int l1,i,count=0;
	clrscr();
	printf("\nEnter String 1 : ");
//	scanf("%s",&s1);
	gets(s1);
//	l1=strlen(s1);

	for(i=0;s1[i]!='\0';i++)
	{
		count++;

	}
	printf("Length Of String 1 is %d",count);
	getch();
}