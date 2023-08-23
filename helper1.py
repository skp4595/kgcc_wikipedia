import pandas as pd
import requests
from bs4 import BeautifulSoup
import pylab
from numpy import shape
from graphviz import Digraph
from queue import Queue



def leastDistance(graph, source, dest):
    Q = Queue()
    # create a dictionary with large distance(infinity) of each vertex from source
    v = len(graph)
    distance = {k: 9999999 for k in range(v)}
    visited_vertices = set()
    Q.put(source)
    visited_vertices.update({0})
    while not Q.empty():
        vertex = Q.get()
        if vertex == source:
            distance[vertex] = 0
        for u in graph[vertex]:
            if u not in visited_vertices:
                # update the distance
                if distance[u] > distance[vertex] + 1:
                    distance[u] = distance[vertex] + 1
                Q.put(u)
                visited_vertices.update({u})
    return distance[dest]

def Create_graph(compound_name):
    compound_name = compound_name.split()
    print("starting importing data")
    count = 0
    n = len(compound_name)

    for i in range(n):
        compound_name[i] = compound_name[i].lower()
        #print(word)
    compound_name[0] = compound_name[0].capitalize()
    print(compound_name)

    name = "_".join(compound_name)
    print(name)

    wikiurl= f"https://en.wikipedia.org/wiki/{name}"
    table_class="wikitable sortable jquery-tablesorter"
    response=requests.get(wikiurl)
    print(response.status_code) # status code 200 means it is legal to do web scrapping on the site

    # parse data from the html into a beautifulsoup object
    soup = BeautifulSoup(response.text, 'html.parser')
    indiatable=soup.find('table',{'class':"infobox ib-chembox"})

    df=pd.read_html(str(indiatable))
    # convert list to dataframe
    df=pd.DataFrame(df[0])
    n = len(df[0])

    labels = {}
    j = 0

    for i in range(n):
        if df[0][i] == df[1][i]:
            li = df[0][i].split()
            if len(df[0][i]) >= 50:
                print(li)
                continue
            labels[df[0][i]] = {}
            j = i
        else:
            try:
                labels[df[0][j]][df[0][i]] = df[1][i]
            except:
                pass
    gra = Digraph("round-table")
    gra.body.append('\t"layout" = "sfdp"\n')
    gra.body.append('\t"overlap" = "false"\n')
    gra.body.append('\t"beautify" = True\n')
    gra.body.append('\t"bgcolor" = "black"\n')


    gra.node('0', name, shape = "oval", color="red", fontcolor="red")

    index = 1
    ind = 100
    ind2 = 200

    count1 = 0

    for i in labels.keys():
        count2 = 0
        rv = "&"

        temp = str(index)
        ntemp = str(i)   
        if(i == ''):
            continue
        gra.node(temp, ntemp, fontcolor="gold", color = "gold")
        for j in labels[i].keys():
            temp1 = str(ind)
            temp2 = str(j)
            edge = j
            node = str(labels[i][j])
            gra.node(temp1, node, fontcolor="cyan", color = "cyan")
            gra.edge(temp, temp1, label= edge, color="gold", fontcolor="gold")
            ind = ind+1
        gra.edge('0', temp, color="red")
        index = index + 1
        filename = gra.render(filename=f'image/{name}')



if __name__ == "__main__":
    print("Does not mean to be executed Directly")
    pass
