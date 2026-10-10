"""Attach scoped parent trace and the invariant corpus once to its legal owner."""
from render_layer import DATA, ROOT, NAMES, fca, source_link, message

INVARIANT_OWNERS = {
'L0':[1,16,24,25,40,41], 'L1':[32,33,37],
'L2':[5,6,9,10,11,15,23,29,30,45,46,50],
'L3':[2,3,7,12,19,20,21,22,31,34,35,36,43,44,48,49],
'L4':[4,17,18,26,38,39,42,47], 'L5':[8,27,28], 'L6':[13,14], 'L7':[]}
assert sorted(n for numbers in INVARIANT_OWNERS.values() for n in numbers)==list(range(1,51))

def complete():
    for layer,numbers in INVARIANT_OWNERS.items():
        path=ROOT/'architecture'/(NAMES[layer]+'.md')
        text=path.read_text(encoding='utf-8')
        if layer!='L0':
            text=text.split('\n## Owned FCA invariant obligations')[0]
        if layer=='L2':
            text=text.split('\n## Parent entity clause crosswalk')[0]
        if layer!='L0' and numbers:
            text+='\n## Owned FCA invariant obligations\n\nThese parent duties retain their semantic force. Scoped RDMS amendments determine effective record lifecycle and representation; derived staleness must not be confused with a canonical lifecycle mutation.\n\n'
            for n in numbers:
                inv=next(i for i in DATA['fca_invariants'] if i['unit_id']==f'FCA-I{n:02d}')
                text+=inv['raw']+'\n\nSource: '+source_link(inv)+'.\n\n'
        if layer=='L2':
            text+='\n## Parent entity clause crosswalk\n\n'
            for n,target in [(8,'L2-E03'),(15,'L2-E05 / L2-E06'),(17,'L2-E07 / L2-E08'),(29,'L2-E11 / L2-E12')]:
                text+=f'- {source_link(fca(n))}: effective entity/lifecycle scope is represented in {target} and the sole-owner record contracts. Parent field conversion is separately unresolved; the old schema is not reintroduced.\n'
            for s in message(17)['segments']:
                if 'ADDITIONAL FORMAL INVARIANTS' in s['heading']:
                    from render_layer import retained_prose
                    text+='\n'+retained_prose({**s,'source_path':message(17)['source_path']},'L2-X-INV')
        path.write_text(text.rstrip()+'\n',encoding='utf-8',newline='\n')

if __name__=='__main__':
    complete()
