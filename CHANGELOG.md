CHANGE LOG
#
Version 1
4/17/2024

Created:

   README-Overview: file stating the purpose, overview and
                          instructions of use

   CHANGE_LOG: created to keep track of versions, updates and
                 addirions to the code 

#
Version 2
4/19/2024

Created:

   inpButton: GUI used for the input button of the audio file
                -getFile()
                -combGraphs()
                -showStats()

Updated:

   CHANGE_LOG: added updates and creations from session 2

#
Version 3
4/20/2024

Created:

   graph.py: these are the tools that are needed to create/display
   wavtools.py: these are the checks made to identify the parts of
                 the wav sound file needed for the graphs and the make
                 graph function

Updated:

   inpButton: This file became the place to combine the pther two files

   inpButton ----> Run_Program_Here
                        file name changed. originally it was named impButton
                        because I intended to just use to for the gui display
                        but then it turned into the main combination of files
                        so the name change seemed appropriate.

Problem Encountered:

   Run_Program_Here: The error comes from there being an issue with connecting
                the wavtools and graph files to the inpButton. I found
                that if i do not import each function from the files
                individually, I get an error that I do not know how to
                fix.

#
Version 4
4/22/24

Updated:

   graph.py: went back through and made my graph colors pink and purple
              instead of the blues i chose originally

Idea:

   I am trying to find a way to make my graphs display in a tab on the
    page next to the file input button, combine graphs, and display button

#
Version 5
4/24/24

Updated:

  graphs.py: added the frequency diagram display and volume display
  Run_Program_Here.py: adds the frequency and volume diagrams and display graohs button
  Installed gitlog?? I thought I had it activated already for this project...

#
Version 6
4/26/24

Updated:

   Volume display graph was giving me issues, so i changed it to a phase plot
   Changed buttons in GUI to pink and created a multipage GUI
   Made GUI navigate to a page displaying the file details after the select file button
    is pressed

   I was not able to figure out how to get my graphs to display in my GUI, I tried
    using the create a canvas but the plot was then just not showing up at all.