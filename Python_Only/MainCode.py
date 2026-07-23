# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 08:41:13 2026

@author: GJLL
"""

#library initialization
import networkx as nx
from matplotlib import pyplot as plt

#own function initialization
from main_functions.add_to_graph import add_triplet
from main_functions.add_to_graph import add_triplets
from main_functions.calculations import node_total_p

#%% Multiple triplets at once
events = {#This is only necessary if we wish to add meta-information to each event
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

triplets = [#unlike a formal risk triplet here the probability goes last
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

#%% ADD Demo
knowledge_graph = nx.DiGraph()#Initialize new directional graph

knowledge_graph=add_triplet(knowledge_graph,('no_event', 'gas_leak', {'p':0.01})) #single add
knowledge_graph=add_triplets(knowledge_graph,triplets) #multiple add

#Add attribute severity. Same format can be used for other attributes. Follow Schema:
for event_consequence, metadata in events.items():
    knowledge_graph.add_node(event_consequence, **metadata)

#%%Calculate Total Probability
interest_node='package_damaged'
total_p=node_total_p(knowledge_graph,interest_node)
print(f"The total probability of consequence {interest_node} is: {100*total_p}%")

#%%Visualization
pos = nx.spring_layout(knowledge_graph, seed=42)
plt.figure(figsize=(10, 8))
nx.draw(
    knowledge_graph, pos, with_labels=True, node_color='lightblue',
    node_size=1000, font_size=10, edge_color='gray'
)