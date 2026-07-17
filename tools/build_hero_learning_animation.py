#!/usr/bin/env python3
"""Build editable SVG fallbacks and Lottie JSON variants for the homepage hero system diagram."""
import json
from pathlib import Path
OUT=Path('assets/animations'); OUT.mkdir(parents=True,exist_ok=True)
W,H,FR,OP=720,620,24,240
nodes={'Reading':(360,70),'Understanding':(360,150),'Opportunity':(360,230),'Product':(240,330),'Strategy':(480,330),'Experiment':(360,430),'Learning':(360,510),'Better Ideas':(360,560)}
edges=[('Reading','Understanding'),('Understanding','Opportunity'),('Opportunity','Product'),('Opportunity','Strategy'),('Product','Experiment'),('Strategy','Experiment'),('Experiment','Learning'),('Learning','Better Ideas')]
return_path=[(438,560),(610,560),(610,70),(436,70)]
variants={'light':{'text':'#2f2922','line':'#6f675b','accent':'#b65f36','fill':'#fffaf1'},'dark':{'text':'#f0f0f0','line':'#9e9e9e','accent':'#d98b5f','fill':'#1a1511'}}
def rgb(h): h=h.lstrip('#'); return [round(int(h[i:i+2],16)/255,4) for i in (0,2,4)]
def K(v): return {'a':0,'k':v}
def layer(n,shapes,op=100): return {'ddd':0,'ind':0,'ty':4,'nm':n,'sr':1,'ks':{'o':K(op),'r':K(0),'p':K([0,0,0]),'a':K([0,0,0]),'s':K([100,100,100])},'ao':0,'shapes':shapes,'ip':0,'op':OP,'st':0,'bm':0}
def text(t,x,y,c): return {'ddd':0,'ind':0,'ty':5,'nm':'label '+t,'sr':1,'ks':{'o':K(82),'r':K(0),'p':K([x,y+5,0]),'a':K([0,0,0]),'s':K([100,100,100])},'ao':0,'t':{'d':{'k':[{'s':{'s':15,'f':'Inter','t':t,'j':2,'tr':0,'lh':18,'ls':0,'fc':rgb(c['text'])},'t':0}]},'p':{},'m':{'g':1,'a':K([0,0])}},'ip':0,'op':OP,'st':0,'bm':0}
def node(t,x,y,c):
 w=max(96,len(t)*8+34); h=42
 return layer('node '+t,[{'ty':'gr','it':[{'ty':'rc','d':1,'s':K([w,h]),'p':K([x,y]),'r':K(12)},{'ty':'st','c':K(rgb(c['line'])),'o':K(30),'w':K(1.2),'lc':2,'lj':2},{'ty':'fl','c':K(rgb(c['fill'])),'o':K(18),'r':1},{'ty':'tr','p':K([0,0]),'a':K([0,0]),'s':K([100,100]),'r':K(0),'o':K(100)}]}])
def line(n,pts,c,op=32,dash=False):
 st={'ty':'st','c':K(rgb(c['line'])),'o':K(op),'w':K(1.4),'lc':2,'lj':2}
 if dash: st['d']=[{'n':'d','v':K(7)},{'n':'g','v':K(9)}]
 return layer(n,[{'ty':'gr','it':[{'ty':'sh','ks':K({'i':[[0,0] for _ in pts],'o':[[0,0] for _ in pts],'v':[[x,y] for x,y in pts],'c':False})},st,{'ty':'tr','p':K([0,0]),'a':K([0,0]),'s':K([100,100]),'r':K(0),'o':K(100)}]}])
def dot(x,y,c): return layer('connection point',[{'ty':'gr','it':[{'ty':'el','p':K([x,y]),'s':K([8,8])},{'ty':'fl','c':K(rgb(c['line'])),'o':K(42),'r':1},{'ty':'tr','p':K([0,0]),'a':K([0,0]),'s':K([100,100]),'r':K(0),'o':K(100)}]}])
def particle(n,positions,c,start,end):
 keys=[]
 for t,(x,y) in positions: keys.append({'t':t,'s':[x,y,0],'i':{'x':[0.42],'y':[1]},'o':{'x':[0.42],'y':[0]}})
 return {'ddd':0,'ind':0,'ty':4,'nm':n,'sr':1,'ks':{'o':{'a':1,'k':[{'t':0,'s':[0]},{'t':start+4,'s':[0],'e':[100]},{'t':end,'s':[100],'e':[0]},{'t':end+12,'s':[0]}]},'r':K(0),'p':{'a':1,'k':keys},'a':K([0,0,0]),'s':K([100,100,100])},'ao':0,'shapes':[{'ty':'gr','it':[{'ty':'el','p':K([0,0]),'s':K([9,9])},{'ty':'fl','c':K(rgb(c['accent'])),'o':K(100),'r':1},{'ty':'tr','p':K([0,0]),'a':K([0,0]),'s':K([100,100]),'r':K(0),'o':K(100)}]}],'ip':0,'op':OP,'st':0,'bm':0}
def lottie(c):
 layers=[line('subtle return loop',return_path,c,18,True)]
 for a,b in edges:
  ax,ay=nodes[a]; bx,by=nodes[b]; layers.append(line(f'{a} to {b}',[(ax,ay+24),(bx,by-24)],c,32,a=='Learning'))
 for label,(x,y) in nodes.items(): layers += [node(label,x,y,c),text(label,x,y,c),dot(x,y,c)]
 layers += [particle('idea particle main',[(0,nodes['Reading']),(32,nodes['Understanding']),(64,nodes['Opportunity']),(118,nodes['Experiment']),(152,nodes['Learning']),(188,nodes['Better Ideas']),(230,nodes['Reading'])],c,0,206),particle('idea particle product branch',[(66,nodes['Opportunity']),(90,nodes['Product']),(118,nodes['Experiment'])],c,64,124),particle('idea particle strategy branch',[(72,nodes['Opportunity']),(96,nodes['Strategy']),(118,nodes['Experiment'])],c,70,126)]
 return {'v':'5.9.0','fr':FR,'ip':0,'op':OP,'w':W,'h':H,'nm':'Hero learning system','ddd':0,'assets':[],'layers':list(reversed(layers))}
def svg(c):
 s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">','<title id="title">Continuous learning system</title>','<desc id="desc">A systems diagram showing reading becoming understanding, opportunity, product strategy, experiments, learning, and better ideas.</desc>',f'<g fill="none" stroke="{c["line"]}" stroke-opacity="0.32" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">']
 for a,b in edges:
  ax,ay=nodes[a]; bx,by=nodes[b]; dash=' stroke-dasharray="7 9"' if a=='Learning' else ''; s.append(f'<path d="M {ax} {ay+24} L {bx} {by-24}"{dash}/>')
 s.append('<path d="M 438 560 L 610 560 L 610 70 L 436 70" stroke-dasharray="7 9" stroke-opacity="0.18"/>'); s.append('</g>')
 for label,(x,y) in nodes.items():
  w=max(96,len(label)*8+34); s.append(f'<rect x="{x-w/2:.1f}" y="{y-21}" width="{w}" height="42" rx="12" fill="{c["fill"]}" fill-opacity="0.18" stroke="{c["line"]}" stroke-opacity="0.30"/>'); s.append(f'<circle cx="{x}" cy="{y}" r="4" fill="{c["line"]}" fill-opacity="0.42"/>'); s.append(f'<text x="{x}" y="{y+5}" text-anchor="middle" font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="15" fill="{c["text"]}" fill-opacity="0.82">{label}</text>')
 return '\n'.join(s+['</svg>'])
source={'canvas':{'width':W,'height':H,'fps':FR,'duration_seconds':10},'nodes':nodes,'edges':edges,'return_path':return_path,'motion':'Main particle flows vertically; two branch particles split from Opportunity through Product and Strategy, then reconnect at Experiment. Diagram remains stationary with transparent background.'}
(OUT/'hero-learning-system.source.json').write_text(json.dumps(source,indent=2))
for name,c in variants.items():
 (OUT/f'hero-learning-system-{name}.json').write_text(json.dumps(lottie(c),separators=(',',':')))
 (OUT/f'hero-learning-system-{name}.svg').write_text(svg(c))
