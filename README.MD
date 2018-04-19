# Vimeo Backend Exercise

This is the Vimeo Backend Exercise. It is a simple tool that sorts through two CSV's that detail data about video's accessible through the Vimeo site. Details include: Video titles, likes, purchases, value of purchases, and currency exchange rates. This tool was built using Python 3.

##Instructions

Place the sort.py file in the folder of your choosing. You will need to edit the file paths located at the top of the sort.py file on lines 6, 8, 10, and 12 in order to run this tool. 

video_path 
    Should be the location of the video csv on your local machine.

rate_path
    Should be the location of the exchange rate csv on your local machine.

valid_path  
    Should be the location of where you want the valid csv to be saved on your local machine.

invalid_path  
    Should be the location of where you want the valid csv to be saved on your local machine.

Once you have set your file paths, open terminal and navigate to folder where sort.py is located. 

Type: python sort.py

This should run the tool and output a valid.csv and an invalid.csv based on the defined parameters. The total value of valid.csv will print into the terminal window. 

##Project Questions

###Was the question/problem clear? Did you feel like something was missing or not explained correctly?
The only thing that was unclear to me was the video price being an "or" question. I went with the CAD exchange rate simply because it produced the smaller list. 

###What makes your solution awesome?
I like my solution because it feels very simple and easy to understand.

###Did you have to make any trade-offs in your design? If so, what?
The design is pretty straight forward for this project. There is some redundant code that I feel that could be cleaned up and I would like to make an interface for CSV filepaths that wasn't editing global variables in the code. 

###Is there anything else you want to share about your solution or the problem?
It's simple, but I think it gives an honest showcase of what I'm currently capable of. I'm new to coding, but learning every day. 