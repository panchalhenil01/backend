#include<stdio.h>
#include<conio.h>
#include<string.h>

void main()
{
	int choice, quantity, total = 0, amount;
	char moreOrders;
	clrscr();
	do
	{
		print("\n--------- Food Menu ---------\n");
		printf("1.Pizza Price = 180rs/pcs\n");
		printf("2.Burger Price = 140rs/pcs\n");
		printf("3.Dosa Price = 120rs/pcs\n");
		printf("4.Idli Price = 100rs/pcs\n");

		printf("\nPlease Enter your choice (1-4): ");
		scanf("%d", &choice);

		switch (choice)
		{
		case 1:
			printf("You selected Pizza\n");
			printf("Enter the quantity: ");
			scanf("%d", &quantity);
			amount = 180 * quantity;
			printf("Amount = %d\n", amount);
			total += amount;
			break;
		case 2:
			printf("You selected Burger\n");
			printf("Enter the quantity: ");
			scanf("%d", &quantity);
			amount = 140 * quantity;
			printf("Amount = %d\n", amount);
			total += amount;
			break;
		case 3:
			printf("You selected Dosa\n");
			printf("Enter the quantity: ");
			scanf("%d", &quantity);
			amount = 120 * quantity;
			printf("Amount = %d\n", amount);
			total += amount;
			break;
		case 4:
			printf("You selected Idli\n");
			printf("Enter the quantity: ");
			scanf("%d", &quantity);
			amount = 100 * quantity;
			printf("Amount = %d\n", amount);
			total += amount;
			break;

		default:
			printf("Invalid choice! Please select between 1-4.\n");
		}

		printf("Total so far = %d\n");

		printf("\nDo you want to order more? (y/n): ");
		scanf("%c", &moreOrders);

	} while (moreOrders == 'y' || moreOrders == 'Y');

	printf("\n========= Final Bill =========\n");
	printf("\nTotal Amount to be paid = %d rs\n", total);
	printf("================================\n");

	getch();
}









