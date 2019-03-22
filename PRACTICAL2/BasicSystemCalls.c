#include <stdio.h>
#include <fcntl.h> 

int main()
{
	int file = creat("createdFile.txt" , O_RDWR|O_CREAT);
	int opener = open("file.txt", O_RDONLY);
	char data[100],writeData[100] = "this is being written\n";

	int sizeRead = read(opener,data,30);
	data[sizeRead] = '\0';
	
	write(file,writeData,30);

	int i = 0;
	while(data[i] != '\0')
	{
		printf("%c",data[i]);
		i = i + 1;
	}
	
	close(file);
	close(opener);

	return 0;
}
