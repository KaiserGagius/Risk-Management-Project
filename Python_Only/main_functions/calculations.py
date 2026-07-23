# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 19:59:30 2026

@author: GJLL
"""
import networkx as nx
def node_total_p(knowledge_graph,node):
    
    #check if node is str
    if not isinstance(node, (str)):
        raise TypeError("Node must be a string")
    
    #get all simple paths leading to desired node
    paths=list(nx.all_simple_paths(knowledge_graph, source='no_event', target=node))
    
    #get all probabilities
    all_p=nx.get_edge_attributes(knowledge_graph, 'p',default="ERROR, no p given")
    
    total_p=0
    for path in paths:
        interim_p=1 #probability of a single path, later to be summed to the total
        for i in range(len(path)-1):# path of length n has n-1 edges
            interim_p=all_p[(path[i],path[i+1])]*interim_p
        total_p=total_p+interim_p
    
    return total_p