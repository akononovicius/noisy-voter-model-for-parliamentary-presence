#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def validateParams(sOn, sOff, herd, nAgents, echo=False):
    """
    Function checks whether parameter set is valid. This is done by checking
    the maximum probability, defiend as max(s) + h*N. If maximum probability
    is equal to or greater than 1, then Error is raised. If maximum probability
    is equal to or greater than 0.5, then Warning is raised.
    
    Parameters
    ----------
    sOn : float
        sigma parameter for agents switching from "off" state to "on" state
    sOff : float
        sigma parameter for agents switching from "on" state to "off" state
    herd : float
        h parameter for interaction between agents
    nAgents : int or float
        number of agents within the model
        
    Returns
    -------
    int
        1 - everything is fine,
        0 - warning
        -1 - error
    """
    maxSigma=np.max(np.array([sOn,sOff]))
    maxProb=switchProb(maxSigma,herd,nAgents)
    if maxProb>=1:
        if echo:
            print(sOn,sOff,herd,nAgents,sep=",")
            print("ERROR! Maximum probability larger than 1: {:.2f}".format(maxProb))
        return -1
    if maxProb>=0.5:
        if echo:
            print(sOn,sOff,herd,nAgents,sep=",")
            print("WARNING! Maximum probability larger than 0.5: {:.2f}".format(maxProb))
        return 0
    if echo:
        minSigma=np.min(np.array([sOn,sOff]))
        minProb=switchProb(minSigma,herd,0)
        print(sOn,sOff,herd,nAgents,sep=",")
        print("GOOD! Probability is within [{:.2f}; {:.2f}]".format(minProb,maxProb))
    return 1

def switchProb(sigma,herd,nOthers):
    return sigma+herd*nOthers

def step(sOn, sOff, herd, state):
    """
    Function performs a single step according to herding model rules. Namely
    switching probability to state ``i`` is assumed to be given by:
        prob[i] = sigma[i] + h*N[i] ,
    wher N[i] is the number of agents in  ``i`` state.
    
    Parameters
    ----------
    sOn : float
        sigma parameter for agents switching from "off" state to "on" state
    sOff : float
        sigma parameter for agents switching from "on" state to "off" state
    herd : float
        h parameter for interaction between agents
    state : array_like
        array containing states of all agents ("on" state is assumed to be
        encoded by 1, while "off" state is assumed to be encoded by -1)
        
    Returns
    -------
    array_like
        updated state array
    """
    # define internal state variable
    _istate=state.copy()
    
    # estimate current state properties
    nTotal=len(_istate) # total number of agents
    nOn=np.sum(_istate==1) # agents in on state
    
    # calculate flipping probabilities
    prob=np.zeros(nTotal)
    prob[_istate==1]=switchProb(sOff,herd,nTotal-nOn)
    prob[_istate==-1]=switchProb(sOn,herd,nOn)
    
    # do the flip
    r=np.random.rand(nTotal)
    _istate[r<prob]=-_istate[r<prob]
    
    return _istate

def rawSeries(nPoints, sOn, sOff, herd, state, warmup=0):
    """
    Function performs multiple steps according to herding model rules (see
    the documentation of step function).
    
    Parameters
    ----------
    nPoints : int
        number of points to perform
    sOn : float
        sigma parameter for agents switching from "off" state to "on" state
    sOff : float
        sigma parameter for agents switching from "on" state to "off" state
    herd : float
        h parameter for interaction between agents
    state : array_like
        array containing states of all agents ("on" state is assumed to be
        encoded by 1, while "off" state is assumed to be encoded by -1)
    warmup : int, optional
        number of warmup steps to perform (so that the model could have a
        chance to "forget" the initial state). Zero by default.
        
    Returns
    -------
    array_like
        array of state observations
        
    See also
    --------
    step
    """
    # define internal state variable
    _istate=state.copy()
    
    # define output variable
    output=np.zeros((nPoints, len(state)))
    
    # the warmup loop
    if warmup>0:
        for i in np.arange(0, warmup):
            _istate=step(sOn, sOff, herd, _istate)
    
    # the main loop
    for i in np.arange(0, nPoints):
        _istate=step(sOn, sOff, herd, _istate)
        output[i]=_istate.copy()
        
    return output

def noisySeries(nPoints, pOn, pOff, sOn, sOff, herd, state, warmup=0):
    """
    Function performs multiple steps according to herding model rules (see
    the documentation of step function) and adds external noise. Namely, "on"
    and "off" states now would mean that the states are noisy. Agent in "on"
    state is on with probability given by pOn and agent in "off" state is on
    with probability given by pOff.
    
    Parameters
    ----------
    nPoints : int
        number of points to perform
    pOn : float
        probability that agent in the "on" state will be "on"
    pOff : float
        probability that agent in the "off" state will be "on"
    sOn : float
        sigma parameter for agents switching from "off" state to "on" state
    sOff : float
        sigma parameter for agents switching from "on" state to "off" state
    herd : float
        h parameter for interaction between agents
    state : array_like
        array containing states of all agents ("on" state is assumed to be
        encoded by 1, while "off" state is assumed to be encoded by -1)
    warmup : int, optional
        number of warmup steps to perform (so that the model could have a
        chance to "forget" the initial state). Zero by default.
    
    Returns
    -------
    array_like
        array of state observations (if parameters are valid) or array of None
        (if parameters are not valid)
        
    See also
    --------
    step, rawSeries
    """
    series=rawSeries(nPoints, sOn, sOff, herd, state, warmup=warmup)
    
    nseries=np.zeros(series.shape)
    
    nseries[series<0]=(np.random.rand(np.sum(series<0))<pOff)
    nseries[series>0]=(np.random.rand(np.sum(series>0))<pOn)
    
    return nseries
