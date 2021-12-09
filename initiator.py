def initiate(pc_lim):
    li = []
    sw_li = []

    for switch in range(len(pc_lim)):
        li.append('sw'+str(switch))
        sw_li.append('sw'+str(switch))
        # print(li)


    for switch in range(len(pc_lim)):
        temp = []
        for details in range(2):
            temp.append('sw'+str(switch)+'_d'+str(details))
            sw_li[switch] = temp

    for switch in range(len(pc_lim)):
        temp = []
        for pc in range(pc_lim[switch]):
            temp.append('sw'+str(switch)+'pc'+str(pc))
            li[switch] = temp
            # print(li)

    for switch in range(len(pc_lim)):
        for pc in range(pc_lim[switch]):
            temp = []
            for details in range(3):
                temp.append('sw'+str(switch)+'_pc'+str(pc)+'_d'+str(details))
                li[switch][pc] = temp
                # print(li)
