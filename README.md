# Converting-a-C-array-to-a-table-lookup-for-use-in-a-PIC16-HCMS-2913-assembly-program
This is a Python 3 program that specifically converts the C array that I got to a PIC16 lookup table. I have added an additional comma to the last element of the C array to makes things simpler.

I have gotten the C array from here: https://github.com/PaulStoffregen/LedDisplay/blob/master/font5x7.h

It is a font data for use in the HCMS-2913. You can look at the datasheet here: https://www.promelec.ru/pdf/HCMS-29xx.pdf

## Usage
You need Python 3. You can download it here: https://www.python.org/downloads/

You can run the program by(Windows example):
```
python main.py inputFile.txt outputFile.txt
```

It takes 2 arguments. The first argument is where the C array data is from(This file needs to exist). The second argument is where to put the output(This file will be created if it doesn't exist. It will be overwritten if it did exist).

After execution, you can see in the terminal how much memory the lookup table will take from the program memory of a PIC16.
