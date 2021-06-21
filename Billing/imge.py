from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk

class bill_app():

	def __init__(self,root):
		self.root = root
		self.root.geometry("1600x900+0+0")
		self.root.title("Billing Software")

		bg = Label(self.root, image = render2).pack()
		frame1 = Frame(self.root,bg="white").place(x=35,y=35,relheight=0.92,relwidth=0.96)

		logout_label = Button(frame1, image = logout_img, bg="white",border=0,command=self.main_destroy).place(x=50,y=50)

		title = Label(frame1, text="Billing System",bg="white", font=("Cooper Black",30,"bold")).place(x=600,y=50)
		time = Label(self.root,text="TIME",bg="white",pady=20).place(x=1400,y=50)

		customer_label = LabelFrame(self.root,text="Customer Details",bg="white",font=("Cooper Black",15),padx=10,pady=20)
		customer_label.place(x=48,y=150)

		bill_num = Label(customer_label,text="Bill Number ",bg="white",font=("Times New Roman",12)).grid(row=0,column=0)
		bill_entry = Entry(customer_label,width=55,bg="white").grid(row=0,column=1)

		Search_img = Button(customer_label, image=search_img,bg="white",border=0).grid(row=0,column=2,padx=20)

		cus_name = Label(customer_label,text="Customer Name ",bg="white",font=("Times New Roman",12)).grid(row=0,column=3)
		cus_entry = Entry(customer_label,width=55,bg="white").grid(row=0,column=4,padx=10)

		cus_contact = Label(customer_label,text="Contact Number ",bg="white",font=("Times New Roman",12)).grid(row=0,column=5,padx=5)
		contact_entry = Entry(customer_label,width=55,bg="white").grid(row=0,column=6,padx=10)

		product_frame = LabelFrame(self.root,text="Products",bg="white",font=("Cooper Black",15))
		product_frame.place(x=48,y=260)

		category = Label(product_frame,text="Select Category ",bg="white",font=("Times New Roman",12)).grid(row=0,column=0,padx=30,sticky="w")

		cat_box = ttk.Combobox(product_frame,width=80)
		cat_box['values'] = ['Monday','Tuesday']
		cat_box.grid(row=1,column=0,padx=30,pady=5)

		sub_category = Label(product_frame,text="Sub Category ",bg="white",font=("Times New Roman",12)).grid(row=2,column=0,padx=30,sticky="w")

		sub_box = ttk.Combobox(product_frame,width=80)
		sub_box['values'] = ['Monday','Tuesday']
		sub_box.grid(row=3,column=0,padx=30,pady=5)

		product = Label(product_frame,text="Products ",bg="white",font=("Times New Roman",12)).grid(row=4,column=0,padx=30,sticky="w")

		product_box = ttk.Combobox(product_frame,width=80)
		product_box['values'] = ['Monday','Tuesday']
		product_box.grid(row=5,column=0,padx=30,pady=5)

		quantity = Label(product_frame,text="Quantity ",bg="white",font=("Times New Roman",12)).grid(row=6,column=0,padx=30,sticky="w")
		quantity_entry = Entry(product_frame,width=85,bg="white").grid(row=7,column=0,padx=30,pady=5,sticky="w")

		Cart_img = Button(product_frame, image=cart_img,bg="white",border=0).grid(row=8,column=0,padx=120,pady=50,sticky="w")
		Remove_img = Button(product_frame, image=remove_img,bg="white",border=0).place(x=270,y=272)
		Clear_img = Button(product_frame, image=clear_img,bg="white",border=0).place(x=400,y=272)

		bill_frame = LabelFrame(self.root,text="Bill Options",bg="white",font=("Cooper Black",15),pady=20)
		bill_frame.place(x=48,y=650)
		Total_img = Button(bill_frame, image=total_img,bg="white",border=0).grid(row=0,column=0,padx=30,pady=15)
		Generate_img = Button(bill_frame, image=generate_img,bg="white",border=0).grid(row=0,column=1,padx=31,pady=15)
		Clear_img = Button(bill_frame, image=clear_img,bg="white",border=0).grid(row=0,column=2,padx=33,pady=15)
		Exit_img = Button(bill_frame, image=exit_img,bg="white",border=0).grid(row=0,column=3,padx=33,pady=15)

		bill_window = LabelFrame(self.root,text="Bill Window",bg="white",font=("Cooper Black",15),height=525,width=920)
		bill_window.place(x=640,y=260)
		address = """
		A303,Shubh Building,
		Chandrangan Swaroop Society,
		Ambegaon Bk.Pune-411046
		"""
		add = Label(bill_window,text=address,bg="white",font=("Times New Roman",12))
		add.place(x=200,y=5)
		customer_name = Label(bill_window,bg="white", text="Customer Name :",font=("Times New Roman",10))
		customer_name.place(x=20,y=110)
		bill_number = Label(bill_window,bg="white", text="Bill Number :",font=("Times New Roman",10))
		bill_number.place(x=20,y=130)
		phone_number = Label(bill_window,bg="white", text="Mobile Number :",font=("Times New Roman",10))
		phone_number.place(x=650,y=110)
		bill_number = Label(bill_window,bg="white", text="Date :",font=("Times New Roman",10))
		bill_number.place(x=650,y=130)











	def main_destroy(self):
		self.root.destroy()




root = Tk()
load2 = Image.open("images/bg.jpg")
load2 = load2.resize((1600,900), Image.ANTIALIAS)
render2 = ImageTk.PhotoImage(load2)

search_img = PhotoImage(file = "images/Search.png")

logout_img = PhotoImage(file = "images/Logout.png")

cart_img = PhotoImage(file = "images/cart.png")
remove_img = PhotoImage(file = "images/Remove.png")
clear_img = PhotoImage(file = "images/Clear.png")
total_img = PhotoImage(file = "images/Total.png")
generate_img = PhotoImage(file = "images/Generate.png")
exit_img = PhotoImage(file = "images/Exit.png")


obj = bill_app(root)

root.mainloop()