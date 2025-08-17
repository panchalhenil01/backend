#include<stdio.h>
#include<conio.h>


void main()
{
	char str[100];
	int i,vowels=0,consonants=0;
	printf("\nEnter a string : \n");
	gets(str);
	for(i=0;str[i]!='\0';i++)
	{
		char c= tolower(str[i]);
		{
			if(c>'a' && c<'z')
			{
				if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
				{
					vowels++;
					consonants++;
				}
			}
		}
	}
	printf("\nvowels : %d\n",vowels);
	printf("\nconsonants : %d",consonants);
	getch();
}


