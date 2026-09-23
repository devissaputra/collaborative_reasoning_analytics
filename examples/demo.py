from pathlib import Path
import json
from collaborative_reasoning_analytics.synthetic import make_dialogue
from collaborative_reasoning_analytics.core import conversation_metrics,classify_move,semantic_uptake
root=Path(__file__).resolve().parents[1]; (root/'results').mkdir(exist_ok=True)
d=make_dialogue(); d['move']=d.text.map(classify_move); d['uptake']=[0.0]+[semantic_uptake(d.text.iloc[i-1],d.text.iloc[i]) for i in range(1,len(d))]; d.to_csv(root/'results'/'synthetic_dialogue.csv',index=False)
m=conversation_metrics(d); (root/'results'/'demo_metrics.json').write_text(json.dumps({k:round(v,3) for k,v in m.items()},indent=2)); print(json.dumps({k:round(v,3) for k,v in m.items()},indent=2))
