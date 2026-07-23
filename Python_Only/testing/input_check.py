# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 23:39:45 2026

@author: Default
"""

def check_risk_triplet(potential_risk_triplet):
    #check if input is tuple
    if not isinstance(potential_risk_triplet, (tuple)):
        raise TypeError("Input must be a Tuple or a list of tuples")
    #check if not right size
    if len(potential_risk_triplet)!=3:
        raise TypeError("Input must be a Tuple with three elements")

    #unpack the tuple
    potential_event,potential_consequence,potential_probability_dict=potential_risk_triplet
    
    #check if event is str
    if not isinstance(potential_event, (str)):
        raise TypeError("First element of tuple (Event) must be a string")
    
    #check if consequence is str
    if not isinstance(potential_consequence, (str)):
        raise TypeError("Second element of tuple (Consequence) must be a string")
    
    #check if probability is the right type
    if not isinstance(potential_probability_dict, (dict)):
        raise TypeError("Third element of tuple (probability) must be a dictionary with the format {'p':your_probability}")
    #chek that the key is 'p'
    if not 'p' in potential_probability_dict:
        raise TypeError("Risk probability must be named 'p'")
    #check if probability is float
    if not isinstance(potential_probability_dict['p'], (float)):
        raise TypeError("Probability must be a float")
        
    event_consequence=(potential_event,potential_consequence)
    probability_dict=potential_probability_dict
        
    return event_consequence,probability_dict

def check_risk_triplets(input_triplets,input_events):
    #TO-DO: add list checks
    checked_events=input_events
    checked_prbabilities=input_probabilities
    return checked_events,checked_prbabilities