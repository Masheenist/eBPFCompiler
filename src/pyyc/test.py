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

# a = 3 + 3
def basic_test(ctx):
    # c = -a
    # b = 1 + 2
    # c = bpf_trace_printk("recieved packet!\n", 3)
    # d = False
    # if ( b != c):
    #     d = True
    # else:
    #     d = False
    lambda z : z*2
    z = lambda x, y: (x + y)/ 4
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


# IDEA FOR BPF MAPS - MAYBE MAKE THEM SPECIAL DICTS
# IF WE CATCH AN EXPLICIT "bpf_list()" OR "b_{}", SOMETHING LIKE THAT,
# THEN WE KNOW ITS A BPF MAP
# OTHERWISE, ITS AN EXPLICIT LIST

# BPF MAPS:
#     BPF_TABLE -> analogue is an explictly declared, ephemeral 2d array.
#         so if the code has: [[elem, elem]] its just normal 2d array, but maybe if they say
#         var = [[elem,elem]]_bpf or is maybe declared as a class i.e. var = bpf_table(), then we know
#         to handle as a bpf table.
#         other cases would be handled similarly
#     BPF_HASH -> analogue is an explictly declared, ephemeral dict
#     BPF_ARRAY -> analogue is an explictly declared, ephemeral array
#     BPF_HISTOGRAM -> no analogue
#     BPF_PERF_ARRAY -> no analogue
