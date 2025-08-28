#include<iostream.h>
#include<conio.h>

class RBI
{
	public:
	virtual void roi(double r)=0;
};

class SBI:public RBI
{
	public:
	void credit_card;
	{
		cout<<"\nPremium Credit Card By SBI";
	}
	void roi(double p)
	{
		cout<<"\nRate Of Interest Given By SBI In"<<r;
	}
};
class HDFC:public RBI
{
	public:
	void credit_card()
	{
		cout<<"\nPremium Credit Card By HDFC";
	}
	void roi(double r)
	{
		cout<<"\nRate Of Interest Given By SBI In"<<r;
	}
};

void main()
{
	clrscr();
	SBI s;
	s.credit_card();
	s.roi(6.5);

	HDFC h;
	h.credit_card();
	h.roi(7.1);
	getch();
}