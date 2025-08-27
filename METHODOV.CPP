#include<iostream.h>
#include<conio.h>

class A
{
	public:
	void test()
	{
		cout<<"\nTest with no arguement";
	}
	void test(int a)
	{
		cout<<"\nTest with 1 arguement";
	}
	void test(int a,int b)
	{
		cout<<"\nTest with 2 arguement";
	}
};
void main()
{
	clrscr();
	A a1;
	a1.test(10);
	a1.test(10,20);
	a1.test();
	getch();
}

