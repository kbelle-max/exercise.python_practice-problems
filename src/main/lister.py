# Created by Leon Hunter at 12:10 PM 12/08/2020
class Lister(object):
    def get_integer_list(self,start, stop, step):
        ''' TODO - Implement solution
        Given 3 integers,
            `start`, `stop`, and `step`
        return a list of all integers
            between `start`,
            incrementing by `step`,
            up to and including `stop`
        '''
        
        ls=[]
        if stop==0:
            ls.append(0)
        else:
            for idx in range(start,stop+1,step):
                ls.append(idx)
        return ls

    def get_even_list(self,start, stop, step):
        ''' TODO - Implement solution
        Given 3 integers,
            `start`, `stop`, and `step`
        return a list of all integers
            between `start`,
            incrementing by `step`,
            up to and including `stop`
            and are divisible by 2
        '''
        int_list=[]
        even_list=[]
        if stop==0:
            even_list.append(0)
    
        else:
            for idx in range(start,stop+1,step):
                int_list.append(idx)
            for i in int_list:
                if i%2==0:
                    even_list.append(i)
        return even_list

    def get_odd_list(self,start, stop, step):
        ''' TODO - Implement solution
        Given 3 integers,
            `start`, `stop`, and `step`
        return a list of all integers
            between `start`,
            incrementing by `step`,
            up to and including `stop`
            and are not divisible by 2
        '''
        int_list=[]
        odd_list=[]

        
        if stop !=0:
            for idx in range(start,stop+1,step):
                int_list.append(idx)
            for i in int_list:
                if i%2!=0:
                    odd_list.append(i)
        return odd_list