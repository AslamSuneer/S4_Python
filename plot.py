import matplotlib.pyplot as plt
import numpy as np
choice=10
while choice!=-1:
  print("1.y=x 2.y=x^2 3.y=2^x 4.y=sinx 5.y=cosx 6.e^x 7.Exit")
  choice=int(input("enter your choice: "))
  if choice==1:
             x=np.linspace(-10,10,400)
             y=x
             plt.xlabel('X')
             plt.ylabel('Y')
             plt.plot(x,y)
             plt.legend(["y=x"],loc="lower right")
             plt.show()
  elif choice==2:
             x=np.linspace(-10,10,400)
             y=x**2
             plt.xlabel('X')
             plt.ylabel('Y')
             plt.plot(x,y)
             plt.legend(["y=x^2"],loc="lower right")
             plt.show()
  elif choice==3:
             x=np.linspace(-2,2,400)
             y=2**x
             plt.xlabel('X')
             plt.ylabel('Y')
             plt.plot(x,y)
             plt.legend(["y=2^x"],loc="lower right")
             plt.show()
  elif choice==4:
             x=np.linspace(-2*np.pi,2*np.pi,400)
             y=np.sin(x)
             plt.xlabel('X')
             plt.ylabel('Y')
             plt.plot(x,y)
             plt.legend(["y=sinx"],loc="lower right")
             plt.show()
  elif choice==5:
             x=np.linspace(-2*np.pi,2*np.pi,400)
             y=np.cos(x)
             plt.xlabel('X')
             plt.ylabel('Y')
             plt.plot(x,y)
             plt.legend(["y=cosx"],loc="lower right")
             plt.show()
  elif choice==6:
             x=np.linspace(-2,2,400)
             y=np.exp(x)
             plt.xlabel('X')
             plt.ylabel('Y')
             plt.plot(x,y)
             plt.legend(["y=e^x"],loc="lower right")
             plt.show()
  elif choice==5:
             print("Invalid choice")
             choice=-1
