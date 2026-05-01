class Solution:
    def rectangleArea(self, rectangles):
        MOD = 10**9+7
        xs = sorted(set([x for r in rectangles for x in (r[0], r[2])]))
        xi = {x:i for i,x in enumerate(xs)}
        seg = [0]*(len(xs)*4)
        cnt = [0]*(len(xs)*4)
        
        def update(i,l,r,ql,qr,val):
            if qr<=l or r<=ql: return
            if ql<=l and r<=qr:
                cnt[i]+=val
            else:
                m=(l+r)//2
                update(i*2,l,m,ql,qr,val)
                update(i*2+1,m,r,ql,qr,val)
            seg[i] = xs[r]-xs[l] if cnt[i]>0 else (seg[i*2]+seg[i*2+1] if r-l>1 else 0)
        
        events=[]
        for x1,y1,x2,y2 in rectangles:
            events.append((y1,1,x1,x2))
            events.append((y2,-1,x1,x2))
        events.sort()
        
        res=0
        prev_y=0
        for y,typ,x1,x2 in events:
            res += seg[1]*(y-prev_y)
            update(1,0,len(xs)-1,xi[x1],xi[x2],typ)
            prev_y=y
        
        return res%MOD