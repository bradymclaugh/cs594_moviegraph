# CS 594 - MovieGraph Showcase
# Brady McLaughlin
# March 3rd, 2024


import sys
import os
import pandas

names = []
actors = ["Anthony Hopkins", "Al Pacino", "Daniel Day-Lewis", "Morgan Freeman", "Robert De Niro", "Denzel Washington", "Jack Nicholson", "Leonardo DiCaprio", "Gary Oldman", "Robin Williams"]
actresses = ["Katharine Hepburn", "Meryl Streep", "Audrey Hepburn", "Maggie Smith", "Ingrid Bergman", "Julie Andrews", "Helen Mirren", "Judi Dench", "Helena Bonham Carter", "Kathy Bates"]

file_names = ["showcase/1_williams_vs_bates.jpg", "showcase/2_pacino_vs_de_niro.jpg", "showcase/3_top_5_actors.jpg", "showcase/4_top_5_actresses.jpg", "showcase/help"]
df = pandas.read_csv('movie_db.csv')

for x, fn in enumerate(file_names):
    help_bool = False
    if x == 0:
        names = ["Robin Williams", "Kathy Bates"]
        print("Generating graph #1")
    if x == 1:
        names = ["Al Pacino", "Robert De Niro"]
        print("Generating graph #2")
    if x == 2:
        names = ["Anthony Hopkins", "Al Pacino", "Daniel Day-Lewis", "Morgan Freeman", "Robert De Niro"]
        print("Generating graph #3")
    if x == 3:
        names = ["Katharine Hepburn", "Meryl Streep", "Audrey Hepburn", "Maggie Smith", "Ingrid Bergman"]
        print("Geenerating graph #4")
    if x == 4:
        print("Generating Actor Database information")
        print("Generating Actress Database information")
        help_bool = True

    file = open("moviegraph.jgr", "w")

    lines = []
    #lines.append("newgraph\n")

    linetypes = ["linetype solid", "linetype dotted", "linetype dashed", "linetype dotdash", "linetype dotdotdash"]
    colors = ["color 1 0 0", "color 0 .8 0", "color 0 0 1", "color .8 .4 1", "color .25 0 .25"]
    title_string = "title : "


    if not help_bool:
        file = open("moviegraph.jgr", "w")
        lines.append("newgraph\n")
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

            lines.append(out)

        title_string += "Movie Rankings over Time"
        if x == 2:
            title_string = "title : Top 5 Actors over Time\n"
        if x == 3:
            title_string = "title : Top 5 Actresses over Time\n"
        
        lines.append("yaxis min 3.0\n")
        lines.append("yaxis max 10\n")
        lines.append("xaxis size 11\n")
        lines.append("yaxis size 4.5\n")
        min_year = df_downselect['date'].min() - 1
        max_year = df_downselect['date'].max() + 1

        lines.append("xaxis label : Time\n")
        lines.append("xaxis label fontsize 14\n")
        lines.append("yaxis label fontsize 16\n")
        lines.append("yaxis label : Movie Rating (source: IMDB)\n")
        lines.append("xaxis draw_hash_marks mhash 20\n")

        lines.append(title_string + '\n')
        lines.append("border\n")
        lines.append("title y 10.5 fontsize 16\n")

        for line in lines:
            file.write(line)

        file.close()

        os.system("./jgraph < moviegraph.jgr > moviegraph.eps")
        #os.system("ps2pdf moviegraph.eps moviegraph.pdf")
        out_string = "convert -density 300 moviegraph.eps {}".format(fn)
        os.system(out_string)

    else:
        file = open("moviegraph_actors.jgr", "w")
        lines.append("newgraph\n")
    
        lines.append("xaxis min 0 max 1000 size 8.5 nodraw\n")
        lines.append("yaxis min 0 max 1000 size 11 nodraw\n")

        lines.append("newcurve eps pics/robin_williams.eps marksize 200 200 pts 150 150\n")
        lines.append("newstring x 450 y 150 fontsize 24 : Robin Williams\n")

        lines.append("newcurve eps pics/al_pacino.eps marksize 200 200 pts 150 350\n")
        lines.append("newstring x 450 y 350 fontsize 24 : Al Pacino\n")

        lines.append("newcurve eps pics/daniel_day_lewis.eps marksize 200 200 pts 150 550\n")
        lines.append("newstring x 450 y 550 fontsize 24 : Daniel Day Lewis\n")

        lines.append("newcurve eps pics/morgan_freeman.eps marksize 200 200 pts 150 750\n")
        lines.append("newstring x 450 y 750 fontsize 24 : Morgan Freeman\n")

        lines.append("newcurve eps pics/robert_de_niro.eps marksize 200 200 pts 150 950\n")
        lines.append("newstring x 450 y 950 fontsize 24 : Robert De Niro\n")    

        lines.append("newcurve eps pics/anthony_hopkins.eps marksize 200 200 pts 1150 150\n")
        lines.append("newstring x 850 y 150 fontsize 24 : Anthony Hopkins\n")

        lines.append("newcurve eps pics/denzel_washington.eps marksize 200 200 pts 1150 350\n")
        lines.append("newstring x 850 y 350 fontsize 24 : Denzel Washington\n")

        lines.append("newcurve eps pics/jack_nicholson.eps marksize 200 200 pts 1150 550\n")
        lines.append("newstring x 850 y 550 fontsize 24 : Jack Nicholson\n")

        lines.append("newcurve eps pics/leonardo_dicaprio.eps marksize 200 200 pts 1150 750\n")
        lines.append("newstring x 850 y 750 fontsize 24 : Leonardo DiCaprio\n")

        lines.append("newcurve eps pics/gary_oldman.eps marksize 200 200 pts 1150 950\n")
        lines.append("newstring x 850 y 950 fontsize 24 : Gary Oldman\n") 

        lines.append("legend off\n")

        lines.append("title : Actors in Database\n")
        lines.append("title x 650 y 1200 fontsize 64\n")
        for line in lines:
            file.write(line)

        file.close()
        os.system("./jgraph < moviegraph_actors.jgr > moviegraph_actors.eps")
        out_string = "convert -density 300 moviegraph_actors.eps {}".format("showcase/5_actor_database.jpg")
        os.system(out_string)

        lines = []
        file = open("moviegraph_actresses.jgr", "w")
        lines.append("newgraph\n")
       
        lines.append("xaxis min 0 max 1000 size 8.5 nodraw\n")
        lines.append("yaxis min 0 max 1000 size 11 nodraw\n")

        lines.append("newcurve eps pics/katherine_hepburn.eps marksize 200 200 pts 115 150\n")
        lines.append("newstring x 400 y 150 fontsize 24 : Katharine Hepburn\n")

        lines.append("newcurve eps pics/meryl_streep.eps marksize 200 200 pts 115 350\n")
        lines.append("newstring x 400 y 350 fontsize 24 : Meryl Streep\n")

        lines.append("newcurve eps pics/audrey_hepburn.eps marksize 200 200 pts 115 550\n")
        lines.append("newstring x 400 y 550 fontsize 24 : Audrey Hepburn\n")

        lines.append("newcurve eps pics/maggie_smith.eps marksize 200 200 pts 115 750\n")
        lines.append("newstring x 400 y 750 fontsize 24 : Maggie Smith\n")

        lines.append("newcurve eps pics/ingrid_bergman.eps marksize 200 200 pts 115 950\n")
        lines.append("newstring x 400 y 950 fontsize 24 : Ingrid Bergman\n")    

        lines.append("newcurve eps pics/julie_andrews.eps marksize 200 200 pts 1050 150\n")
        lines.append("newstring x 800 y 150 fontsize 24 : Julie Andrews\n")

        lines.append("newcurve eps pics/helen_mirren.eps marksize 200 200 pts 1050 350\n")
        lines.append("newstring x 800 y 350 fontsize 24 : Helen Mirren\n")

        lines.append("newcurve eps pics/judi_dench.eps marksize 200 200 pts 1050 550\n")
        lines.append("newstring x 800 y 550 fontsize 24 : Judi Dench\n")

        lines.append("newcurve eps pics/helena_bonham_carter.eps marksize 200 200 pts 1050 750\n")
        lines.append("newstring x 750 y 750 fontsize 24 : Helena Bonham Carter\n")

        lines.append("newcurve eps pics/kathy_bates.eps marksize 200 200 pts 1050 950\n")
        lines.append("newstring x 800 y 950 fontsize 24 : Kathy Bates\n") 

        lines.append("legend off\n")

        lines.append("title : Actresses in Database\n")
        lines.append("title x 585 y 1200 fontsize 64\n")

        for line in lines:
            file.write(line)

        file.close()

        os.system("./jgraph < moviegraph_actresses.jgr > moviegraph_actresses.eps")
        #os.system("ps2pdf moviegraph.eps moviegraph.pdf")
        out_string = "convert -density 300 moviegraph_actresses.eps {}".format("showcase/6_actress_database.jpg")
        os.system(out_string)

print("Showcase done. Please check the showcase/ folder for results!")