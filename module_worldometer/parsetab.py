
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BEGINTABLEA CLOSEDATA CLOSEDIV CLOSEHEADER CLOSEHREF CLOSEROW CLOSESPAN CLOSESTYLE CLOSETABLE CONTENT GARBAGE OPENDATA OPENDIV OPENHEADER OPENHREF OPENROW OPENSPAN OPENSTYLE OPENTABLE SEPA TABLEH TABLET THEAD_CLOSE THEAD_OPEN spa spostart : tableskiptag : CONTENT skiptag\n               | OPENHREF skiptag\n               | CLOSEHREF skiptag\n               | OPENDATA skiptag\n               | CLOSEDATA skiptag\n               | OPENHEADER skiptag\n               | CLOSEHEADER skiptag\n               | THEAD_OPEN skiptag\n               | THEAD_CLOSE skiptag\n               | OPENTABLE skiptag\n               | CLOSETABLE skiptag\n               | CLOSEROW skiptag\n               | emptytable : BEGINTABLEA skiptag OPENROW startrow CLOSETABLE\n     startrow : firstrow CLOSEROW startrow\n                 | OPENROW getcell CLOSEROW startrow\n                 | empty\n       firstrow : OPENDATA content CLOSEDATA firstrow\n                | empty\n    content : CONTENT CONTENT CONTENT CONTENT\n                | CONTENT CONTENT CONTENT\n                | CONTENT CONTENT\n                | CONTENT\n                | empty\n    getcell : OPENDATA content CLOSEDATA skipdata getcell\n               | empty\n    skipdata : CONTENT skipdata\n               | CLOSEDATA skipdata\n               | emptyempty :'
    
_lr_action_items = {'BEGINTABLEA':([0,],[3,]),'$end':([1,2,39,],[0,-1,-15,]),'CONTENT':([3,5,6,7,8,9,10,11,12,13,14,15,16,35,37,42,48,50,53,54,56,],[6,6,6,6,6,6,6,6,6,6,6,6,6,42,42,48,53,56,58,56,56,]),'OPENHREF':([3,5,6,7,8,9,10,11,12,13,14,15,16,],[7,7,7,7,7,7,7,7,7,7,7,7,7,]),'CLOSEHREF':([3,5,6,7,8,9,10,11,12,13,14,15,16,],[8,8,8,8,8,8,8,8,8,8,8,8,8,]),'OPENDATA':([3,5,6,7,8,9,10,11,12,13,14,15,16,18,31,40,44,47,50,54,55,56,57,59,61,],[9,9,9,9,9,9,9,9,9,9,9,9,9,35,37,35,35,35,-31,-31,37,-31,-30,-29,-28,]),'CLOSEDATA':([3,5,6,7,8,9,10,11,12,13,14,15,16,35,37,41,42,43,45,48,50,53,54,56,58,],[10,10,10,10,10,10,10,10,10,10,10,10,10,-31,-31,47,-24,-25,50,-23,54,-22,54,54,-21,]),'OPENHEADER':([3,5,6,7,8,9,10,11,12,13,14,15,16,],[11,11,11,11,11,11,11,11,11,11,11,11,11,]),'CLOSEHEADER':([3,5,6,7,8,9,10,11,12,13,14,15,16,],[12,12,12,12,12,12,12,12,12,12,12,12,12,]),'THEAD_OPEN':([3,5,6,7,8,9,10,11,12,13,14,15,16,],[13,13,13,13,13,13,13,13,13,13,13,13,13,]),'THEAD_CLOSE':([3,5,6,7,8,9,10,11,12,13,14,15,16,],[14,14,14,14,14,14,14,14,14,14,14,14,14,]),'OPENTABLE':([3,5,6,7,8,9,10,11,12,13,14,15,16,],[15,15,15,15,15,15,15,15,15,15,15,15,15,]),'CLOSETABLE':([3,5,6,7,8,9,10,11,12,13,14,15,16,18,32,34,40,44,46,49,],[5,5,5,5,5,5,5,5,5,5,5,5,5,-31,39,-18,-31,-31,-16,-17,]),'CLOSEROW':([3,5,6,7,8,9,10,11,12,13,14,15,16,18,31,33,34,36,38,40,44,47,50,51,52,54,55,56,57,59,60,61,],[16,16,16,16,16,16,16,16,16,16,16,16,16,-31,-31,40,-20,44,-27,-31,-31,-31,-31,-19,-20,-31,-31,-31,-30,-29,-26,-28,]),'OPENROW':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,40,44,],[-31,18,-31,-31,-31,-31,-31,-31,-31,-31,-31,-31,-31,-31,-14,31,-12,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-13,31,31,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'table':([0,],[2,]),'skiptag':([3,5,6,7,8,9,10,11,12,13,14,15,16,],[4,19,20,21,22,23,24,25,26,27,28,29,30,]),'empty':([3,5,6,7,8,9,10,11,12,13,14,15,16,18,31,35,37,40,44,47,50,54,55,56,],[17,17,17,17,17,17,17,17,17,17,17,17,17,34,38,43,43,34,34,52,57,57,38,57,]),'startrow':([18,40,44,],[32,46,49,]),'firstrow':([18,40,44,47,],[33,33,33,51,]),'getcell':([31,55,],[36,60,]),'content':([35,37,],[41,45,]),'skipdata':([50,54,56,],[55,59,61,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> table','start',1,'p_start','worldometer.py',132),
  ('skiptag -> CONTENT skiptag','skiptag',2,'p_skiptag','worldometer.py',137),
  ('skiptag -> OPENHREF skiptag','skiptag',2,'p_skiptag','worldometer.py',138),
  ('skiptag -> CLOSEHREF skiptag','skiptag',2,'p_skiptag','worldometer.py',139),
  ('skiptag -> OPENDATA skiptag','skiptag',2,'p_skiptag','worldometer.py',140),
  ('skiptag -> CLOSEDATA skiptag','skiptag',2,'p_skiptag','worldometer.py',141),
  ('skiptag -> OPENHEADER skiptag','skiptag',2,'p_skiptag','worldometer.py',142),
  ('skiptag -> CLOSEHEADER skiptag','skiptag',2,'p_skiptag','worldometer.py',143),
  ('skiptag -> THEAD_OPEN skiptag','skiptag',2,'p_skiptag','worldometer.py',144),
  ('skiptag -> THEAD_CLOSE skiptag','skiptag',2,'p_skiptag','worldometer.py',145),
  ('skiptag -> OPENTABLE skiptag','skiptag',2,'p_skiptag','worldometer.py',146),
  ('skiptag -> CLOSETABLE skiptag','skiptag',2,'p_skiptag','worldometer.py',147),
  ('skiptag -> CLOSEROW skiptag','skiptag',2,'p_skiptag','worldometer.py',148),
  ('skiptag -> empty','skiptag',1,'p_skiptag','worldometer.py',149),
  ('table -> BEGINTABLEA skiptag OPENROW startrow CLOSETABLE','table',5,'p_table','worldometer.py',153),
  ('startrow -> firstrow CLOSEROW startrow','startrow',3,'p_startrow','worldometer.py',158),
  ('startrow -> OPENROW getcell CLOSEROW startrow','startrow',4,'p_startrow','worldometer.py',159),
  ('startrow -> empty','startrow',1,'p_startrow','worldometer.py',160),
  ('firstrow -> OPENDATA content CLOSEDATA firstrow','firstrow',4,'p_firstrow','worldometer.py',170),
  ('firstrow -> empty','firstrow',1,'p_firstrow','worldometer.py',171),
  ('content -> CONTENT CONTENT CONTENT CONTENT','content',4,'p_content','worldometer.py',180),
  ('content -> CONTENT CONTENT CONTENT','content',3,'p_content','worldometer.py',181),
  ('content -> CONTENT CONTENT','content',2,'p_content','worldometer.py',182),
  ('content -> CONTENT','content',1,'p_content','worldometer.py',183),
  ('content -> empty','content',1,'p_content','worldometer.py',184),
  ('getcell -> OPENDATA content CLOSEDATA skipdata getcell','getcell',5,'p_getcell','worldometer.py',201),
  ('getcell -> empty','getcell',1,'p_getcell','worldometer.py',202),
  ('skipdata -> CONTENT skipdata','skipdata',2,'p_skipdata','worldometer.py',207),
  ('skipdata -> CLOSEDATA skipdata','skipdata',2,'p_skipdata','worldometer.py',208),
  ('skipdata -> empty','skipdata',1,'p_skipdata','worldometer.py',209),
  ('empty -> <empty>','empty',0,'p_empty','worldometer.py',213),
]
