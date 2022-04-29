
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocPRINTleftPLUSNEGASSIGN INPUT INT NAME NEG NEW_LINE PAREN_END PAREN_START PLUS PRINTmodule : statement_liststatement_list : statement_list new_line statementstatement_list : statementstatement_list : statement_list new_linenew_line : NEW_LINEnew_line : new_line NEW_LINEstatement : PRINT expressionstatement : NAME ASSIGN expressionstatement : expressionexpression : expression PLUS expressionexpression : NEG expressionexpression : INTexpression : NAMEexpression : PAREN_START expression PAREN_ENDexpression : INPUT PAREN_START PAREN_END'
    
_lr_action_items = {'NAME':([0,3,4,6,11,16,17,19,23,],[1,12,12,12,12,-5,1,12,-6,]),'INT':([0,3,4,6,11,16,17,19,23,],[2,2,2,2,2,-5,2,2,-6,]),'NEG':([0,3,4,6,11,16,17,19,23,],[3,3,3,3,3,-5,3,3,-6,]),'PAREN_START':([0,3,4,6,9,11,16,17,19,23,],[4,4,4,4,18,4,-5,4,4,-6,]),'PAREN_END':([2,12,13,14,18,21,24,25,],[-12,-13,-11,21,24,-14,-15,-10,]),'PLUS':([1,2,10,12,13,14,15,20,21,24,25,],[-13,-12,19,-13,-11,19,19,19,-14,-15,-10,]),'PRINT':([0,16,17,23,],[6,-5,6,-6,]),'INPUT':([0,3,4,6,11,16,17,19,23,],[9,9,9,9,9,-5,9,9,-6,]),'NEW_LINE':([1,2,7,8,10,12,13,15,16,17,20,21,22,23,24,25,],[-13,-12,-3,16,-9,-13,-11,-7,-5,23,-8,-14,-2,-6,-15,-10,]),'ASSIGN':([1,],[11,]),'$end':([1,2,5,7,8,10,12,13,15,16,17,20,21,22,23,24,25,],[-13,-12,0,-3,-1,-9,-13,-11,-7,-5,-4,-8,-14,-2,-6,-15,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement_list':([0,],[8,]),'new_line':([8,],[17,]),'expression':([0,3,4,6,11,17,19,],[10,13,14,15,20,10,25,]),'statement':([0,17,],[7,22,]),'module':([0,],[5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> module","S'",1,None,None,None),
  ('module -> statement_list','module',1,'p_module_module','compile.py',420),
  ('statement_list -> statement_list new_line statement','statement_list',3,'p_newline_statement','compile.py',423),
  ('statement_list -> statement','statement_list',1,'p_statement_list','compile.py',427),
  ('statement_list -> statement_list new_line','statement_list',2,'p_trailing_new_line','compile.py',430),
  ('new_line -> NEW_LINE','new_line',1,'p_new_line_single','compile.py',433),
  ('new_line -> new_line NEW_LINE','new_line',2,'p_new_line_repeat','compile.py',435),
  ('statement -> PRINT expression','statement',2,'p_print_statement','compile.py',437),
  ('statement -> NAME ASSIGN expression','statement',3,'p_assign_statement','compile.py',440),
  ('statement -> expression','statement',1,'p_disard_statement','compile.py',443),
  ('expression -> expression PLUS expression','expression',3,'p_plus_expression','compile.py',446),
  ('expression -> NEG expression','expression',2,'p_neg_expression','compile.py',449),
  ('expression -> INT','expression',1,'p_int_expression','compile.py',452),
  ('expression -> NAME','expression',1,'p_name_expression','compile.py',455),
  ('expression -> PAREN_START expression PAREN_END','expression',3,'p_paren_expression','compile.py',458),
  ('expression -> INPUT PAREN_START PAREN_END','expression',3,'p_input_expression','compile.py',461),
]
