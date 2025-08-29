#include<iostream.h>
#include<conio.h>

class XYZ;
class ABC;
{
	int a;
	public:
		void setA()
		{
			cout<<"\nEnter A : ";
			cin>>a;
		}
		friend void max(ABC a,XYZ a);
};
class XYZ
{
	int x;
	public:
		void setX()
		{
			cout<<"\nEnter X : ";
			cin>>x;
		}
		friend void max(ABC a,XYZ a);
};
void max(ABC A,XYZ X)
{
	if(A.a>X.x)
	{
		cout<<"\nA Is Max";
	}
	else
	{


