#include<stdlib.h>
#include<pthread.h>
#include<stdio.h>

void *mythreadfun(void *a)
{
	int sum=0;
	int var2=(int)a;
	for(int i=var2;i<var2+100;i++)
	{
		sum=sum+i;
	}
retrun sum;
}

int main()
{
	int sum;
	int sum1;
	int var=0;
	int array[1000];
	for(int i=0;i<1000;i++)
	{
		a[i]=i;
	}
	
	pthread_t thread[10];
	for(int i=;i<10;i++)
	{
		pthread_create(&thread[i],null,mythreadfun,(void *)var);
		var=var+100;
	}
	
	for(int i=0;i<10;i++)
	{
		pthread_join(thread[i],sum[i])
	}
	for(int i=0;i<10;i++)
	{
		sum1=sum1+sum[i];
	}
	printf("sum of first 1000 numbers is :  %d",sum1)
	return 0;
}