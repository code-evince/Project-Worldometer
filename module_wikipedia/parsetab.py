
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BEGININFO CLOSEDATA CLOSEDIV CLOSEH3 CLOSEHREF CLOSEROW CLOSESPAN CLOSESTYLE CONTENT ENDINFO GARBAGE NBSP OPENDATA OPENDIV OPENH3 OPENHREF OPENROW OPENSPAN OPENSTYLEstart : tableskipall : OPENHREF skipall\n                | CLOSEHREF skipall\n                | OPENDATA skipall\n                | CLOSEDATA skipall\n                | CONTENT skipall\n                | emptyskiptag : CONTENT skiptag\n            | emptytable : BEGININFO skiptag news skiptag ENDINFOdate : OPENH3 CONTENT textdata CLOSEH3textdata : CONTENT textdata\n                | emptynews : date textdata news\n            | date textdata\n            | emptycontent : CONTENT\n            | emptyempty :'
    
_lr_action_items = {'BEGININFO':([0,],[3,]),'$end':([1,2,17,],[0,-1,-10,]),'CONTENT':([3,4,5,6,7,8,9,10,11,13,14,15,16,18,19,21,],[5,-19,5,-9,5,14,-16,16,-8,-15,14,-13,14,-14,-12,-11,]),'OPENH3':([3,4,5,6,8,11,13,14,15,19,21,],[-19,10,-19,-9,-19,-8,10,-19,-13,-12,-11,]),'ENDINFO':([3,4,5,6,7,8,9,11,12,13,14,15,18,19,21,],[-19,-19,-19,-9,-19,-19,-16,-8,17,-15,-19,-13,-14,-12,-11,]),'CLOSEH3':([14,15,16,19,20,],[-19,-13,-19,-12,21,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'table':([0,],[2,]),'skiptag':([3,5,7,],[4,11,12,]),'empty':([3,4,5,7,8,13,14,16,],[6,9,6,6,15,9,15,15,]),'news':([4,13,],[7,18,]),'date':([4,13,],[8,8,]),'textdata':([8,14,16,],[13,19,20,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> table','start',1,'p_start','wiki_parser_2019.py',98),
  ('skipall -> OPENHREF skipall','skipall',2,'p_skipall','wiki_parser_2019.py',102),
  ('skipall -> CLOSEHREF skipall','skipall',2,'p_skipall','wiki_parser_2019.py',103),
  ('skipall -> OPENDATA skipall','skipall',2,'p_skipall','wiki_parser_2019.py',104),
  ('skipall -> CLOSEDATA skipall','skipall',2,'p_skipall','wiki_parser_2019.py',105),
  ('skipall -> CONTENT skipall','skipall',2,'p_skipall','wiki_parser_2019.py',106),
  ('skipall -> empty','skipall',1,'p_skipall','wiki_parser_2019.py',107),
  ('skiptag -> CONTENT skiptag','skiptag',2,'p_skiptag','wiki_parser_2019.py',110),
  ('skiptag -> empty','skiptag',1,'p_skiptag','wiki_parser_2019.py',111),
  ('table -> BEGININFO skiptag news skiptag ENDINFO','table',5,'p_table','wiki_parser_2019.py',114),
  ('date -> OPENH3 CONTENT textdata CLOSEH3','date',4,'p_date','wiki_parser_2019.py',118),
  ('textdata -> CONTENT textdata','textdata',2,'p_textdata','wiki_parser_2019.py',123),
  ('textdata -> empty','textdata',1,'p_textdata','wiki_parser_2019.py',124),
  ('news -> date textdata news','news',3,'p_news','wiki_parser_2019.py',131),
  ('news -> date textdata','news',2,'p_news','wiki_parser_2019.py',132),
  ('news -> empty','news',1,'p_news','wiki_parser_2019.py',133),
  ('content -> CONTENT','content',1,'p_content','wiki_parser_2019.py',144),
  ('content -> empty','content',1,'p_content','wiki_parser_2019.py',145),
  ('empty -> <empty>','empty',0,'p_empty','wiki_parser_2019.py',149),
]
