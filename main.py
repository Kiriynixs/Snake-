import tkinter as tk

LIGHT_BLUE= "#7b68ee"
LABEL_COLOR= "#00f7ad"
DEFAULT_FONT_STYLE= ("Arial",20)
OFF_WHITE = "#ff9baa"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(None,None)
        self.window.title("Calculator")
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.create_square_button()
        self.create_sqrt_button()
        self.create_equals_button()
        self.create_clear_button()
        self.total_expression = ""
        self.current_expression = ""
        self.total_label,self.label=self.create_display_labels()
        self.digits = {7:(1,1),8:(1,2),9:(1,3),
                       4:(2,1),5:(2,2),6:(2,3),
                       1:(3,1),2:(3,2),3:(3,3),
                       0:(4,2),".":(4,1)}
        self.operations = {"/":"\u00F7","*":"\u00D7","-": "-","+":"+"}
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.buttons_frame.rowconfigure(0,weight=1)
        for x in range (1,5):
            self.buttons_frame.rowconfigure(x,weight=1)
            self.buttons_frame.columnconfigure(x,weight=1)

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)
    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame,text="\u221ax", bg= LIGHT_BLUE, fg= LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)


    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=OFF_WHITE,
                           fg = LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.evalute)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)


    def evalute(self):
        self.total_expression+=self.current_expression
        self.update_total_label()
        try:

            self.current_expression=str(eval(self.total_expression))
            self.total_expression=""
        except ZeroDivisionError:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def add_to_expression(self,value):
        self.current_expression+=str(value)
        self.update_label()

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame,
                               text=str(digit),bg=LIGHT_BLUE,fg="black",
                               font=("Arial",24,"bold"),borderwidth=0,
                               command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0],
                        column=grid_value[1],sticky=tk.NSEW)


    def append_operator(self,operator):
        self.current_expression +=operator
        self.total_expression+=self.current_expression
        self.current_expression=""
        self.update_total_label()
        self.update_label()
    def create_operator_buttons(self):
        i=0
        for operator,symbol in self.operations.items():
            button = tk.Button(self.buttons_frame,
                               text=symbol,bg=LIGHT_BLUE,fg="black",
                               font=("Arial",24,"bold"),
                               borderwidth=0,
                               command=lambda x=operator: self.append_operator(x))
            button.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame,
                               text=self.total_expression, anchor=tk.E,
                               bg="lightgrey", fg="black",
                               padx=24,font=("Arial",16))
        total_label.pack(expand=True,fill="both")
        label = tk.Label(self.display_frame,
                         text=self.current_expression,anchor=tk.E,
                         bg="lightgrey", fg="black",
                         padx=24,font=("Arial",40,"bold"))
        label.pack(expand=True,fill="both")
        return total_label,label

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True,fill="both")
        return frame
    def run(self):
        self.window.mainloop()

    def create_display_frame(self):
        frame = tk.Frame(self.window,height=221, bg="lightgrey")
        frame.pack(expand=True,fill="both")
        return frame

if __name__=="__main__":
    calc = Calculator()
    calc.run()

