def doOverlap(self, L1, R1, L2, R2):
        #code here
        x1range=(L1[0],R1[0])
        y1range=(R1[1],L1[1])
        x2range=(L2[0],R2[0])
        y2range=(R2[1],L2[1])
    #if 1 is contained in 2
        if x1range[0]<=x2range[0] and x1range[1]>=x2range[0]:
            if (y1range[0]<=y2range[0] and y1range[1]>=y2range[0]) or (y1range[0]>=y2range[0] and y1range[0]<=y2range[1]):
                return 1
        if x1range[0]>=x2range[0] and x1range[0]<=x2range[1]:
            if (y1range[0]<=y2range[0] and y1range[1]>=y2range[0]) or (y1range[0]>=y2range[0] and y1range[0]<=y2range[1]):
                return 1
        return 0