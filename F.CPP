#include<iostream.h>
#include<conio.h>

class a
{
	int n;
	public:
	a()
	{
		n=10;
		cout<<"Destroyed object"<<endl;
		cout<<n<<endl;
	}
};
void main()
{
	clrscr();
	a ob,ob1;
	getch();
}
