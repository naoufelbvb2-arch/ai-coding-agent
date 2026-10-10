"""Preserve non-superseded baseline invariants with explicit scoped changes."""
import re
from render_layer import DATA, ROOT, NAMES, message, source_link

def add():
    layer_sources={'L3':[6],'L4':[9,12],'L5':[14],'L2':[16],'L6':[18],'L7':[23]}
    for layer,orders in layer_sources.items():
        path=ROOT/'architecture'/(NAMES[layer]+'.md')
        text=path.read_text(encoding='utf-8').split('\n## Retained RDMS invariant corpus')[0]
        text+='\n## Retained RDMS invariant corpus\n\nBaseline admission follows its final source freeze; the archived draft-status label is historical. Explicit replacements govern affected wording and all added invariant obligations remain in the amended articles.\n\n'
        for order in orders:
            source=next(s for s in message(order)['segments'] if 'INVARIANT' in s['heading'].upper())
            raw=source['raw']
            start=re.search(r'^RDMS(?:\d+)?-?I\d+',raw,re.M).start()
            raw=raw[start:].strip()
            if order==6:
                raw=raw.replace('PTY, EXEC and SERVICE are execution modes over a common\nProcess Runtime, not separate authorities.','ProcessLaunch invocation, interaction and lifetime dimensions share a common\nProcess Runtime and confer no separate authority (RDMS-04 C01-11).')
            text+='### '+layer+'-BI'+str(order)+'\n\n'+raw+'\n\nSource: '+source_link({**source,'source_path':message(order)['source_path']})+'.\n\n'
        if layer=='L2':
            source=next(s for s in message(2)['segments'] if s['heading'].startswith('74. '))
            text+='RDMS-02 baseline RDMS-I46 remains effective: canonical state is a composite view over normalized entities, not a single mutable state blob. Baseline RDMS-I23–45 are replaced by C01-35; the prior GoalStack and giant lifecycle statements are not reintroduced.\n\nSource: '+source_link({**source,'source_path':message(2)['source_path']})+'.\n'
        path.write_text(text,encoding='utf-8',newline='\n')

if __name__=='__main__':add()
