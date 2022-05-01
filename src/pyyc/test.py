# temp0 = input()
# temp1 = - input()
# temp2 = temp1 + 2
# print(temp2)

# Module(
#     body=[
#         Assign(
#             targets=[
#                 Name(id='temp0', ctx=Store())
#             ], 
#             value=Call(
#                func=Name(id='input', ctx=Load()), 
#                args=[], 
#                keywords=[]
#             )
#         ), 
#         Assign(
#             targets=[Name(id='temp1', ctx=Store())], 
#             value=UnaryOp(
#                 op=USub(), 
#                 operand=Call(
#                     func=Name(id='input', ctx=Load()), 
#                     args=[], 
#                     keywords=[]
#                 )
#             )
#         ), 
#         Assign(
#             targets=[
#                 Name(id='temp2', ctx=Store())
#             ], 
#             value=BinOp(
#                 left=Name(id='temp1', ctx=Load()), 
#                 op=Add(), 
#                 right=Num(n=2)
#             )
#         ), 
#         Expr(
#             value=Call(
#                 func=Name(id='print', ctx=Load()), 
#                 args=[Name(id='temp2', ctx=Load())], 
#                 keywords=[]
#             )
#         )
#     ]
# )


def basic_test(ctx):
    b = 1+1
    bpf_trace_printk("recieved packet!\n")
    return XDP_DROP

# Module(
#     body=[
#         FunctionDef(
#             name='basic_test', 
#             args=arguments(
#                 args=[
#                     arg(arg='ctx', annotation=None)
#                 ], 
#                 vararg=None, 
#                 kwonlyargs=[], 
#                 kw_defaults=[], 
#                 kwarg=None, 
#                 defaults=[]
#             ), 
#             body=[
#                 Assign(
#                     targets=[Name(id='b', ctx=Store())], 
#                     value=BinOp(
#                         left=Num(n=1), 
#                         op=Add(), 
#                         right=Num(n=1)
#                     )
#                 ), 
#                 Expr(
#                     value=Call(
#                         func=Name(id='bpf_trace_printk', ctx=Load()), 
#                         args=[Str(s='recieved packet!\n')], keywords=[]
#                     )
#                 ), 
#                 Return(
#                     value=Name(id='XDP_DROP', ctx=Load())
#                 )
#             ], 
#             decorator_list=[], 
#             returns=None
#         )
#     ]
# )

