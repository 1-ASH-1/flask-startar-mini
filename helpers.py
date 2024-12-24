import tinytuya




def connect_devise(devise_id=None,address=None,local_key=None,version=None):
	
	devise = tinytuya.OutletDevice(

		    dev_id=devise_id,

		    address=address,    

		    local_key=local_key, 

		    version=version
	)


	data = devise.status() 
	print('set_status() result %r' % data)



connect_devise(devise_id="bf9d1cf013e1c76fd4fjgc",local_key="7B<b6wEje#(1Q=a3",address="192.168.0.148",version=3.4)