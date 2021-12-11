#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 16:51:26 2021

@author: antoine
"""


import numpy as np
import pandas as pd

from scipy.optimize import minimize



def MCR_calc(alloc,Returns):
    ptf=np.multiply(Returns,alloc);
    ptfReturns=np.sum(ptf,1); # Summing across columns
    vol_ptf=np.std(ptfReturns);
    Sigma=Returns.cov()
    MCR=np.dot(Sigma,alloc)/vol_ptf;
    return MCR


def ERC(alloc,Returns):
    ptf=np.multiply(Returns,alloc);
    ptfReturns=np.sum(ptf,1); # Summing across columns
    vol_ptf=np.std(ptfReturns);
    indiv_ERC=alloc*MCR_calc(alloc,Returns);
    criterion=np.power(indiv_ERC-vol_ptf/len(alloc),2)
    criterion=np.sum(criterion)*1000000
    return criterion

def get_weights(pc_ret):

    x0 = np.array([0]*np.size(pc_ret,1))+0.1
    cons=({'type':'eq', 'fun': lambda x:sum(x)-1})

    Bounds= [(0 , 1) for i in range(0,len(x0))]

    res_ERC = minimize(ERC, x0, method='SLSQP', args=(pc_ret.iloc[:,:]),bounds=Bounds,constraints=cons,options={'disp': True})
    
    return res_ERC.x


def portfolio_return(weights, returns):
    """
    Computes the return on a portfolio from constituent returns and weights
    weights are a numpy array or Nx1 matrix and returns are a numpy array or Nx1 matrix
    """
    return weights.T @ returns