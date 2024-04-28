#include <cs50.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: $ ./recover.c forensic_image_file\n");
        return 1;
    }
    string filename = argv[1];
    FILE *f = fopen(filename, "r");
    uint8_t buffer[512];
    char img_name[8];
    int counter = 0;
    FILE *img = NULL;

    while (fread(buffer, 1, sizeof(buffer), f) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            if (img != NULL)
            {
                fclose(img);
            }
            sprintf(img_name, "%03i.jpg", counter);
            img = fopen(img_name, "w");

            if (img == NULL)
            {
                printf("Could not create new image file\n");
                fclose(f);
                return 1;
            }
            fwrite(buffer, 1, sizeof(buffer), img);
            counter++;
        }
        else if (img != NULL)
        {
            fwrite(buffer, 1, sizeof(buffer), img);
        }
    }
    fclose(img);
    fclose(f);
}
