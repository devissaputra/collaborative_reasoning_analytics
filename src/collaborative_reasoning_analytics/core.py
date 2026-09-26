# Calculation reading guide: ../CALCULATIONS.md (repository root).
# Uptake proxy = |tokens(previous) ∩ tokens(current)| / |union|.
# This is lexical overlap, not semantic understanding. Participation entropy is normalized by the number of observed speakers. Turn order must belong to one conversation; mixing conversations would create invalid adjacency.

from __future__ import annotations
import re, math, pandas as pd

def tokens(text:str)->set[str]: return {w for w in re.findall(r"[a-zA-Z']+",(text or '').lower()) if len(w)>2}
def semantic_uptake(previous:str,current:str)->float:
    a,b=tokens(previous),tokens(current); return 0.0 if not a or not b else len(a&b)/len(a|b)
def classify_move(text:str)->str:
    t=(text or '').lower()
    if any(x in t for x in ['evidence','source','how do we know']): return 'evidence_request'
    if any(x in t for x in ['i disagree','but','however','not necessarily']): return 'challenge'
    if any(x in t for x in ['because','therefore','so that means']): return 'reasoning'
    if any(x in t for x in ['building on','your point','as you said']): return 'uptake'
    return 'other'
def participation_balance(df:pd.DataFrame)->float:
    shares=df.speaker.value_counts(normalize=True).to_numpy(); n=len(shares)
    if n<=1: return 0.0
    h=-sum(p*math.log(p) for p in shares if p>0)/math.log(n); return float(h)
def conversation_metrics(df:pd.DataFrame)->dict:
    d=df.sort_values('turn').copy(); prev=d.text.shift(1).fillna(''); d['uptake']=[semantic_uptake(a,b) for a,b in zip(prev,d.text)]; d['move']=d.text.map(classify_move)
    return {'mean_uptake':float(d.uptake.iloc[1:].mean()),'participation_balance':participation_balance(d),'reasoning_move_rate':float((d.move=='reasoning').mean()),'evidence_request_rate':float((d.move=='evidence_request').mean()),'challenge_rate':float((d.move=='challenge').mean())}
