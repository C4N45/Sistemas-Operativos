import threading
import os


def main():
	print("Hola Mundo")
	
def pid():
	pid = os.getpid()
	print(pid)
	

if __name__ == "__pid__":
	pid()
	
if __name__ == "__main__":
	main()
	

	hilo1 = threading.Thread(target=main)
	hilo2 = threading.Thread(target=pid)
#hilo3 = threading.Thread(target=info)


	hilo1.start()
	hilo2.start()
	
	hilo1.join()
	hilo2.join()
#hilo3.start(3)

#hilo1.join(10)
#hilo2.join(

#print(
