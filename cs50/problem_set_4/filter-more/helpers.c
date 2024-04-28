#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sum = image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue;
            int avg = round((float) sum / 3);
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtBlue = avg;
            image[i][j].rgbtGreen = avg;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j].rgbtRed = image[i][width - 1 - j].rgbtRed;
            image[i][j].rgbtBlue = image[i][width - 1 - j].rgbtBlue;
            image[i][j].rgbtGreen = image[i][width - 1 - j].rgbtGreen;
            image[i][width - 1 - j] = temp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int a = 0; a < height; a++)
    {
        for (int b = 0; b < width; b++)
        {
            copy[a][b] = image[a][b];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int avg_red = 0;
            int avg_green = 0;
            int avg_blue = 0;
            int count = 0;
            int k, l;

            for (k = -1; k <= 1; k++)
            {
                for (l = -1; l <= 1; l++)
                {
                    if ((i + k >= 0 && i + k < height) && (j + l >= 0 && j + l < width))
                    {
                        avg_red += copy[i + k][j + l].rgbtRed;
                        avg_blue += copy[i + k][j + l].rgbtBlue;
                        avg_green += copy[i + k][j + l].rgbtGreen;
                        count++;
                    }
                }
            }
            image[i][j].rgbtRed = round((float) avg_red / count);
            image[i][j].rgbtBlue = round((float) avg_blue / count);
            image[i][j].rgbtGreen = round((float) avg_green / count);
        }
    }
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int a = 0; a < height; a++)
    {
        for (int b = 0; b < width; b++)
        {
            copy[a][b] = image[a][b];
        }
    }

    int gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red_x = 0;
            int green_x = 0;
            int blue_x = 0;
            int red_y = 0;
            int green_y = 0;
            int blue_y = 0;

            for (int k = -1; k <= 1; k++)
            {
                for (int l = -1; l <= 1; l++)
                {
                    if ((i + k >= 0 && i + k < height) && (j + l >= 0 && j + l < width))
                    {
                        red_x += copy[i + k][j + l].rgbtRed * gx[k + 1][l + 1];
                        green_x += copy[i + k][j + l].rgbtGreen * gx[k + 1][l + 1];
                        blue_x += copy[i + k][j + l].rgbtBlue * gx[k + 1][l + 1];

                        red_y += copy[i + k][j + l].rgbtRed * gy[k + 1][l + 1];
                        green_y += copy[i + k][j + l].rgbtGreen * gy[k + 1][l + 1];
                        blue_y += copy[i + k][j + l].rgbtBlue * gy[k + 1][l + 1];
                    }
                }
            }

            // calculate// round(sqrt)
            int final_red = round(sqrt((red_x * red_x) + (red_y * red_y)));
            int final_blue = round(sqrt((blue_x * blue_x) + (blue_y * blue_y)));
            int final_green = round(sqrt((green_x * green_x) + (green_y * green_y)));

            // Cap the values at 255
            if (final_red > 255)
            {
                final_red = 255;
            }
            if (final_green > 255)
            {
                final_green = 255;
            }
            if (final_blue > 255)
            {
                final_blue = 255;
            }

            // Update the original image with the final values
            image[i][j].rgbtRed = final_red;
            image[i][j].rgbtGreen = final_green;
            image[i][j].rgbtBlue = final_blue;
        }
    }
}
