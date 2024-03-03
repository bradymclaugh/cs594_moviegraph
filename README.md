# CS594 - MovieGraph
 
This project tracks the relative "greatness" of actors and actresses over time. Using data acquired through IMDB's API, the rating of every movie an actor or actress played in over their career is shown. In this program, up to five people may be selected. If the actor or actress performed in multiple roles in a single year, the average score of the movies that year are shown. Choosing the actors and actresses in the database came from the website Ranker (https://www.ranker.com/crowdranked-list/best-actors & https://www.ranker.com/crowdranked-list/the-best-actresses-in-film-history). The top 10 actors and actresses were selected. 

The project was done soley on UTK's Hydra servers and assumptions about what is previously installed are reliant on this project being run on Hydra. 


## Usage
After cloning and navigating to the repository:
```
cd jgraph/jgraph
```
Activate Python virtual environment for Pandas library:
```
source movie_venv/bin/activate
```
Run the showcase Python program:
```
python3 moviegraph_showcase.py
```
Pick your own names with (Important note - names must be in quotations):
```
python3 moviegraph.py {Name 1} ... {Name 5}
```
Example:
```
python3 moviegraph.py "Robin Williams" "Kathy Bates"
```
For information on which actors and actresses are in the database:
```
python3 moviegraph.py help
```
The output of the standard program is `moviegraph.jpg`. The output of the showcase program is in the `showcase/` folder.

## Examples
### 1 - Robin Williams vs Kathy Bates
### 2 - Al Pacino vs Robert De Niro
### 3 - Top 5 actors
### 4 - Top 5 actresses
### 5 - Help page?