#t=6
while True:
    try:
        n=input('How many digits? (or q to quit): ')
        if n=='q':
            break
        else:
            n=int(n)
        t=6/9*n
        clear_screen()
        a=[]
        for i in range(n):
            a.append(str(randint(10)))
        aa=' '.join(a)
        c=int(''.join(a))
        print(aa)
        cm()
        if False:
            t0=time.time()
            while(time.time()<t0+t):
                for i in range(1000):
                    j=i*6
        clear_screen()
        b=input('answer:')
        #if b=='q':
        #    break
        if c==int(b):
            print('correct!')
        else:
            print('wrong!',c)
    except KeyboardInterrupt:
        clear_screen()
        cr('*** KeyboardInterrupt ***')
        #sys.exit()
    except Exception as e:
        clear_screen()
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print('Exception!')
        print(d2s(exc_type,file_name,exc_tb.tb_lineno)) 