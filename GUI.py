from tkinter import *
from tkinter.ttk import Style
from tkinter import messagebox


class Login(Frame):
	global username, password

	username = ("1")
	password = ("1")

	def __init__(self, parent):
		Frame.__init__(self,parent)
		self.parent = parent
		self.initUI()

	def initUI(self):
		global username_guess, password_guess
		self.parent.title("Login")
		self.pack(fill=BOTH, expand=True)
		
		#Creating the username & password entry boxes
		username_text = Label(self, text="Username:")
		username_guess = Entry(self)
		password_text = Label(self, text="Password:")
		password_guess = Entry(self, show="*")

		#attempt to login button
		attempt_login = Button(self,text="Login", command=self.try_login)

		username_text.pack()
		username_guess.pack()
		password_text.pack()
		password_guess.pack()
		attempt_login.pack()

	def try_login(self):
		global newWindow
		print("Trying to login...")
		if (username_guess.get() == username) and (password_guess.get() == password):
			messagebox.showinfo("-- COMPLETE --", "You Have Now Logged In.", icon="info")
			self.parent.withdraw()
			self.newWindow = Toplevel(self.parent)
			app1 = GUI(self.newWindow)
			self.newWindow.resizable(width=FALSE, height=FALSE)
			self.newWindow.geometry("500x270+500+300")

		else:
			messagebox.showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")






class GUI(Frame):
	global OPTIONS_1, OPTIONS_2, OPTIONS_3, Check, KEY

	Check = True

	KEY = []

	OPTIONS_1 = [
	"None",
	"RIGHT",
	"LEFT"
	]

	OPTIONS_2 = [
	"None",
	"Enable",
	"Disable"
	]

	OPTIONS_3 = [
	"None",
	"Enable",
	"Disable"
	]

	def __init__(self, parent):
		Frame.__init__(self,parent)
		self.parent = parent
		self.initUI()

	def initUI(self):
		self.parent.title("Controll Panel")
		self.style = Style()
		self.style.theme_use("default")
		self.frame = Frame(self, relief=RAISED, borderwidth=1)
		self.frame.pack(fill=BOTH, expand=True)
		self.pack(fill=BOTH, expand=True)


		# TAB SET BACKGOUND
		Label1 = Label(self.frame, text="SET BACKGOUND")
		Label1.pack()

		self.variable1 = StringVar(self.frame)
		self.variable1.set(OPTIONS_1[0]) # default value
		Tab1 = OptionMenu(self.frame, self.variable1, *OPTIONS_1)
		Tab1.pack()

		# TAB SET ARM HANDLE
		Label2 = Label(self.frame, text="SET ARM HANDLE")
		Label2.pack()

		self.variable2 = StringVar(self.frame)
		self.variable2.set(OPTIONS_2[0]) # default value
		Tab2 = OptionMenu(self.frame, self.variable2, *OPTIONS_2)
		Tab2.pack()

		# TAB SET MODE CAMERA
		Label3 = Label(self.frame, text="SET MODE CAMERA")
		Label3.pack()

		self.variable3 = StringVar(self.frame)
		self.variable3.set(OPTIONS_3[0]) # default value
		Tab3 = OptionMenu(self.frame, self.variable3, *OPTIONS_3, command=self.OptionMenu_SelectionEvent)
		Tab3.pack()

		closeButton = Button(self, text="Close", command=self.exit)
		closeButton.pack(side=RIGHT, padx=5, pady=5)
		okButton = Button(self, text="OK", command=self.ok)
		okButton.pack(side=RIGHT)


	# DEF
	def exit(self):
		self.quit()

	def ok(self):
		global KEY
		KEY = []
		if self.variable3.get() != "Enable":
			KEY = [self.variable1.get(), self.variable2.get(), self.variable3.get(), "None", "None", "None"]
			print(KEY)
		else:
			if Entry3_1.get().isdigit() == False or Entry3_2_1.get().isdigit() == False or Entry3_2_2.get().isdigit() == False:
				messagebox.showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")
			else:
				KEY = [self.variable1.get(), self.variable2.get(), self.variable3.get(), Entry3_1.get(), Entry3_2_1.get(),Entry3_2_2.get()]
				print(KEY)


	def OptionMenu_SelectionEvent(self, *variable):
		global Check, frame3_1, frame3_2, Entry3_1, Entry3_2_1, Entry3_2_2
		if (self.variable3.get() == "Enable") and Check:
			frame3_1 = Frame(self.frame)
			frame3_1.pack(fill=X)

			# FPS
			Label3_1 = Label(frame3_1, text="FPS")
			Label3_1.pack(side=LEFT, padx=5, pady=5)

			Entry3_1 = Entry(frame3_1)
			Entry3_1.pack(fill=X, padx=5, expand=False)

			# Frame
			frame3_2 = Frame(self.frame)
			frame3_2.pack(fill=X)

			Label3_2_1 = Label(frame3_2, text="Frame")
			Label3_2_1.pack(side=LEFT, padx=5, pady=5)

			Entry3_2_1 = Entry(frame3_2)
			Entry3_2_1.pack(side=LEFT, padx=5, expand=True)

			Label3_2_2 = Label(frame3_2, text="x")
			Label3_2_2.pack(side=LEFT, padx=5, expand=True)

			Entry3_2_2 = Entry(frame3_2)
			Entry3_2_2.pack(side=LEFT, padx=5, expand=True)

			Check = False

		elif (self.variable3.get() != "Enable") and Check:
			pass

		elif (self.variable3.get() == "Enable") and (Check==False):
			pass

		else:
			frame3_1.pack_forget()
			frame3_2.pack_forget()
			Check = True


if __name__ == '__main__':
	root = Tk()
	root.resizable(width=FALSE, height=FALSE)
	root.geometry("200x120+500+300")
	app = Login(root)
	root.mainloop()


	