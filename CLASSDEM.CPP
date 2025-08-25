#include<iostream.h>
#include<conio.h>

class Student
{
	int rno;
	char *sname;
	clrscr();
	public:
	void getData()
	{
		cout<<"\nEnter Roll No : ";
		cin>>rno;
		cout<<"\nEnter Student Name : ";
		cin>>sname;
	}
	void putData();
};
void Student :: putData()
{
	cout<<"\Roll No : "<<rno;
	cout<<"\nStudent Name : "<<sname;
}
void main()
{
	Student s1;
	clrscr();
	s1.getData();
	s1.putData();
	getch();
}

