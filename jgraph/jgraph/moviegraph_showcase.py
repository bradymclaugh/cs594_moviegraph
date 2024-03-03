# CS 594 - MovieGraph
# Brady McLaughlin
# March 3rd, 2024


import sys
import os
import pandas

names = []
actors = ["Anthony Hopkins", "Al Pacino", "Daniel Day-Lewis", "Morgan Freeman", "Robert De Niro", "Denzel Washington", "Jack Nicholson", "Leonardo DiCaprio", "Gary Oldman", "Robin Williams"]
actresses = ["Katharine Hepburn", "Meryl Streep", "Audrey Hepburn", "Maggie Smith", "Ingrid Bergman", "Julie Andrews", "Helen Mirren", "Judi Dench", "Helena Bonham Carter", "Kathy Bates"]

# for arg in sys.argv: 
#     names.append(arg)

# names.pop(0)

# if len(sys.argv) < 2:
#     print("Usage: python3 moviegraph.py {Name 1} ... {Name 5}.")
#     print("Please select up to 5 names.")
#     print("For database information: python3 moviegraph.py help")
#     exit(0)

# if names[0] == "help":
#     print("Actors in database:\n")
#     for name in actors:
#         print(name)
#     print("\nActresses in database:\n")
#     for name in actresses:
#         print(name)
#     exit(0)

# for name in names:
#     if name not in actors and name not in actresses:
#         print(name + " not found in database")
#         print("For database information: python3 moviegraph.py help")
#         exit(0)

# print(names)

# Jgraph strat:
# Import CSV, downselect to actors
# Add points based on downselected data
# Magic 
# Get output .eps file and convert to pdf 
        
# 1 - Robin Williams vs Kathy Bates
# 2 - Al Pacino vs Robert De Niro
# 3 - Top 5 actors
# 4 - Top 5 actresses
# 5 - Help page?

file_names = ["showcase/1_william_vs_bates.jpg", "showcase/2_pacino_vs_de_niro.jpg", "showcase/3_top_5_actors.jpg", "showcase/4_top_5_actresses.jpg"]
df = pandas.read_csv('movie_db.csv')

for x, fn in enumerate(file_names):
    
    if x == 0:
        names = ["Robin Williams", "Kathy Bates"]
    if x == 1:
        names = ["Al Pacino", "Robert De Niro"]
    if x == 2:
        names = ["Anthony Hopkins", "Al Pacino", "Daniel Day-Lewis", "Morgan Freeman", "Robert De Niro"]
    if x == 3:
        names = ["Katharine Hepburn", "Meryl Streep", "Audrey Hepburn", "Maggie Smith", "Ingrid Bergman"]

    file = open("moviegraph.jgr", "w")

    lines = []
    lines.append("newgraph\n")

    linetypes = ["linetype solid", "linetype dotted", "linetype dashed", "linetype dotdash", "linetype dotdotdash"]
    colors = ["color 1 0 0", "color 0 .8 0", "color 0 0 1", "color .8 .4 1", "color .25 0 .25"]
    title_string = "title : "


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
    lines.append("xaxis label : Time\n")
    lines.append("xaxis label fontsize 14\n")
    lines.append("yaxis label fontsize 16\n")
    lines.append("yaxis label : Movie Rating (source: IMDB)\n")
    lines.append("xaxis draw_hash_marks mhash 20\n")

    lines.append(title_string + '\n')

    #lines.append("title : This is an example graph\n")
    lines.append("border\n")
    lines.append("title y 10.5 fontsize 16\n")


    #lines.append("include pics/robin_williams.eps\n")
    #lines.append("newcurve marktype eps")
    #lines.append("newcurve eps pics/robin_williams.eps pts 2020 5.5")
    #lines.append("export JGRAPH_BORDER=5\n")
    #lines.append("image { image ""pics/robin_williams.jpg"" pos 1 1 width 2 height 2}")


    for line in lines:
        file.write(line)

    file.close()

    os.system("./jgraph < moviegraph.jgr > moviegraph.eps")
    #os.system("ps2pdf moviegraph.eps moviegraph.pdf")
    out_string = "convert -density 300 moviegraph.eps {}".format(fn)
    os.system(out_string)

