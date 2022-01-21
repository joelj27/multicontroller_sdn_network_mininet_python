from mininet.net import Mininet
from mininet.node import CPULimitedHost,OVSKernelSwitch,Controller, RemoteController,OVSSwitch
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel, info
from mininet.node import RemoteController
from mininet.cli import CLI
import time
import subprocess
import random
net = Mininet( switch=OVSKernelSwitch,link=TCLink,  )

data_packet_size=[10,50,100]
data_packet_size=random.choice(data_packet_size)
if data_packet_size==10:
	average_load_of_controller=20
	NO_of_switch=3
	no_of_connetion_to_switch=2
	k=NO_of_switch*no_of_connetion_to_switch
	fg=k/average_load_of_controller
elif data_packet_size==50:
	average_load_of_controller=20
	NO_of_switch=7
	no_of_connetion_to_switch=6
	k=NO_of_switch*no_of_connetion_to_switch
	fg=k/average_load_of_controller
elif data_packet_size==100:
	average_load_of_controller=20
	NO_of_switch=8
	no_of_connetion_to_switch=8
	k=NO_of_switch*no_of_connetion_to_switch
	fg=k/average_load_of_controller

if fg==0:
   fg=1

print("NO 0F CONTROLLER: "+str(fg))
time.sleep(3)
if fg==1:
	c0=net.addController( 'c0',controller=RemoteController, ip="127.0.0.1",port=6633 )

        print"CREATING THE Main Controller**********************"
	print"c0 Main Controller Created"
	time.sleep(3)
	c1 = net.addController( 'c1' )
        print"CREATING THE sub Controller**********************"
	print"c0 sub Controller Created"
	time.sleep(3)
        



	#creating CLIENT
	client1 = net.addHost('client1',bw=10)
	client2 = net.addHost('client2',bw=10)
	client3 = net.addHost('client3',bw=10)
	client4 = net.addHost('client4',bw=10)
	client5 = net.addHost('client5',bw=10)
	client6 = net.addHost('client6',bw=10)
	client7 = net.addHost('client7',bw=10)
	client8 = net.addHost('client8',bw=10)
	client9 = net.addHost('client9',bw=10)
	client10 = net.addHost('client10',bw=10)

	print"CREATING THE CLIENT**********************"
	print"client 1  Created"
	print"client 2  Created"
	print"client 3  Created"
	print"client 4  Created"
	print"client 5  Created"
	print"client 6  Created"
	print"client 7  Created"
	print"client 8  Created"
	print"client 9  Created"
	print"client 10 Created"
	time.sleep(3)


	switch1 = net.addSwitch('switch1',inNamespace=False)
	switch2 = net.addSwitch('switch2',inNamespace=False)
	switch3 = net.addSwitch('switch3',inNamespace=False)

	print"CREATING THE SWITCHES**********************"
	print"switch 1  Created"
	print"switch 2  Created"
	print"switch 3  Created"
	time.sleep(3)


	switch1.linkTo(client1)
	switch1.linkTo(client2)
	switch1.linkTo(client3)
	switch1.linkTo(client4)
	switch1.linkTo(client5)
	switch2.linkTo(client6)
	switch2.linkTo(client7)
	switch2.linkTo(client8)
	switch2.linkTo(client9)
	switch2.linkTo(client10)

	print"CREATING THE lINK**********************"
	time.sleep(3)
	print"CONNECTING CLIENT WITH SWITCHES"
	time.sleep(3)
	print"client1 linked with switch1"
	print"client2 linked with switch1"
	print"client3 linked with switch1"
	print"client4 linked with switch1"
	print"client5 linked with switch1"
	print"client6 linked with switch2"
	print"client7 linked with switch2"
	print"client8 linked with switch2"
	print"client9 linked with switch2"
	print"client10 linked with switch2"
	time.sleep(3)

	switch1.linkTo(switch3)
	switch2.linkTo(switch3) 

	print"CONNECTING SWITCHES WITH SWITCHES"
	time.sleep(3)
	print"switch1 linked with switch3"
	print"switch2 linked with switch3"      
        time.sleep(3)
    
	net.start()
        print"Start main Controller"
	time.sleep(3)
	c0.start()
	time.sleep(3)

        print"Start sub Controller"
	time.sleep(3)
        c1.start()
        switch3.start([c0])
        switch3.start([c1])
	C1,C2,C3,C4,C5,C6,C7,C8,C9,C10 = net.get('client1','client2','client3','client4','client5','client6','client7','client8','client9','client10',)
	print"GETING THE BANDWIDTH OF client1 client2 client3  client4  client5  client6  client7  client8  client9  client10 *****************************"
	time.sleep(3)
	b1,b2=net.iperf( (C1, C2) )
	b2,b3=net.iperf( (C2, C3) )
	b3,b4=net.iperf( (C3, C4) )
	b4,b5=net.iperf( (C4, C5) )
	b5,b6=net.iperf( (C5, C6) )
	b6,b7=net.iperf( (C6, C7) )
	b7,b8=net.iperf( (C7, C8) )
	b8,b9=net.iperf( (C8, C9) )
	b9,b10=net.iperf( (C9, C10) )
	b10,b1=net.iperf( (C10, C1) )
	time.sleep(3)
        print"bandwidth of client1"
        print(b1)
        print"bandwidth of client1"
        print(b2)
        print"bandwidth of client2"
        print(b3)
        print"bandwidth of client3"
        print(b4)
        print"bandwidth of client4"
        print(b5)
        print"bandwidth of client5"
        print(b6)
        print"bandwidth of client6"
        print(b7)
        print"bandwidth of client7"
        print(b8)
        print"bandwidth of client8"
        print(b9)
        print"bandwidth of client9"
        print(b10)
        print"bandwidth of client10"   
	time.sleep(3)     
        print"CHECKING THE PING REACHABILITY**********************"
	time.sleep(3)
        net.pingAll()
        print"TAKING DOWN THE SWITCH 1 DOWN**********************"
	time.sleep(3)
        net.configLinkStatus( 'switch1', 'switch3', 'down')
        net.configLinkStatus( 'switch1', 'client1', 'down')
        net.configLinkStatus( 'switch1', 'client2', 'down')
        net.configLinkStatus( 'switch1', 'client3', 'down')
        net.configLinkStatus( 'switch1', 'client4', 'down')
        net.configLinkStatus( 'switch1', 'client5', 'down')


        print"CHECKING THE PING REACHABILITY**********************"
	CLI(net)
	time.sleep(3)
	net.pingAll()
        l=[]
        k=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]
        for i in k:
            for token in i.split():
		    try:
			l.append(float(token))
		    except ValueError:
			pass
	total=sum(l)


	b_s2=[b6,b7,b8,b9,b10]
    
        

	bl_s2=[]
	for i in b_s2:
		    for token in i.split():
			    try:
				bl_s2.append(float(token))
			    except ValueError:
				pass

	bandwith_switches=[]
	bw_s2=sum(bl_s2)
        round(bw_s2)
        bandwith_switches.append(bw_s2)

        y=[bw_s2]
        y=sum(y)
        y1=1

        packet_inspection=bw_s2/5
        d1=total+bw_s2
        d=d1+packet_inspection

        
        for i in k:
            if i<=d:
                print"detected"
            else:
                pass	     

	minim_band=bandwith_switches.sort()
	minim_band=bandwith_switches[:1]
	print(bw_s2)
	for i in minim_band:
		if i==bw_s2:
		    j='switch2'

	print("switch with minimum bandwith"+j)
	print"CONNECTING CLIENT WITH THE "+j+'.'
	time.sleep(3)

        net.addLink(net.get('switch1'),net.get('switch3'))
	net.configLinkStatus( 'switch1', 'switch3', 'up') 
        net.addLink(net.get('switch2'),net.get('client1'))
        net.configLinkStatus( 'switch1', 'client1', 'up')
        net.addLink(net.get('switch2'),net.get('client2'))
        net.configLinkStatus( 'switch1', 'client2', 'up')
        net.addLink(net.get('switch2'),net.get('client3'))
        net.configLinkStatus( 'switch1', 'client3', 'up')
        net.addLink(net.get('switch2'),net.get('client4'))
        net.configLinkStatus( 'switch1', 'client4', 'up')
        net.addLink(net.get('switch2'),net.get('client5'))
        net.configLinkStatus( 'switch1', 'client5', 'up') 

        print"CHECKING THE PING REACHABILITY**********************"
	time.sleep(3)
	net.pingAll()
	CLI(net)
elif fg==2:
        c0=net.addController( 'c0',controller=RemoteController, ip="127.0.0.1",port=6633 )

        print"CREATING THE Main Controller**********************"
	print"c0 Main Controller Created"
	time.sleep(3)

	c1 = net.addController( 'c1' )
	c2 = net.addController( 'c2' )
        print"CREATING THE sub Controller**********************"
	print"c1 sub Controller Created"
	print"c2 sub Controller Created"
	time.sleep(3)
    
	#creatrng CLIENT
	client1 = net.addHost('client1',bw=10)
	client2 = net.addHost('client2',bw=10)
	client3 = net.addHost('client3',bw=10)
	client4 = net.addHost('client4',bw=10)
	client5 = net.addHost('client5',bw=10)
	client6 = net.addHost('client6',bw=10)
	client7 = net.addHost('client7',bw=10)
	client8 = net.addHost('client8',bw=10)
	client9 = net.addHost('client9',bw=10)
	client10 = net.addHost('client10',bw=10)

	print"CREATING THE CLIENT**********************"
	print"client 1  Created"
	print"client 2  Created"
	print"client 3  Created"
	print"client 4  Created"
	print"client 5  Created"
	print"client 6  Created"
	print"client 7  Created"
	print"client 8  Created"
	print"client 9  Created"
	print"client 10 Created"
	time.sleep(3)

	switch1 = net.addSwitch('switch1',inNamespace=False)
	switch2 = net.addSwitch('switch2',inNamespace=False)
	switch3 = net.addSwitch('switch3',inNamespace=False)
	switch4 = net.addSwitch('switch4',inNamespace=False)
	switch5 = net.addSwitch('switch5',inNamespace=False)
	switch6 = net.addSwitch('switch6',inNamespace=False)
	switch7 = net.addSwitch('switch7',inNamespace=False)

	print"CREATING THE SWITCHES**********************"
	print"switch 1  Created"
	print"switch 2  Created"
	print"switch 3  Created"
	print"switch 4  Created"
	print"switch 5  Created"
	print"switch 6  Created"
	print"switch 7  Created"
	time.sleep(3)

	switch1.linkTo(switch2)
	switch1.linkTo(switch3)

	switch2.linkTo(switch4)
	switch2.linkTo(switch5)
	switch3.linkTo(switch6)
	switch3.linkTo(switch7)

	switch4.linkTo(client1)
	switch4.linkTo(client2)
	switch5.linkTo(client3)
	switch5.linkTo(client4)

	switch6.linkTo(client5)
	switch6.linkTo(client6)
	switch6.linkTo(client7)
	switch7.linkTo(client8)
	switch7.linkTo(client9)
	switch7.linkTo(client10)


	print"CONNECTING CLIENT WITH SWITCHES"
	time.sleep(3)
	print"client1 linked with switch4"
	print"client2 linked with switch4"
	print"client3 linked with switch5"
	print"client4 linked with switch5"
	print"client5 linked with switch6"
	print"client6 linked with switch6"
	print"client7 linked with switch6"
	print"client8 linked with switch7"
	print"client9 linked with switch7"
	print"client10 linked with switch7"
	time.sleep(3)

        net.start()
	#connecting SERVER to the controller
	c0.start()
	c1.start()
	c2.start()
	print"CONNECTING SUB-CONTROLLER WITH SWITCHES"
	time.sleep(3)
	print"SUB-CONTROLLER1 linked with switch4"
	print"SUB-CONTROLLER2 linked with switch4"
	time.sleep(3)

	switch2.start([c1])

	switch3.start([c2])


	C1,C2,C3,C4,C5,C6,C7,C8,C9,C10 = net.get('client1','client2','client3','client4','client5','client6','client7','client8','client9','client10',)
	print"GETING THE BANDWIDTH OF client1 client2 client3  client4  client5  client6  client7  client8  client9  client10 *****************************"
	time.sleep(3)
	b1,b2=net.iperf( (C1, C2) )
	b2,b3=net.iperf( (C2, C3) )
	b3,b4=net.iperf( (C3, C4) )
	b4,b5=net.iperf( (C4, C5) )
	b5,b6=net.iperf( (C5, C6) )
	b6,b7=net.iperf( (C6, C7) )
	b7,b8=net.iperf( (C7, C8) )
	b8,b9=net.iperf( (C8, C9) )
	b9,b10=net.iperf( (C9, C10) )
	b10,b1=net.iperf( (C10, C1) )
	time.sleep(3)
        print"bandwidth of client1"
        print(b1)
        print"bandwidth of client1"
        print(b2)
        print"bandwidth of client2"
        print(b3)
        print"bandwidth of client3"
        print(b4)
        print"bandwidth of client4"
        print(b5)
        print"bandwidth of client5"
        print(b6)
        print"bandwidth of client6"
        print(b7)
        print"bandwidth of client7"
        print(b8)
        print"bandwidth of client8"
        print(b9)
        print"bandwidth of client9"
        print(b10)
        print"bandwidth of client10"  
	time.sleep(3)
        
        print"CHECKING THE PING REACHABILITY**********************"
	time.sleep(3)
	net.pingAll()

        print"TAKING DOWN THE SWITCH 4 DOWN**********************"
	time.sleep(3)
        net.configLinkStatus( 'switch2', 'switch4', 'down') 
        net.configLinkStatus( 'switch4', 'client1', 'down')

        print"CHECKING THE PING REACHABILITY**********************"  
	time.sleep(3)    
	net.pingAll()
	CLI(net)

        l=[]
        k=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]
        for i in k:
            for token in i.split():
		    try:
			l.append(float(token))
		    except ValueError:
			pass
	total=sum(l)


	b_s5=[b3,b4]
	b_s6=[b5,b6,b7]
	b_s7=[b8,b9,b10]
    
        

	bl_s5=[]
	for i in b_s5:
		    for token in i.split():
			    try:
				bl_s5.append(float(token))
			    except ValueError:
				pass
	bl_s6=[]
	for i in b_s6:
		    for token in i.split():
			    try:
				bl_s6.append(float(token))
			    except ValueError:
				pass
	bl_s7=[]
	for i in b_s7:
		    for token in i.split():
			    try:
				bl_s7.append(float(token))
			    except ValueError:
				pass

	bandwith_switches=[]
	bw_s5=sum(bl_s5)
        round(bw_s5)
	bandwith_switches.append(bw_s5)
	bw_s6=sum(bl_s6)
        round(bw_s6)
	bandwith_switches.append(bw_s6)
	bw_s7=sum(bl_s7)
        round(bw_s7)
	bandwith_switches.append(bw_s7)
	     
        y=[bw_s5,bw_s6,bw_s7]
        y=sum(y)
        y1=3
        packet_inspection=y/y1
        d1=total+bw_s5+bw_s6+bw_s7
        d=d1+packet_inspection

        
        for i in k:
            if i<=d:
                print"detected"
            else:
                pass	

	minim_band=bandwith_switches.sort()
	minim_band=bandwith_switches[:1]

	time.sleep(3)
        print"bandwidth of switch5"
	print(bw_s5)
        print"bandwidth of switch6"
	print(bw_s6)
        print"bandwidth of switch7"
	print(bw_s7)


	for i in minim_band:
		if i==bw_s5:
		      j='switch5'
		elif i==bw_s6:
		      j='switch6'
		elif i==bw_s7:
		      j='switch7'
	time.sleep(3)
	print("switch with minimum bandwith"+j)
       


	time.sleep(3)
	print"CONNECTING CLIENT WITH THE "+j+'.'

        net.addLink(net.get('switch2'),net.get('switch4'),bw=43)
	net.configLinkStatus( 'switch2', 'switch4', 'up') 
        net.addLink(net.get(j),net.get('client1'),bw=43)
	net.configLinkStatus( 'switch4', 'client1', 'up') 



	time.sleep(3)
        print"CHECKING THE PING REACHABILITY**********************" 
        net.pingAll()

	CLI(net)
elif fg==3:
        c0=net.addController( 'c0',controller=RemoteController, ip="127.0.0.1",port=6633 )
	time.sleep(3)
        print"CREATING THE Main Controller**********************"
	print"c0 Main Controller Created"

	c1 = net.addController( 'c1' )
	c2 = net.addController( 'c2' )
	c3 = net.addController( 'c3' )
	time.sleep(3)
        print"CREATING THE sub Controller**********************"
	print"c1 sub Controller Created"
	print"c2 sub Controller Created"
	print"c3 sub Controller Created"

	#creating CLIENT
	client1 = net.addHost('client1',bw=10)
	client2 = net.addHost('client2',bw=10)
	client3 = net.addHost('client3',bw=10)
	client4 = net.addHost('client4',bw=10)
	client5 = net.addHost('client5',bw=10)
	client6 = net.addHost('client6',bw=10)
	client7 = net.addHost('client7',bw=10)
	client8 = net.addHost('client8',bw=10)
	client9 = net.addHost('client9',bw=10)
	client10 = net.addHost('client10',bw=10)

	print"CREATING THE CLIENT**********************"
	print"client 1  Created"
	print"client 2  Created"
	print"client 3  Created"
	print"client 4  Created"
	print"client 5  Created"
	print"client 6  Created"
	print"client 7  Created"
	print"client 8  Created"
	print"client 9  Created"
	print"client 10 Created"
	time.sleep(3)

	switch1 = net.addSwitch('switch1',inNamespace=False)
	switch2 = net.addSwitch('switch2',inNamespace=False)
	switch3 = net.addSwitch('switch3',inNamespace=False)
	switch4 = net.addSwitch('switch4',inNamespace=False)
	switch5 = net.addSwitch('switch5',inNamespace=False)
	switch6 = net.addSwitch('switch6',inNamespace=False)
	switch7 = net.addSwitch('switch7',inNamespace=False)
	switch8 = net.addSwitch('switch8',inNamespace=False)

	print"CREATING THE SWITCHES**********************"
	print"switch 1  Created"
	print"switch 2  Created"
	print"switch 3  Created"
	print"switch 4  Created"
	print"switch 5  Created"
	print"switch 6  Created"
	print"switch 7  Created"
	print"switch 8  Created"
	time.sleep(3)

	switch1.linkTo(switch2)
	switch1.linkTo(switch3)
	switch1.linkTo(switch4)

	switch2.linkTo(switch5)
	switch2.linkTo(switch6)
	switch3.linkTo(switch7)
	switch4.linkTo(switch8)


	switch5.linkTo(client1)
	switch5.linkTo(client2)
	switch6.linkTo(client3)
	switch6.linkTo(client4)

	switch7.linkTo(client5)
	switch7.linkTo(client6)
	switch7.linkTo(client7)
	switch8.linkTo(client8)
	switch8.linkTo(client9)
	switch8.linkTo(client10)

	print"CONNECTING CLIENT WITH SWITCHES"
	time.sleep(3)
	print"client1 linked with switch5"
	print"client2 linked with switch5"
	print"client3 linked with switch6"
	print"client4 linked with switch6"
	print"client5 linked with switch7"
	print"client6 linked with switch7"
	print"client7 linked with switch7"
	print"client8 linked with switch8"
	print"client9 linked with switch8"
	print"client10 linked with switch8"
	time.sleep(3)
        net.start()
	#connecting SERVER to the controller
	c0.start()
	c1.start()
	c2.start()
	c3.start()
	time.sleep(3)
	switch2.start([c1])
	print"SUB-CONTROLLER1 linked with switch2"
	time.sleep(3)
	switch3.start([c2])
	print"SUB-CONTROLLER2 linked with switch3"
	time.sleep(3)
	switch4.start([c3])
	print"SUB-CONTROLLER3 linked with switch4"

	C1,C2,C3,C4,C5,C6,C7,C8,C9,C10 = net.get('client1','client2','client3','client4','client5','client6','client7','client8','client9','client10',)
	print"GETING THE BANDWIDTH OF client1 client2 client3  client4  client5  client6  client7  client8  client9  client10 *****************************"
	time.sleep(3)
	b1,b2=net.iperf( (C1, C2) )
	b2,b3=net.iperf( (C2, C3) )
	b3,b4=net.iperf( (C3, C4) )
	b4,b5=net.iperf( (C4, C5) )
	b5,b6=net.iperf( (C5, C6) )
	b6,b7=net.iperf( (C6, C7) )
	b7,b8=net.iperf( (C7, C8) )
	b8,b9=net.iperf( (C8, C9) )
	b9,b10=net.iperf( (C9, C10) )
	b10,b1=net.iperf( (C10, C1) )
	time.sleep(3)
        print"bandwidth of client1"
        print(b1)
        print"bandwidth of client1"
        print(b2)
        print"bandwidth of client2"
        print(b3)
        print"bandwidth of client3"
        print(b4)
        print"bandwidth of client4"
        print(b5)
        print"bandwidth of client5"
        print(b6)
        print"bandwidth of client6"
        print(b7)
        print"bandwidth of client7"
        print(b8)
        print"bandwidth of client8"
        print(b9)
        print"bandwidth of client9"
        print(b10)
        print"bandwidth of client10" 
	time.sleep(3)
        print"CHECKING THE PING REACHABILITY**********************"
	time.sleep(3)
	net.pingAll()

        print"TAKING DOWN THE SWITCH 4 DOWN**********************"
	time.sleep(3)
        net.configLinkStatus( 'switch2', 'switch5', 'down') 
        net.configLinkStatus( 'switch5', 'client1', 'down')

        print"CHECKING THE PING REACHABILITY**********************"
	time.sleep(3)
	net.pingAll()
	CLI(net)
        l=[]

        k=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]
        for i in k:
            for token in i.split():
		    try:
			# if this succeeds, you have your (first) float
			l.append(float(token))
		    except ValueError:
			pass
	total=sum(l)
        d=total
        for i in k:
            if i<=d:
                print"detected"
            else:
                pass

	b_s6=[b3,b4]
	b_s7=[b5,b6,b7]
	b_s8=[b8,b9,b10]

	bl_s6=[]
	for i in b_s6:
		    for token in i.split():
			    try:
				bl_s6.append(float(token))
			    except ValueError:
				pass
	bl_s7=[]
	for i in b_s7:
		    for token in i.split():
			    try:
				bl_s7.append(float(token))
			    except ValueError:
				pass
	bl_s8=[]
	for i in b_s8:
		    for token in i.split():
			    try:
				bl_s8.append(float(token))
			    except ValueError:
				pass


	bandwith_switches=[]
	bw_s6=sum(bl_s6)
        round(bw_s6)
	bandwith_switches.append(bw_s6)
	bw_s7=sum(bl_s7)
        round(bw_s7)
	bandwith_switches.append(bw_s7)
	bw_s8=sum(bl_s8)
        round(bw_s8)
	bandwith_switches.append(bw_s8)
	     


        y=[bw_s6,bw_s7,bw_s8]
        y=sum(y)
        y1=3
        packet_inspection=y/y1
        d1=total+bw_s6+bw_s7+bw_s8
        d=d1+packet_inspection

        
        for i in k:
            if i<=d:
                print"detected"
            else:
                pass	

	minim_band=bandwith_switches.sort()
	minim_band=bandwith_switches[:1]
	time.sleep(3)
        print"bandwidth of switch6"
	print(bw_s6)
	time.sleep(3)
        print"bandwidth of switch7"
	print(bw_s7)
	time.sleep(3)
        print"bandwidth of switch8"
	print(bw_s8)

	for i in minim_band:
		if i==bw_s6:
		      j='switch6'
		elif i==bw_s7:
		      j='switch7'
		elif i==bw_s8:
		      j='switch8'
	time.sleep(3)
	print("switch with minimum bandwith="+j)
       
	time.sleep(3)
	print"CONNECTING CLIENT WITH THE "+j+'.'


        net.addLink(net.get('switch2'),net.get('switch5'),bw=43)
	net.configLinkStatus( 'switch2', 'switch5', 'up') 
        net.addLink(net.get(j),net.get('client1'),bw=43)
	net.configLinkStatus( 'switch5', 'client1', 'up') 



	time.sleep(3)
        print"CHECKING THE PING REACHABILITY**********************" 
        net.pingAll()

	CLI(net)


net.stop()
