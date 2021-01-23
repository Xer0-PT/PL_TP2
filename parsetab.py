
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'END NUMBER OPERATOR SIGN STR TO VAR back bk fd forward home if ifelse left lt make pd pendown penup pu repeat right rt setpencolor setpos setx setxy sety while program : command  program : program command  command : forward NUMBER \n                    | fd NUMBER \n                    | forward \':\' VAR\n                    | fd \':\' VAR  command : right NUMBER \n                    | rt NUMBER\n                    | right \':\' VAR\n                    | rt \':\' VAR  command : back NUMBER \n                    | bk NUMBER\n                    | back \':\' VAR\n                    | bk \':\' VAR  command : left NUMBER \n                    | lt NUMBER\n                    | left \':\' VAR\n                    | lt \':\' VAR  command : setpos \'[\' NUMBER NUMBER \']\'\n                    | setxy NUMBER NUMBER\n                    | setpos \'[\' \':\' VAR NUMBER \']\'\n                    | setpos \'[\' NUMBER \':\' VAR \']\'\n                    | setpos \'[\' \':\' VAR \':\' VAR \']\'\n                    | setxy \':\' VAR NUMBER\n                    | setxy NUMBER \':\' VAR\n                    | setxy \':\' VAR \':\' VAR  command : setx NUMBER \n                    | setx \':\' VAR command : sety NUMBER\n                    | sety \':\' VAR  command : home  command : pendown\n                    | pd  command : penup\n                    | pu  command : setpencolor \'[\' NUMBER NUMBER NUMBER \']\'\n                    | setpencolor \'[\' NUMBER NUMBER \':\' VAR \']\'\n                    | setpencolor \'[\' NUMBER \':\' VAR NUMBER \']\'\n                    | setpencolor \'[\' NUMBER \':\' VAR \':\' VAR \']\'\n                    | setpencolor \'[\' \':\' VAR NUMBER NUMBER \']\' \n                    | setpencolor \'[\' \':\' VAR NUMBER \':\' VAR \']\'\n                    | setpencolor \'[\' \':\' VAR \':\' VAR NUMBER \']\'\n                    | setpencolor \'[\' \':\' VAR \':\' VAR \':\' VAR \']\'  command : make \'"\' VAR NUMBER\n                    | make \'"\' VAR \':\' VAR OPERATOR NUMBER\n                    | make \'"\' VAR NUMBER OPERATOR \':\' VAR  command : repeat NUMBER \'[\' program \']\' \n                    | repeat \':\' VAR \'[\' program \']\'  command : while \'[\' \':\' VAR SIGN NUMBER \']\' \'[\' program \']\'  command : if NUMBER SIGN NUMBER \'[\' program \']\'\n                    | if \':\' VAR SIGN NUMBER \'[\' program \']\'\n                    | if  NUMBER SIGN \':\' VAR \'[\' program \']\'\n                    | if \':\' VAR SIGN \':\' VAR \'[\' program \']\'\n                    | if \'[\' NUMBER SIGN NUMBER \']\' \'[\' program \']\'\n                    | if \'[\' \':\' VAR SIGN NUMBER \']\' \'[\' program \']\'\n                    | if \'[\' NUMBER SIGN \':\' VAR \']\' \'[\' program \']\'\n                    | if \'[\' \':\' VAR SIGN \':\' VAR \']\' \'[\' program \']\'  command : ifelse NUMBER SIGN NUMBER \'[\' program \']\' \'[\' program \']\'\n                    | ifelse \':\' VAR SIGN NUMBER \'[\' program \']\' \'[\' program \']\'\n                    | ifelse NUMBER SIGN \':\' VAR \'[\' program \']\' \'[\' program \']\'\n                    | ifelse \':\' VAR SIGN \':\' VAR \'[\' program \']\' \'[\' program \']\'\n                    | ifelse \'[\' NUMBER SIGN NUMBER \']\' \'[\' program \']\' \'[\' program \']\'\n                    | ifelse \'[\' \':\' VAR SIGN NUMBER \']\' \'[\' program \']\' \'[\' program \']\'\n                    | ifelse \'[\' NUMBER SIGN \':\' VAR \']\' \'[\' program \']\' \'[\' program \']\'\n                    | ifelse \'[\' \':\' VAR SIGN \':\' VAR \']\' \'[\' program \']\' \'[\' program \']\'  command : TO STR \':\' VAR \'[\' program \']\' END  command : STR \':\' VAR '
    
_lr_action_items = {'forward':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[3,3,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,3,-67,-25,-24,-44,3,3,-19,-26,-47,3,3,3,3,-22,-21,-36,-48,3,3,3,3,3,3,3,-23,-37,-38,-40,-46,-45,-50,3,3,3,3,3,3,3,3,-39,-42,-41,3,-52,3,3,3,3,-51,3,3,3,3,3,-66,-43,3,-54,3,3,3,-53,3,3,3,3,3,3,-49,-56,3,-55,-58,3,3,3,3,3,-57,-60,3,3,3,3,-59,-62,3,3,3,-61,-64,3,-63,-65,]),'fd':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[4,4,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,4,-67,-25,-24,-44,4,4,-19,-26,-47,4,4,4,4,-22,-21,-36,-48,4,4,4,4,4,4,4,-23,-37,-38,-40,-46,-45,-50,4,4,4,4,4,4,4,4,-39,-42,-41,4,-52,4,4,4,4,-51,4,4,4,4,4,-66,-43,4,-54,4,4,4,-53,4,4,4,4,4,4,-49,-56,4,-55,-58,4,4,4,4,4,-57,-60,4,4,4,4,-59,-62,4,4,4,-61,-64,4,-63,-65,]),'right':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[5,5,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,5,-67,-25,-24,-44,5,5,-19,-26,-47,5,5,5,5,-22,-21,-36,-48,5,5,5,5,5,5,5,-23,-37,-38,-40,-46,-45,-50,5,5,5,5,5,5,5,5,-39,-42,-41,5,-52,5,5,5,5,-51,5,5,5,5,5,-66,-43,5,-54,5,5,5,-53,5,5,5,5,5,5,-49,-56,5,-55,-58,5,5,5,5,5,-57,-60,5,5,5,5,-59,-62,5,5,5,-61,-64,5,-63,-65,]),'rt':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[6,6,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,6,-67,-25,-24,-44,6,6,-19,-26,-47,6,6,6,6,-22,-21,-36,-48,6,6,6,6,6,6,6,-23,-37,-38,-40,-46,-45,-50,6,6,6,6,6,6,6,6,-39,-42,-41,6,-52,6,6,6,6,-51,6,6,6,6,6,-66,-43,6,-54,6,6,6,-53,6,6,6,6,6,6,-49,-56,6,-55,-58,6,6,6,6,6,-57,-60,6,6,6,6,-59,-62,6,6,6,-61,-64,6,-63,-65,]),'back':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[7,7,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,7,-67,-25,-24,-44,7,7,-19,-26,-47,7,7,7,7,-22,-21,-36,-48,7,7,7,7,7,7,7,-23,-37,-38,-40,-46,-45,-50,7,7,7,7,7,7,7,7,-39,-42,-41,7,-52,7,7,7,7,-51,7,7,7,7,7,-66,-43,7,-54,7,7,7,-53,7,7,7,7,7,7,-49,-56,7,-55,-58,7,7,7,7,7,-57,-60,7,7,7,7,-59,-62,7,7,7,-61,-64,7,-63,-65,]),'bk':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[8,8,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,8,-67,-25,-24,-44,8,8,-19,-26,-47,8,8,8,8,-22,-21,-36,-48,8,8,8,8,8,8,8,-23,-37,-38,-40,-46,-45,-50,8,8,8,8,8,8,8,8,-39,-42,-41,8,-52,8,8,8,8,-51,8,8,8,8,8,-66,-43,8,-54,8,8,8,-53,8,8,8,8,8,8,-49,-56,8,-55,-58,8,8,8,8,8,-57,-60,8,8,8,8,-59,-62,8,8,8,-61,-64,8,-63,-65,]),'left':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[9,9,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,9,-67,-25,-24,-44,9,9,-19,-26,-47,9,9,9,9,-22,-21,-36,-48,9,9,9,9,9,9,9,-23,-37,-38,-40,-46,-45,-50,9,9,9,9,9,9,9,9,-39,-42,-41,9,-52,9,9,9,9,-51,9,9,9,9,9,-66,-43,9,-54,9,9,9,-53,9,9,9,9,9,9,-49,-56,9,-55,-58,9,9,9,9,9,-57,-60,9,9,9,9,-59,-62,9,9,9,-61,-64,9,-63,-65,]),'lt':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[10,10,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,10,-67,-25,-24,-44,10,10,-19,-26,-47,10,10,10,10,-22,-21,-36,-48,10,10,10,10,10,10,10,-23,-37,-38,-40,-46,-45,-50,10,10,10,10,10,10,10,10,-39,-42,-41,10,-52,10,10,10,10,-51,10,10,10,10,10,-66,-43,10,-54,10,10,10,-53,10,10,10,10,10,10,-49,-56,10,-55,-58,10,10,10,10,10,-57,-60,10,10,10,10,-59,-62,10,10,10,-61,-64,10,-63,-65,]),'setpos':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[11,11,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,11,-67,-25,-24,-44,11,11,-19,-26,-47,11,11,11,11,-22,-21,-36,-48,11,11,11,11,11,11,11,-23,-37,-38,-40,-46,-45,-50,11,11,11,11,11,11,11,11,-39,-42,-41,11,-52,11,11,11,11,-51,11,11,11,11,11,-66,-43,11,-54,11,11,11,-53,11,11,11,11,11,11,-49,-56,11,-55,-58,11,11,11,11,11,-57,-60,11,11,11,11,-59,-62,11,11,11,-61,-64,11,-63,-65,]),'setxy':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[12,12,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,12,-67,-25,-24,-44,12,12,-19,-26,-47,12,12,12,12,-22,-21,-36,-48,12,12,12,12,12,12,12,-23,-37,-38,-40,-46,-45,-50,12,12,12,12,12,12,12,12,-39,-42,-41,12,-52,12,12,12,12,-51,12,12,12,12,12,-66,-43,12,-54,12,12,12,-53,12,12,12,12,12,12,-49,-56,12,-55,-58,12,12,12,12,12,-57,-60,12,12,12,12,-59,-62,12,12,12,-61,-64,12,-63,-65,]),'setx':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[13,13,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,13,-67,-25,-24,-44,13,13,-19,-26,-47,13,13,13,13,-22,-21,-36,-48,13,13,13,13,13,13,13,-23,-37,-38,-40,-46,-45,-50,13,13,13,13,13,13,13,13,-39,-42,-41,13,-52,13,13,13,13,-51,13,13,13,13,13,-66,-43,13,-54,13,13,13,-53,13,13,13,13,13,13,-49,-56,13,-55,-58,13,13,13,13,13,-57,-60,13,13,13,13,-59,-62,13,13,13,-61,-64,13,-63,-65,]),'sety':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[14,14,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,14,-67,-25,-24,-44,14,14,-19,-26,-47,14,14,14,14,-22,-21,-36,-48,14,14,14,14,14,14,14,-23,-37,-38,-40,-46,-45,-50,14,14,14,14,14,14,14,14,-39,-42,-41,14,-52,14,14,14,14,-51,14,14,14,14,14,-66,-43,14,-54,14,14,14,-53,14,14,14,14,14,14,-49,-56,14,-55,-58,14,14,14,14,14,-57,-60,14,14,14,14,-59,-62,14,14,14,-61,-64,14,-63,-65,]),'home':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[15,15,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,15,-67,-25,-24,-44,15,15,-19,-26,-47,15,15,15,15,-22,-21,-36,-48,15,15,15,15,15,15,15,-23,-37,-38,-40,-46,-45,-50,15,15,15,15,15,15,15,15,-39,-42,-41,15,-52,15,15,15,15,-51,15,15,15,15,15,-66,-43,15,-54,15,15,15,-53,15,15,15,15,15,15,-49,-56,15,-55,-58,15,15,15,15,15,-57,-60,15,15,15,15,-59,-62,15,15,15,-61,-64,15,-63,-65,]),'pendown':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[16,16,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,16,-67,-25,-24,-44,16,16,-19,-26,-47,16,16,16,16,-22,-21,-36,-48,16,16,16,16,16,16,16,-23,-37,-38,-40,-46,-45,-50,16,16,16,16,16,16,16,16,-39,-42,-41,16,-52,16,16,16,16,-51,16,16,16,16,16,-66,-43,16,-54,16,16,16,-53,16,16,16,16,16,16,-49,-56,16,-55,-58,16,16,16,16,16,-57,-60,16,16,16,16,-59,-62,16,16,16,-61,-64,16,-63,-65,]),'pd':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[17,17,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,17,-67,-25,-24,-44,17,17,-19,-26,-47,17,17,17,17,-22,-21,-36,-48,17,17,17,17,17,17,17,-23,-37,-38,-40,-46,-45,-50,17,17,17,17,17,17,17,17,-39,-42,-41,17,-52,17,17,17,17,-51,17,17,17,17,17,-66,-43,17,-54,17,17,17,-53,17,17,17,17,17,17,-49,-56,17,-55,-58,17,17,17,17,17,-57,-60,17,17,17,17,-59,-62,17,17,17,-61,-64,17,-63,-65,]),'penup':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[18,18,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,18,-67,-25,-24,-44,18,18,-19,-26,-47,18,18,18,18,-22,-21,-36,-48,18,18,18,18,18,18,18,-23,-37,-38,-40,-46,-45,-50,18,18,18,18,18,18,18,18,-39,-42,-41,18,-52,18,18,18,18,-51,18,18,18,18,18,-66,-43,18,-54,18,18,18,-53,18,18,18,18,18,18,-49,-56,18,-55,-58,18,18,18,18,18,-57,-60,18,18,18,18,-59,-62,18,18,18,-61,-64,18,-63,-65,]),'pu':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[19,19,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,19,-67,-25,-24,-44,19,19,-19,-26,-47,19,19,19,19,-22,-21,-36,-48,19,19,19,19,19,19,19,-23,-37,-38,-40,-46,-45,-50,19,19,19,19,19,19,19,19,-39,-42,-41,19,-52,19,19,19,19,-51,19,19,19,19,19,-66,-43,19,-54,19,19,19,-53,19,19,19,19,19,19,-49,-56,19,-55,-58,19,19,19,19,19,-57,-60,19,19,19,19,-59,-62,19,19,19,-61,-64,19,-63,-65,]),'setpencolor':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[20,20,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,20,-67,-25,-24,-44,20,20,-19,-26,-47,20,20,20,20,-22,-21,-36,-48,20,20,20,20,20,20,20,-23,-37,-38,-40,-46,-45,-50,20,20,20,20,20,20,20,20,-39,-42,-41,20,-52,20,20,20,20,-51,20,20,20,20,20,-66,-43,20,-54,20,20,20,-53,20,20,20,20,20,20,-49,-56,20,-55,-58,20,20,20,20,20,-57,-60,20,20,20,20,-59,-62,20,20,20,-61,-64,20,-63,-65,]),'make':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[21,21,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,21,-67,-25,-24,-44,21,21,-19,-26,-47,21,21,21,21,-22,-21,-36,-48,21,21,21,21,21,21,21,-23,-37,-38,-40,-46,-45,-50,21,21,21,21,21,21,21,21,-39,-42,-41,21,-52,21,21,21,21,-51,21,21,21,21,21,-66,-43,21,-54,21,21,21,-53,21,21,21,21,21,21,-49,-56,21,-55,-58,21,21,21,21,21,-57,-60,21,21,21,21,-59,-62,21,21,21,-61,-64,21,-63,-65,]),'repeat':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[22,22,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,22,-67,-25,-24,-44,22,22,-19,-26,-47,22,22,22,22,-22,-21,-36,-48,22,22,22,22,22,22,22,-23,-37,-38,-40,-46,-45,-50,22,22,22,22,22,22,22,22,-39,-42,-41,22,-52,22,22,22,22,-51,22,22,22,22,22,-66,-43,22,-54,22,22,22,-53,22,22,22,22,22,22,-49,-56,22,-55,-58,22,22,22,22,22,-57,-60,22,22,22,22,-59,-62,22,22,22,-61,-64,22,-63,-65,]),'while':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[23,23,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,23,-67,-25,-24,-44,23,23,-19,-26,-47,23,23,23,23,-22,-21,-36,-48,23,23,23,23,23,23,23,-23,-37,-38,-40,-46,-45,-50,23,23,23,23,23,23,23,23,-39,-42,-41,23,-52,23,23,23,23,-51,23,23,23,23,23,-66,-43,23,-54,23,23,23,-53,23,23,23,23,23,23,-49,-56,23,-55,-58,23,23,23,23,23,-57,-60,23,23,23,23,-59,-62,23,23,23,-61,-64,23,-63,-65,]),'if':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[24,24,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,24,-67,-25,-24,-44,24,24,-19,-26,-47,24,24,24,24,-22,-21,-36,-48,24,24,24,24,24,24,24,-23,-37,-38,-40,-46,-45,-50,24,24,24,24,24,24,24,24,-39,-42,-41,24,-52,24,24,24,24,-51,24,24,24,24,24,-66,-43,24,-54,24,24,24,-53,24,24,24,24,24,24,-49,-56,24,-55,-58,24,24,24,24,24,-57,-60,24,24,24,24,-59,-62,24,24,24,-61,-64,24,-63,-65,]),'ifelse':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[25,25,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,25,-67,-25,-24,-44,25,25,-19,-26,-47,25,25,25,25,-22,-21,-36,-48,25,25,25,25,25,25,25,-23,-37,-38,-40,-46,-45,-50,25,25,25,25,25,25,25,25,-39,-42,-41,25,-52,25,25,25,25,-51,25,25,25,25,25,-66,-43,25,-54,25,25,25,-53,25,25,25,25,25,25,-49,-56,25,-55,-58,25,25,25,25,25,-57,-60,25,25,25,25,-59,-62,25,25,25,-61,-64,25,-63,-65,]),'TO':([0,1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[26,26,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,26,-67,-25,-24,-44,26,26,-19,-26,-47,26,26,26,26,-22,-21,-36,-48,26,26,26,26,26,26,26,-23,-37,-38,-40,-46,-45,-50,26,26,26,26,26,26,26,26,-39,-42,-41,26,-52,26,26,26,26,-51,26,26,26,26,26,-66,-43,26,-54,26,26,26,-53,26,26,26,26,26,26,-49,-56,26,-55,-58,26,26,26,26,26,-57,-60,26,26,26,26,-59,-62,26,26,26,-61,-64,26,-63,-65,]),'STR':([0,1,2,15,16,17,18,19,26,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,83,95,99,101,105,107,108,121,125,133,134,136,143,150,151,153,154,163,165,166,172,173,174,180,181,182,183,184,189,190,191,193,194,195,199,200,202,203,207,208,210,212,213,214,215,216,217,219,220,221,222,224,225,227,228,230,231,232,233,234,235,236,237,238,239,241,242,243,245,246,247,248,249,250,251,252,254,256,257,258,259,260,261,263,264,265,266,267,268,269,270,271,272,273,274,],[27,27,-1,-31,-32,-33,-34,-35,63,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,27,-67,-25,-24,-44,27,27,-19,-26,-47,27,27,27,27,-22,-21,-36,-48,27,27,27,27,27,27,27,-23,-37,-38,-40,-46,-45,-50,27,27,27,27,27,27,27,27,-39,-42,-41,27,-52,27,27,27,27,-51,27,27,27,27,27,-66,-43,27,-54,27,27,27,-53,27,27,27,27,27,27,-49,-56,27,-55,-58,27,27,27,27,27,-57,-60,27,27,27,27,-59,-62,27,27,27,-61,-64,27,-63,-65,]),'$end':([1,2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,95,99,101,105,121,125,133,151,153,154,163,182,183,184,189,190,191,193,210,212,213,215,221,230,231,233,237,246,247,249,250,258,259,265,266,270,271,273,274,],[0,-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,-67,-25,-24,-44,-19,-26,-47,-22,-21,-36,-48,-23,-37,-38,-40,-46,-45,-50,-39,-42,-41,-52,-51,-66,-43,-54,-53,-49,-56,-55,-58,-57,-60,-59,-62,-61,-64,-63,-65,]),']':([2,15,16,17,18,19,28,29,31,33,35,37,39,41,43,48,50,65,66,67,68,69,70,71,72,75,78,79,95,96,99,101,105,107,121,122,124,125,126,133,134,138,145,151,152,153,154,155,156,160,163,164,165,168,170,173,176,178,181,182,183,184,185,187,188,189,190,191,193,194,197,200,202,205,208,210,211,212,213,215,216,220,221,224,228,230,231,232,233,234,236,237,238,241,243,246,247,248,249,250,251,254,257,258,259,260,264,265,266,267,269,270,271,272,273,274,],[-1,-31,-32,-33,-34,-35,-2,-3,-4,-7,-8,-11,-12,-15,-16,-27,-29,-5,-6,-9,-10,-13,-14,-17,-18,-20,-28,-30,-67,121,-25,-24,-44,133,-19,151,153,-26,154,-47,163,167,175,-22,182,-21,-36,183,184,189,-48,192,193,196,198,201,204,206,209,-23,-37,-38,210,212,213,-40,-46,-45,-50,215,218,221,223,226,229,-39,231,-42,-41,-52,233,237,-51,240,244,-66,-43,246,-54,247,249,-53,250,253,255,-49,-56,258,-55,-58,259,262,265,-57,-60,266,270,-59,-62,271,273,-61,-64,274,-63,-65,]),'NUMBER':([3,4,5,6,7,8,9,10,12,13,14,22,24,25,45,46,52,58,61,73,77,80,82,86,90,98,102,104,112,114,117,119,128,130,135,140,147,158,162,],[29,31,33,35,37,39,41,43,46,48,50,54,57,60,73,75,80,87,91,96,101,102,105,110,115,124,126,130,138,142,145,149,156,160,164,170,178,187,191,]),':':([3,4,5,6,7,8,9,10,12,13,14,22,24,25,27,45,46,52,56,58,61,63,73,77,80,82,86,90,98,102,104,112,114,117,119,128,130,131,140,147,158,],[30,32,34,36,38,40,42,44,47,49,51,55,59,62,64,74,76,81,85,88,92,94,97,100,103,106,111,116,123,127,129,139,141,146,148,157,159,161,169,177,186,]),'[':([11,20,23,24,25,54,84,110,115,120,137,142,144,149,167,171,175,179,192,196,198,201,204,206,218,223,226,229,240,244,253,255,262,],[45,52,56,58,61,83,108,136,143,150,166,172,174,180,195,199,203,207,214,217,219,222,225,227,235,239,242,245,252,256,261,263,268,]),'"':([21,],[53,]),'VAR':([30,32,34,36,38,40,42,44,47,49,51,53,55,59,62,64,74,76,81,85,88,92,94,97,100,103,106,111,116,123,127,129,139,141,146,148,157,159,161,169,177,186,],[65,66,67,68,69,70,71,72,77,78,79,82,84,89,93,95,98,99,104,109,113,118,120,122,125,128,132,137,144,152,155,158,168,171,176,179,185,188,190,197,205,211,]),'SIGN':([57,60,87,89,91,93,109,113,118,],[86,90,112,114,117,119,135,140,147,]),'OPERATOR':([105,132,],[131,162,]),'END':([209,],[230,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,83,108,136,143,150,166,172,174,180,195,199,203,207,214,217,219,222,225,227,235,239,242,245,252,256,261,263,268,],[1,107,134,165,173,181,194,200,202,208,216,220,224,228,232,234,236,238,241,243,248,251,254,257,260,264,267,269,272,]),'command':([0,1,83,107,108,134,136,143,150,165,166,172,173,174,180,181,194,195,199,200,202,203,207,208,214,216,217,219,220,222,224,225,227,228,232,234,235,236,238,239,241,242,243,245,248,251,252,254,256,257,260,261,263,264,267,268,269,272,],[2,28,2,28,2,28,2,2,2,28,2,2,28,2,2,28,28,2,2,28,28,2,2,28,2,28,2,2,28,2,28,2,2,28,28,28,2,28,28,2,28,2,28,2,28,28,2,28,2,28,28,2,2,28,28,2,28,28,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> command','program',1,'p_program0','Parser.py',72),
  ('program -> program command','program',2,'p_program1','Parser.py',77),
  ('command -> forward NUMBER','command',2,'p_command0','Parser.py',83),
  ('command -> fd NUMBER','command',2,'p_command0','Parser.py',84),
  ('command -> forward : VAR','command',3,'p_command0','Parser.py',85),
  ('command -> fd : VAR','command',3,'p_command0','Parser.py',86),
  ('command -> right NUMBER','command',2,'p_command1','Parser.py',94),
  ('command -> rt NUMBER','command',2,'p_command1','Parser.py',95),
  ('command -> right : VAR','command',3,'p_command1','Parser.py',96),
  ('command -> rt : VAR','command',3,'p_command1','Parser.py',97),
  ('command -> back NUMBER','command',2,'p_command2','Parser.py',104),
  ('command -> bk NUMBER','command',2,'p_command2','Parser.py',105),
  ('command -> back : VAR','command',3,'p_command2','Parser.py',106),
  ('command -> bk : VAR','command',3,'p_command2','Parser.py',107),
  ('command -> left NUMBER','command',2,'p_command3','Parser.py',115),
  ('command -> lt NUMBER','command',2,'p_command3','Parser.py',116),
  ('command -> left : VAR','command',3,'p_command3','Parser.py',117),
  ('command -> lt : VAR','command',3,'p_command3','Parser.py',118),
  ('command -> setpos [ NUMBER NUMBER ]','command',5,'p_command4','Parser.py',127),
  ('command -> setxy NUMBER NUMBER','command',3,'p_command4','Parser.py',128),
  ('command -> setpos [ : VAR NUMBER ]','command',6,'p_command4','Parser.py',129),
  ('command -> setpos [ NUMBER : VAR ]','command',6,'p_command4','Parser.py',130),
  ('command -> setpos [ : VAR : VAR ]','command',7,'p_command4','Parser.py',131),
  ('command -> setxy : VAR NUMBER','command',4,'p_command4','Parser.py',132),
  ('command -> setxy NUMBER : VAR','command',4,'p_command4','Parser.py',133),
  ('command -> setxy : VAR : VAR','command',5,'p_command4','Parser.py',134),
  ('command -> setx NUMBER','command',2,'p_command5','Parser.py',159),
  ('command -> setx : VAR','command',3,'p_command5','Parser.py',160),
  ('command -> sety NUMBER','command',2,'p_command6','Parser.py',167),
  ('command -> sety : VAR','command',3,'p_command6','Parser.py',168),
  ('command -> home','command',1,'p_command7','Parser.py',175),
  ('command -> pendown','command',1,'p_command8','Parser.py',179),
  ('command -> pd','command',1,'p_command8','Parser.py',180),
  ('command -> penup','command',1,'p_command9','Parser.py',184),
  ('command -> pu','command',1,'p_command9','Parser.py',185),
  ('command -> setpencolor [ NUMBER NUMBER NUMBER ]','command',6,'p_command10','Parser.py',189),
  ('command -> setpencolor [ NUMBER NUMBER : VAR ]','command',7,'p_command10','Parser.py',190),
  ('command -> setpencolor [ NUMBER : VAR NUMBER ]','command',7,'p_command10','Parser.py',191),
  ('command -> setpencolor [ NUMBER : VAR : VAR ]','command',8,'p_command10','Parser.py',192),
  ('command -> setpencolor [ : VAR NUMBER NUMBER ]','command',7,'p_command10','Parser.py',193),
  ('command -> setpencolor [ : VAR NUMBER : VAR ]','command',8,'p_command10','Parser.py',194),
  ('command -> setpencolor [ : VAR : VAR NUMBER ]','command',8,'p_command10','Parser.py',195),
  ('command -> setpencolor [ : VAR : VAR : VAR ]','command',9,'p_command10','Parser.py',196),
  ('command -> make " VAR NUMBER','command',4,'p_command11','Parser.py',226),
  ('command -> make " VAR : VAR OPERATOR NUMBER','command',7,'p_command11','Parser.py',227),
  ('command -> make " VAR NUMBER OPERATOR : VAR','command',7,'p_command11','Parser.py',228),
  ('command -> repeat NUMBER [ program ]','command',5,'p_command12','Parser.py',239),
  ('command -> repeat : VAR [ program ]','command',6,'p_command12','Parser.py',240),
  ('command -> while [ : VAR SIGN NUMBER ] [ program ]','command',10,'p_command13','Parser.py',248),
  ('command -> if NUMBER SIGN NUMBER [ program ]','command',7,'p_command14','Parser.py',254),
  ('command -> if : VAR SIGN NUMBER [ program ]','command',8,'p_command14','Parser.py',255),
  ('command -> if NUMBER SIGN : VAR [ program ]','command',8,'p_command14','Parser.py',256),
  ('command -> if : VAR SIGN : VAR [ program ]','command',9,'p_command14','Parser.py',257),
  ('command -> if [ NUMBER SIGN NUMBER ] [ program ]','command',9,'p_command14','Parser.py',258),
  ('command -> if [ : VAR SIGN NUMBER ] [ program ]','command',10,'p_command14','Parser.py',259),
  ('command -> if [ NUMBER SIGN : VAR ] [ program ]','command',10,'p_command14','Parser.py',260),
  ('command -> if [ : VAR SIGN : VAR ] [ program ]','command',11,'p_command14','Parser.py',261),
  ('command -> ifelse NUMBER SIGN NUMBER [ program ] [ program ]','command',10,'p_command15','Parser.py',284),
  ('command -> ifelse : VAR SIGN NUMBER [ program ] [ program ]','command',11,'p_command15','Parser.py',285),
  ('command -> ifelse NUMBER SIGN : VAR [ program ] [ program ]','command',11,'p_command15','Parser.py',286),
  ('command -> ifelse : VAR SIGN : VAR [ program ] [ program ]','command',12,'p_command15','Parser.py',287),
  ('command -> ifelse [ NUMBER SIGN NUMBER ] [ program ] [ program ]','command',12,'p_command15','Parser.py',288),
  ('command -> ifelse [ : VAR SIGN NUMBER ] [ program ] [ program ]','command',13,'p_command15','Parser.py',289),
  ('command -> ifelse [ NUMBER SIGN : VAR ] [ program ] [ program ]','command',13,'p_command15','Parser.py',290),
  ('command -> ifelse [ : VAR SIGN : VAR ] [ program ] [ program ]','command',14,'p_command15','Parser.py',291),
  ('command -> TO STR : VAR [ program ] END','command',8,'p_command16','Parser.py',315),
  ('command -> STR : VAR','command',3,'p_command17','Parser.py',323),
]
