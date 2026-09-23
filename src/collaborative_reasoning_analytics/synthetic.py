import numpy as np, pandas as pd

def make_dialogue(n_turns=180,seed=31):
    rng=np.random.default_rng(seed); speakers=['A','B','C','D']; templates=['I think the evidence supports the first explanation','Building on your point, the evidence also shows a timing effect','However, I disagree because the second condition changes the result','How do we know this? What source supports it?','Therefore the group should test the alternative explanation','I have another example that might fit the pattern']
    return pd.DataFrame([{'turn':i,'speaker':rng.choice(speakers,p=[.3,.27,.23,.2]),'text':rng.choice(templates)} for i in range(n_turns)])
