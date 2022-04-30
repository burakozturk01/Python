def b_gen(*args):
        if isinstance(args[0], int) and args[0] != 0:
                return b_gen([""], args[0])
        elif isinstance(args[1], int) and args[1] > 0:
                b_list = []
                for b in args[0]:
                        b_list.append(b + "0")
                        b_list.append(b + "1")
                return b_gen(b_list, args[1] - 1)
        else:
                return args[0]
	
print(b_gen(int(12)))
input()
