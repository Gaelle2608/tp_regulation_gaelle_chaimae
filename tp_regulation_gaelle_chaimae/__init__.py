# publisher pour envoyer la commande
self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
 
# constante Kp
self.Kp = 2.0  # tu peux changer plus tard
 
