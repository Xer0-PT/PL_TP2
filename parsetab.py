
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NUMBER OPERATOR SIGN VAR back bk fd forward home left lt make pd pendown penup pu repeat right rt setpencolor setpos setx setxy sety while program : command  program : program command  command : forward NUMBER \n                    | fd NUMBER \n                    | forward \':\' VAR\n                    | fd \':\' VAR  command : right NUMBER \n                    | rt NUMBER\n                    | right \':\' VAR\n                    | rt \':\' VAR  command : back NUMBER \n                    | bk NUMBER\n                    | back \':\' VAR\n                    | bk \':\' VAR  command : left NUMBER \n                    | lt NUMBER\n                    | left \':\' VAR\n                    | lt \':\' VAR  command : setpos \'[\' NUMBER NUMBER \']\'\n                    | setxy NUMBER NUMBER\n                    | setpos \'[\' \':\' VAR NUMBER \']\'\n                    | setpos \'[\' NUMBER \':\' VAR \']\'\n                    | setpos \'[\' \':\' VAR \':\' VAR \']\'\n                    | setxy \':\' VAR NUMBER\n                    | setxy NUMBER \':\' VAR\n                    | setxy \':\' VAR \':\' VAR  command : setx NUMBER \n                    | setx \':\' VAR command : sety NUMBER\n                    | sety \':\' VAR  command : home  command : pendown\n                    | pd  command : penup\n                    | pu  command : setpencolor \'[\' NUMBER NUMBER NUMBER \']\'\n                    | setpencolor \'[\' NUMBER NUMBER \':\' VAR \']\'\n                    | setpencolor \'[\' NUMBER \':\' VAR NUMBER \']\'\n                    | setpencolor \'[\' NUMBER \':\' VAR \':\' VAR \']\'\n                    | setpencolor \'[\' \':\' VAR NUMBER NUMBER \']\' \n                    | setpencolor \'[\' \':\' VAR NUMBER \':\' VAR \']\'\n                    | setpencolor \'[\' \':\' VAR \':\' VAR NUMBER \']\'\n                    | setpencolor \'[\' \':\' VAR \':\' VAR \':\' VAR \']\'  command : make \'"\' VAR NUMBER\n                    | make \'"\' VAR \':\' VAR OPERATOR NUMBER\n                    | make \'"\' VAR NUMBER OPERATOR \':\' VAR  command : repeat NUMBER \'[\' program \']\' \n                    | repeat \':\' VAR \'[\' program \']\'  command : while \'[\' \':\' VAR SIGN NUMBER \']\' \'[\' program \']\' '
    
_lr_action_items = {'forward':([0,1,2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,71,77,79,83,85,86,88,92,100,101,103,105,106,115,117,118,119,124,125,126,128,130,131,132,133,134,135,],[3,3,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,3,-25,-24,-44,3,3,-19,-26,-47,3,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-39,-42,-41,3,-43,3,-49,]),'fd':([0,1,2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,71,77,79,83,85,86,88,92,100,101,103,105,106,115,117,118,119,124,125,126,128,130,131,132,133,134,135,],[4,4,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,4,-25,-24,-44,4,4,-19,-26,-47,4,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-39,-42,-41,4,-43,4,-49,]),'right':([0,1,2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,71,77,79,83,85,86,88,92,100,101,103,105,106,115,117,118,119,124,125,126,128,130,131,132,133,134,135,],[5,5,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,5,-25,-24,-44,5,5,-19,-26,-47,5,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-39,-42,-41,5,-43,5,-49,]),'rt':([0,1,2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,71,77,79,83,85,86,88,92,100,101,103,105,106,115,117,118,119,124,125,126,128,130,131,132,133,134,135,],[6,6,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,6,-25,-24,-44,6,6,-19,-26,-47,6,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-39,-42,-41,6,-43,6,-49,]),'back':([0,1,2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,71,77,79,83,85,86,88,92,100,101,103,105,106,115,117,118,119,124,125,126,128,130,131,132,133,134,135,],[7,7,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,7,-25,-24,-44,7,7,-19,-26,-47,7,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-39,-42,-41,7,-43,7,-49,]),'bk':([0,1,2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,71,77,79,83,85,86,88,92,100,101,103,105,106,115,117,118,119,124,125,126,128,130,131,132,133,134,135,],[8,8,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,8,-25,-24,-44,8,8,-19,-26,-47,8,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-39,-42,-41,8,-43,8,-49,]),'left':([0,1,2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,71,77,79,83,85,86,88,92,100,101,103,105,106,115,117,118,119,124,125,126,128,130,131,132,133,134,135,],[9,9,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,9,-25,-24,-44,9,9,-19,-26,-47,9,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-39,-42,-41,9,-43,9,-49,]),'lt':([0,1,2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,71,77,79,83,85,86,88,92,100,101,103,105,106,115,117,118,119,124,125,126,128,130,131,132,133,134,135,],[10,10,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,10,-25,-24,-44,10,10,-19,-26,-47,10,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-39,-42,-41,10,-43,10,-49,]),'setpos':([0,1,2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,71,77,79,83,85,86,88,92,100,101,103,105,106,115,117,118,119,124,125,126,128,130,131,132,133,134,135,],[11,11,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,11,-25,-24,-44,11,11,-19,-26,-47,11,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-39,-42,-41,11,-43,11,-49,]),'setxy':([0,1,2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,71,77,79,83,85,86,88,92,100,101,103,105,106,115,117,118,119,124,125,126,128,130,131,132,133,134,135,],[12,12,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,12,-25,-24,-44,12,12,-19,-26,-47,12,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-39,-42,-41,12,-43,12,-49,]),'setx':([0,1,2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,71,77,79,83,85,86,88,92,100,101,103,105,106,115,117,118,119,124,125,126,128,130,131,132,133,134,135,],[13,13,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,13,-25,-24,-44,13,13,-19,-26,-47,13,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-39,-42,-41,13,-43,13,-49,]),'sety':([0,1,2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,71,77,79,83,85,86,88,92,100,101,103,105,106,115,117,118,119,124,125,126,128,130,131,132,133,134,135,],[14,14,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,14,-25,-24,-44,14,14,-19,-26,-47,14,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-39,-42,-41,14,-43,14,-49,]),'home':([0,1,2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,71,77,79,83,85,86,88,92,100,101,103,105,106,115,117,118,119,124,125,126,128,130,131,132,133,134,135,],[15,15,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,15,-25,-24,-44,15,15,-19,-26,-47,15,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-39,-42,-41,15,-43,15,-49,]),'pendown':([0,1,2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,71,77,79,83,85,86,88,92,100,101,103,105,106,115,117,118,119,124,125,126,128,130,131,132,133,134,135,],[16,16,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,16,-25,-24,-44,16,16,-19,-26,-47,16,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-39,-42,-41,16,-43,16,-49,]),'pd':([0,1,2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,71,77,79,83,85,86,88,92,100,101,103,105,106,115,117,118,119,124,125,126,128,130,131,132,133,134,135,],[17,17,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,17,-25,-24,-44,17,17,-19,-26,-47,17,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-39,-42,-41,17,-43,17,-49,]),'penup':([0,1,2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,71,77,79,83,85,86,88,92,100,101,103,105,106,115,117,118,119,124,125,126,128,130,131,132,133,134,135,],[18,18,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,18,-25,-24,-44,18,18,-19,-26,-47,18,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-39,-42,-41,18,-43,18,-49,]),'pu':([0,1,2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,71,77,79,83,85,86,88,92,100,101,103,105,106,115,117,118,119,124,125,126,128,130,131,132,133,134,135,],[19,19,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,19,-25,-24,-44,19,19,-19,-26,-47,19,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-39,-42,-41,19,-43,19,-49,]),'setpencolor':([0,1,2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,71,77,79,83,85,86,88,92,100,101,103,105,106,115,117,118,119,124,125,126,128,130,131,132,133,134,135,],[20,20,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,20,-25,-24,-44,20,20,-19,-26,-47,20,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-39,-42,-41,20,-43,20,-49,]),'make':([0,1,2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,71,77,79,83,85,86,88,92,100,101,103,105,106,115,117,118,119,124,125,126,128,130,131,132,133,134,135,],[21,21,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,21,-25,-24,-44,21,21,-19,-26,-47,21,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-39,-42,-41,21,-43,21,-49,]),'repeat':([0,1,2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,71,77,79,83,85,86,88,92,100,101,103,105,106,115,117,118,119,124,125,126,128,130,131,132,133,134,135,],[22,22,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,22,-25,-24,-44,22,22,-19,-26,-47,22,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-39,-42,-41,22,-43,22,-49,]),'while':([0,1,2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,71,77,79,83,85,86,88,92,100,101,103,105,106,115,117,118,119,124,125,126,128,130,131,132,133,134,135,],[23,23,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,23,-25,-24,-44,23,23,-19,-26,-47,23,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-39,-42,-41,23,-43,23,-49,]),'$end':([1,2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,77,79,83,88,92,100,103,105,106,115,117,118,119,124,125,126,128,130,131,133,135,],[0,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,-25,-24,-44,-19,-26,-47,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-39,-42,-41,-43,-49,]),']':([2,15,16,17,18,19,24,25,27,29,31,33,35,37,39,44,46,53,54,55,56,57,58,59,60,63,66,67,74,77,79,83,85,88,89,91,92,93,100,101,103,104,105,106,107,108,112,115,116,117,118,119,120,122,123,124,125,126,128,129,130,131,133,134,135,],[-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,88,-25,-24,-44,100,-19,103,105,-26,106,-47,115,-22,117,-21,-36,118,119,124,-48,127,-23,-37,-38,128,130,131,-40,-46,-45,-39,133,-42,-41,-43,135,-49,]),'NUMBER':([3,4,5,6,7,8,9,10,12,13,14,22,41,42,48,61,65,68,70,76,80,82,95,97,102,110,114,],[25,27,29,31,33,35,37,39,42,44,46,50,61,63,68,74,79,80,83,91,93,97,108,112,116,122,126,]),':':([3,4,5,6,7,8,9,10,12,13,14,22,41,42,48,52,61,65,68,70,76,80,82,95,97,98,110,],[26,28,30,32,34,36,38,40,43,45,47,51,62,64,69,73,75,78,81,84,90,94,96,109,111,113,121,]),'[':([11,20,23,50,72,127,],[41,48,52,71,86,132,]),'"':([21,],[49,]),'VAR':([26,28,30,32,34,36,38,40,43,45,47,49,51,62,64,69,73,75,78,81,84,90,94,96,109,111,113,121,],[53,54,55,56,57,58,59,60,65,66,67,70,72,76,77,82,87,89,92,95,99,104,107,110,120,123,125,129,]),'OPERATOR':([83,99,],[98,114,]),'SIGN':([87,],[102,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,71,86,132,],[1,85,101,134,]),'command':([0,1,71,85,86,101,132,134,],[2,24,2,24,2,24,2,24,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> command','program',1,'p_program0','Parser.py',71),
  ('program -> program command','program',2,'p_program1','Parser.py',76),
  ('command -> forward NUMBER','command',2,'p_command0','Parser.py',82),
  ('command -> fd NUMBER','command',2,'p_command0','Parser.py',83),
  ('command -> forward : VAR','command',3,'p_command0','Parser.py',84),
  ('command -> fd : VAR','command',3,'p_command0','Parser.py',85),
  ('command -> right NUMBER','command',2,'p_command1','Parser.py',93),
  ('command -> rt NUMBER','command',2,'p_command1','Parser.py',94),
  ('command -> right : VAR','command',3,'p_command1','Parser.py',95),
  ('command -> rt : VAR','command',3,'p_command1','Parser.py',96),
  ('command -> back NUMBER','command',2,'p_command2','Parser.py',103),
  ('command -> bk NUMBER','command',2,'p_command2','Parser.py',104),
  ('command -> back : VAR','command',3,'p_command2','Parser.py',105),
  ('command -> bk : VAR','command',3,'p_command2','Parser.py',106),
  ('command -> left NUMBER','command',2,'p_command3','Parser.py',114),
  ('command -> lt NUMBER','command',2,'p_command3','Parser.py',115),
  ('command -> left : VAR','command',3,'p_command3','Parser.py',116),
  ('command -> lt : VAR','command',3,'p_command3','Parser.py',117),
  ('command -> setpos [ NUMBER NUMBER ]','command',5,'p_command4','Parser.py',126),
  ('command -> setxy NUMBER NUMBER','command',3,'p_command4','Parser.py',127),
  ('command -> setpos [ : VAR NUMBER ]','command',6,'p_command4','Parser.py',128),
  ('command -> setpos [ NUMBER : VAR ]','command',6,'p_command4','Parser.py',129),
  ('command -> setpos [ : VAR : VAR ]','command',7,'p_command4','Parser.py',130),
  ('command -> setxy : VAR NUMBER','command',4,'p_command4','Parser.py',131),
  ('command -> setxy NUMBER : VAR','command',4,'p_command4','Parser.py',132),
  ('command -> setxy : VAR : VAR','command',5,'p_command4','Parser.py',133),
  ('command -> setx NUMBER','command',2,'p_command5','Parser.py',158),
  ('command -> setx : VAR','command',3,'p_command5','Parser.py',159),
  ('command -> sety NUMBER','command',2,'p_command6','Parser.py',166),
  ('command -> sety : VAR','command',3,'p_command6','Parser.py',167),
  ('command -> home','command',1,'p_command7','Parser.py',174),
  ('command -> pendown','command',1,'p_command8','Parser.py',178),
  ('command -> pd','command',1,'p_command8','Parser.py',179),
  ('command -> penup','command',1,'p_command9','Parser.py',183),
  ('command -> pu','command',1,'p_command9','Parser.py',184),
  ('command -> setpencolor [ NUMBER NUMBER NUMBER ]','command',6,'p_command10','Parser.py',188),
  ('command -> setpencolor [ NUMBER NUMBER : VAR ]','command',7,'p_command10','Parser.py',189),
  ('command -> setpencolor [ NUMBER : VAR NUMBER ]','command',7,'p_command10','Parser.py',190),
  ('command -> setpencolor [ NUMBER : VAR : VAR ]','command',8,'p_command10','Parser.py',191),
  ('command -> setpencolor [ : VAR NUMBER NUMBER ]','command',7,'p_command10','Parser.py',192),
  ('command -> setpencolor [ : VAR NUMBER : VAR ]','command',8,'p_command10','Parser.py',193),
  ('command -> setpencolor [ : VAR : VAR NUMBER ]','command',8,'p_command10','Parser.py',194),
  ('command -> setpencolor [ : VAR : VAR : VAR ]','command',9,'p_command10','Parser.py',195),
  ('command -> make " VAR NUMBER','command',4,'p_command11','Parser.py',225),
  ('command -> make " VAR : VAR OPERATOR NUMBER','command',7,'p_command11','Parser.py',226),
  ('command -> make " VAR NUMBER OPERATOR : VAR','command',7,'p_command11','Parser.py',227),
  ('command -> repeat NUMBER [ program ]','command',5,'p_command12','Parser.py',239),
  ('command -> repeat : VAR [ program ]','command',6,'p_command12','Parser.py',240),
  ('command -> while [ : VAR SIGN NUMBER ] [ program ]','command',10,'p_command13','Parser.py',249),
]
