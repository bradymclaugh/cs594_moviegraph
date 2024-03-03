# CS 594 - MovieGraph
# Brady McLaughlin
# March 3rd, 2024


import sys
import os
import pandas

names = []
actors = ["Anthony Hopkins", "Al Pacino", "Daniel Day-Lewis", "Morgan Freeman", "Robert De Niro", "Denzel Washington", "Jack Nicholson", "Leonardo DiCaprio", "Gary Oldman", "Robin Williams"]
actresses = ["Katharine Hepburn", "Meryl Streep", "Audrey Hepburn", "Maggie Smith", "Ingrid Bergman", "Julie Andrews", "Helen Mirren", "Judi Dench", "Helena Bonham Carter", "Kathy Bates"]
help_bool = False

for arg in sys.argv: 
    names.append(arg)

names.pop(0)

if len(sys.argv) < 2:
    print("Usage: python3 moviegraph.py {Name 1} ... {Name 5}.")
    print("Please select up to 5 names.")
    print("For database information: python3 moviegraph.py help")
    exit(0)

if names[0] == "help":
    help_bool = True
    # print("Actors in database:\n")
    # for name in actors:
    #     print(name)
    # print("\nActresses in database:\n")
    # for name in actresses:
    #     print(name)

if not help_bool:
    for name in names:
        if name not in actors and name not in actresses:
            print(name + " not found in database")
            print("For database information: python3 moviegraph.py help")
            exit(0)

#print(names)

# Jgraph strat:
# Import CSV, downselect to actors
# Add points based on downselected data
# Magic 
# Get output .eps file and convert to pdf 

df = pandas.read_csv('movie_db.csv')

file = open("moviegraph.jgr", "w")

lines = []
lines.append("newgraph\n")

linetypes = ["linetype solid", "linetype dotted", "linetype dashed", "linetype dotdash", "linetype dotdotdash"]
colors = ["color 1 0 0", "color 0 .8 0", "color 0 0 1", "color .8 .4 1", "color .25 0 .25"]
title_string = "title : "

if not help_bool:
    for i, name in enumerate(names):
        df_downselect = df[df['name'] == name]
        df_downselect = df_downselect.sort_values(by='date', ascending=True)
        df_downselect = df_downselect.groupby('date', as_index=False).mean()
        out = "newcurve pts "
        for entry in df_downselect.index:
            out += str(df_downselect['date'][entry]) + " " + str(df_downselect['score'][entry]) + " "
            #print(entry)
        out += linetypes[i] + " "
        out += colors[i] + " "
        out += "label : " + name + '\n'

        title_string += name + " "
        if i != len(names) - 1:
            title_string += "vs. "

        # if len(names) == 1:
        #     title_string = name + " Movie Rankings over Time"

        #print(out) 
        lines.append(out)

    title_string += "Movie Rankings over Time"
    

    #lines.append("newcurve pts 2 3 4 5 1 6 linetype solid\n")
    #lines.append("newcurve pts 5 5 1 7 2 8 linetype dotted\n")
    lines.append("yaxis min 3.0\n")
    lines.append("yaxis max 10\n")
    lines.append("xaxis size 11\n")
    lines.append("yaxis size 4.5\n")
    min_year = df_downselect['date'].min() - 1
    max_year = df_downselect['date'].max() + 1

    lines.append("xaxis min {} max {}".format(min_year, max_year))
    lines.append("xaxis label : Time\n")

    lines.append("xaxis label fontsize 14\n")
    lines.append("yaxis label fontsize 16\n")
    lines.append("yaxis label : Movie Rating (source: IMDB)\n")
    lines.append("xaxis draw_hash_marks mhash 20\n")

    lines.append(title_string + '\n')

    
    lines.append("border\n")
    lines.append("title y 10.5 fontsize 16\n")
    
    lines.append("newgraph inherit_axes\n")
    lines.append("xaxis min 0 max 1000 nodraw\n")
    lines.append("yaxis min 0 max 1000 nodraw\n")
    #lines.append("newcurve eps pics/robin_williams.eps marksize 0 0 pts 200 150 2025 5.5")

    #lines.append("include pics/robin_williams.eps\n")
    #lines.append("newcurve marktype eps")
    #lines.append("newcurve eps pics/robin_williams.eps pts 2020 5.5")
    #lines.append("export JGRAPH_BORDER=5\n")


    for line in lines:
        file.write(line)

    file.close()

    os.system("./jgraph < moviegraph.jgr > moviegraph.eps")
    #os.system("ps2pdf moviegraph.eps moviegraph.pdf")
    os.system("convert -density 300 moviegraph.eps moviegraph.jpg")

else:
    #actors = ["Anthony Hopkins", "Al Pacino", "Daniel Day-Lewis", "Morgan Freeman", "Robert De Niro", "Denzel Washington", "Jack Nicholson", "Leonardo DiCaprio", "Gary Oldman", "Robin Williams"]
    #actresses = ["Katharine Hepburn", "Meryl Streep", "Audrey Hepburn", "Maggie Smith", "Ingrid Bergman", "Julie Andrews", "Helen Mirren", "Judi Dench", "Helena Bonham Carter", "Kathy Bates"]
    lines.append("xaxis min 0 max 1000 nodraw\n")
    lines.append("yaxis min 0 max 1000 nodraw\n")
    lines.append("newcurve eps pics/robin_williams.eps marksize 350 350 label : Robin Williams\n label x 550 y 450\n")
    lines.append("newcurve eps pics/al_pacino.eps marksize 350 350 label : Al Pacino\n label x 550 y 350\n")
    lines.append("newcurve eps pics/daniel_day_lewis.eps marksize 350 350 label : Al Pacino\n label x 550 y 550\n")
    lines.append("title : Actors in Database\n")
    lines.append("title x 800 y 2050 fontsize 24\n")
    for line in lines:
        file.write(line)

    file.close()

    os.system("./jgraph < moviegraph.jgr > moviegraph.eps")
    #os.system("ps2pdf moviegraph.eps moviegraph.pdf")
    os.system("convert -density 300 moviegraph.eps moviegraph.jpg")