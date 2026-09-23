import pandas as pd
from collaborative_reasoning_analytics.core import semantic_uptake,classify_move,participation_balance,conversation_metrics

def test_moves():
    assert classify_move('How do we know this? What evidence?')=='evidence_request'
    assert classify_move('I disagree because that assumption fails')=='challenge'
    assert semantic_uptake('evidence supports claim','the evidence is weak')>0

def test_balance():
    d=pd.DataFrame({'speaker':['a','b','a','b']}); assert participation_balance(d)>.99
