import customtkinter

app = customtkinter.CTk()
app.title('dee')
app.geometry("500x500")
#ข้อความแสดงผล
label = customtkinter.CTkLabel(app, text="you want to say?",fg_color="transparent", font=('Wild Youth', 40))
label.pack(pady=(20,0))
#ข้อความแสดงคำตอบ
answer_text = customtkinter.StringVar()
answer_label = customtkinter.CTkLabel(app, textvariable=answer_text, font=('Wild Youth', 40))
answer_label.pack(pady=(20,0))
#กล่องรับค่า input
entry= customtkinter.CTkEntry(app, placeholder_text="ใส่ข้อความตรงนี้เลย")
entry.pack(pady=(15, 0))
#ปุ่มกด
def button_event():
    user_input = entry.get()
    answer = eval(user_input)
    answer_text.set(answer)
    print(user_input,answer)

button = customtkinter.CTkButton(app, text="กด", command=button_event)
button.pack(pady=(20, 0))






app.mainloop()