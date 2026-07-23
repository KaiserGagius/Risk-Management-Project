# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:47:22 2026

@author: GJLL
"""
#library initialization
import networkx as nx
from matplotlib import pyplot as plt

#own function initialization
from main_functions.add_to_graph import add_triplet
from main_functions.calculations import node_total_p

#DG = nx.DiGraph()          # Directed graph object initialization

#add_triplet(DG,('Event1','Consequence1',{'p':0.01}))

events = {
    'no_event':{'severity':'none'},
    'floor_wet': {'severity': 'low'},
    'user_fall_down': {'severity': 'high'},
    'machine_fall_down': {'severity': 'medium'},
    'machine_damage': {'severity': 'high'},
    'package_lost': {'severity': 'high'},
    'user_injury': {'severity': 'maximum'},
    'package_damaged': {'severity': 'maximum'},
    'machine_stuck': {'severity': 'medium'}
}

probabilities = [
    ('no_event', 'floor_wet', {'p':0.05}),
    ('no_event', 'machine_stuck', {'p':0.04}),
    ('floor_wet', 'user_fall_down', {'p': 0.11}),
    ('floor_wet', 'machine_fall_down', {'p': 0.12}),
    ('user_fall_down', 'package_lost', {'p': 0.13}),
    ('user_fall_down', 'machine_fall_down', {'p': 0.14}),
    ('user_fall_down', 'user_injury', {'p': 0.15}),
    ('machine_fall_down', 'package_lost', {'p': 0.17}),
    ('machine_fall_down', 'user_injury', {'p': 0.18}),
    ('machine_fall_down', 'machine_damage', {'p': 0.19}),
    ('machine_stuck', 'machine_damage', {'p': 0.09}),
    ('machine_damage', 'package_lost', {'p': 0.08}),
    ('package_lost', 'package_damaged', {'p': 0.2})
]

DG = nx.DiGraph()
for event_consequence, metadata in events.items():
    DG.add_node(event_consequence, **metadata)
DG.add_edges_from(probabilities)

#VISUALIZATION
pos = nx.spring_layout(DG, seed=42)
plt.figure(figsize=(10, 8))
nx.draw(
    DG, pos, with_labels=True, node_color='lightblue',
    node_size=1000, font_size=10, edge_color='gray'
)

waka=list(nx.all_simple_paths(DG, source='no_event', target='package_damaged'))
#%%Calculate Total Probability
interest_node='package_damaged'
total_p=node_total_p(DG,interest_node)
print(f"The total probability of consequence {interest_node} is: {100*total_p}%")

#%%Neo4J stuff WIP
from neo4j import GraphDatabase

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "<database-uri>"
AUTH = ("<username>", "<password>")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()