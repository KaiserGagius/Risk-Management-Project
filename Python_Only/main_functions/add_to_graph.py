# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 23:36:02 2026

@author: GJLL
"""
#library initialization
import networkx as nx

#own function initialization
from testing.input_check import check_risk_triplet
from testing.input_check import check_risk_triplets


def add_triplet(knowledge_graph,input_triplet):
    #check input triplet
    event_consequence,probability_dict=check_risk_triplet(input_triplet)
    
    knowledge_graph.add_node(event_consequence)
    knowledge_graph.add_edge(input_triplet) #TO-DO: FIX!!!!!!!!!
    
    return knowledge_graph

def add_triplets(knowledge_graph,input_triplets,input_events=[]):
    #Need to finish the checks for multiple first:
    triplets_checked=input_triplets
    events_checked=input_events
    # if len(input_events)!=0:
    #     triplet_checked,events_checked=check_risk_triplets(input_triplets,input_events)
    # else:
    #     triplet_checked,events_checked=check_risk_triplets(input_triplets,input_events)
    
    if len(input_events)!=0:
        for event_consequence, metadata in events_checked.items():
            knowledge_graph.add_node(event_consequence, **metadata)
    else:
            knowledge_graph.add_edges_from(triplets_checked)
    
    return knowledge_graph