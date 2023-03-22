import customtkinter
import os
from PIL import Image, ImageTk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



class AddPlant(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("smart_greenhouse.py")
        self.geometry("220x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=15)
        self.grid_columnconfigure(0, weight=15)
        self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"image python")
        self.logo_image = customtkinter.CTkImage(
            Image.open(os.path.join(self.image_path, r"icons8-greenhouse-with-flower-96.png")), size=(40, 40))

        self.frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_rowconfigure(15, weight=1)

        self.frame_label = customtkinter.CTkLabel(self.frame, text="  SMART GREENHOUSE",
                                                  image=self.logo_image,
                                                  compound="left",
                                                  font=customtkinter.CTkFont(size=15, weight="bold"))
        self.frame_label.grid()
        self.label = customtkinter.CTkLabel(self.frame, text="Plant name", justify="center")
        self.label.grid()
        self.entry = customtkinter.CTkEntry(self.frame)
        self.entry.grid()
        self.label_1 = customtkinter.CTkLabel(self.frame, text="Plant temperature", justify="center")
        self.label_1.grid()
        self.entry_1 = customtkinter.CTkEntry(self.frame)
        self.entry_1.grid()
        self.label_2 = customtkinter.CTkLabel(self.frame, text="Plant cooling", justify="center")
        self.label_2.grid()
        self.entry_2 = customtkinter.CTkEntry(self.frame)
        self.entry_2.grid()
        self.label_3 = customtkinter.CTkLabel(self.frame, text="Plant water", justify="center")
        self.label_3.grid()
        self.entry_3 = customtkinter.CTkEntry(self.frame)
        self.entry_3.grid()
        self.label_4 = customtkinter.CTkLabel(self.frame, text="Plant ozon", justify="center")
        self.label_4.grid()
        self.entry_4 = customtkinter.CTkEntry(self.frame)
        self.entry_4.grid()

        self.button = customtkinter.CTkButton(self.frame, text="Add")
        self.button.grid(pady=15)

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.frame,
                                                                values=["System", "Dark", "Light"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(padx=20, pady=20, sticky="s")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("EcoFLat")
        self.geometry("750x550")
        self.array = ['Выберите растение', 'Огурец', 'Помидор','Клубника','Листья Салата']
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        # connect by firebase admin
        self.cred = credentials.Certificate('greenhouse-a121e-firebase-adminsdk-rrjw0-f8cc38e6e9.json')
        # Initialize the app with a service account, granting admin privileges
        firebase_admin.initialize_app(self.cred, {
            'databaseURL': 'https://greenhouse-a121e-default-rtdb.firebaseio.com/'
        })
        # Set default
        self.ref = db.reference('/')
        self.plants = db.reference('/Plants')
       # self.ref.set({
        #   'Plant types': 'None',
       #   'Heating': False,
       # 'Cooling': False,
       #  'Water': False,
      #   'Light': False,
       #     'Temperature': "0",
       #     'Humidity': "0"
       #  })
        # load images with light and dark mode image
        self.images()
        # create navigation frame
        self.navigation_frame_fun()
        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="",image=self.large_test_image)
        self.home_frame_large_image_label.grid()
        self.optionemenu = customtkinter.CTkOptionMenu(self.home_frame,values=self.array)
        self.optionemenu.grid(row=3, column=0, padx=40, pady=(10), sticky="nsew")
        self.optionemenu.set("Выберите растение")
        #self.add_button = customtkinter.CTkButton(self.home_frame, text="+", height=30, width=30)
        #self.add_button.grid(sticky="W",row=3,padx=5)
        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="Нагрев", image=self.icon,
                                                           command=lambda: self.button('Heating'))
        self.home_frame_button_1.grid(row=4,sticky="W",padx=20, pady=10)
        self.temperatureText = customtkinter.CTkLabel(self.home_frame, text="Температура")
        self.temperatureText.grid(row=4, padx=30)
        self.temperature = customtkinter.CTkLabel(self.home_frame, text=self.get_temperature()+"°C")
        self.temperature.grid(sticky="e", row=4,padx=100)
        self.temperature.after(100,self.temperature.configure(text=self.get_temperature()+"°C"))
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Продув", image=self.icon_1,
                                                           command=lambda: self.button('Cooling'))
        self.home_frame_button_2.grid(row=5, sticky="W", padx=20, pady=10)
        self.humidityText = customtkinter.CTkLabel(self.home_frame, text="Влажность")
        self.humidityText.grid(row=5, padx=30)
        self.humidity = customtkinter.CTkLabel(self.home_frame, text=self.get_humidity()+"%")
        self.humidity.grid(sticky="e", row=5,padx=100)
        self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="Вода", image=self.icon_2,
                                                           command=lambda: self.button('Water'))
        self.home_frame_button_3.grid(row=6, sticky="W", padx=20, pady=10)
        self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="Свет", image=self.icon_3,
                                                           command=lambda: self.button('Light'))
        self.home_frame_button_4.grid(row=7, sticky="W", padx=20, pady=10)
        # create help frame
        self.help()
        # create feedback frame
        self.feedbackFun()
        # select default frame
        self.select_frame_by_name("home")
        self.progressbar_1 = customtkinter.CTkProgressBar(self.home_frame)
        self.progressbar_1.grid(row=20, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()

    def navigation_frame_fun(self):
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=" EcoFlat",
                                                             image=self.logo_image,
                                                             text_color="green",
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.help_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Help",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.chat_image, anchor="w", command=self.help_button_event)
        self.help_button.grid(row=3, column=0, sticky="ew")

        self.feedback = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                text="Feedback",
                                                fg_color="transparent", text_color=("gray10", "gray90"),
                                                hover_color=("gray70", "gray30"),
                                                image=self.add_user_image, anchor="w",
                                                command=self.feedback_button_event)
        self.feedback.grid(row=4, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                values=["System", "Dark", "Light"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))
        self.scaling_optionemenu.set("100%")
    def help(self):
        self.help_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.help_frame.grid_columnconfigure(0, weight=1)
        self.scrollbar_help = customtkinter.CTkLabel(self.help_frame, bg_color="transparent",
                                                     justify=customtkinter.LEFT, text="")

        self.scrollbar_help.grid(row=0, column=0)
        self.textbox = customtkinter.CTkLabel(self.help_frame,text= """      
                     •Выберите растение-кнопка отвечающая за смену 
                         режимов теплицы
                     •Нагрев-кнопка отвечающая за включение
                         или отключение обогревателя
                     •Продув-кнопка отвечающая за включения
                         или отключения вентилятора
                     •Вода-кнопка отвечающая за подачу
                         воды для жизнидеятельности растений
                     •Свет-кнопка отвечающая за включение
                         или отключение света
                     •System-кнопка отвечающая за смену 
                         тем
                     •%-кнопка отвечающая за смену 
                         масштабов программы
                    """)
        self.textbox.grid(row=2,column=0)

    def feedbackFun(self):
        self.feedback_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.feedback_frame.grid_columnconfigure(0, weight=1)
        self.scrollbar_feedback = customtkinter.CTkLabel(self.feedback_frame,
                                                         justify=customtkinter.LEFT, bg_color="transparent",
                                                         text="""
                                                         
                                                         
                                                         
                                                         
                                                         
                                                         
                                                         
                                                         
                                                         
                ©Сязаться со SPARTA
                sparta.info2023@gmail.com
                +37499918631/+37494793697
                +37477114429/+79515433345

                Республика Армения, г. Ереван, ул. Мамиконянц 52,
                Ереванский государственный 
                Колледж информатики

                Россия, г. Воронеж, ул. Ленина 73а
                АНПОО Колледж Воронежского института 
                высоких технологий""")

        self.scrollbar_feedback.grid(sticky="n",padx=100)
    def images(self):
        self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"image python")
        self.logo_image = customtkinter.CTkImage(
            Image.open(os.path.join(self.image_path, r"icons8-greenhouse-with-flower-96.png")), size=(50, 50))
        self.large_test_image = customtkinter.CTkImage(
            Image.open(os.path.join(self.image_path, r"93z_2206_w009_n001_145b_p14_145.jpg")), size=(400, 200))
        self.icon = customtkinter.CTkImage(
            Image.open(os.path.join(self.image_path, r"icons8-temperature-inside-64.png")), size=(30, 30))
        self.icon_1 = customtkinter.CTkImage(
            Image.open(os.path.join(self.image_path, r"external-Cooler-propeller-others-inmotus-design-15.png")),
            size=(30, 30))
        self.icon_2 = customtkinter.CTkImage(
            Image.open(os.path.join(self.image_path, r"icons8-thirst-50.png")), size=(30, 30))
        self.icon_3 = customtkinter.CTkImage(
            Image.open(os.path.join(self.image_path, r"lightbulb.png")), size=(30, 30))
        self.icon_4 = customtkinter.CTkImage(Image.open(os.path.join(self.image_path,
                                                                     r"icon_thermometer.png")), size=(60, 60))
        self.icon_5 = customtkinter.CTkImage(Image.open(os.path.join(self.image_path,
                                                                     r"dewpoint.png")),
                                             size=(60, 60))
        self.icon_6 = customtkinter.CTkImage(Image.open(os.path.join(self.image_path,
                                                                     r"wind.png")),
                                             size=(60, 60))

        self.home_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(self.image_path, r"icons8-home-64.png")),
            dark_image=Image.open(os.path.join(self.image_path, r"icons8-home-64.png")), size=(40, 40))
        self.chat_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(self.image_path, r"help-icon-3.png")),
            dark_image=Image.open(os.path.join(self.image_path, r"help-icon-3.png")), size=(40, 40))
        self.add_user_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(self.image_path, r"icons8-comments-64.png")),
            dark_image=Image.open(os.path.join(self.image_path, r"icons8-comments-64.png")), size=(40, 40))
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.help_button.configure(fg_color=("gray75", "gray25") if name == "help" else "transparent")
        self.feedback.configure(fg_color=("gray75", "gray25") if name == "feedback" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "help":
            self.help_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.help_frame.grid_forget()
        if name == "feedback":
            self.feedback_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.feedback_frame.grid_forget()


    def get_temperature(self):
        while True:
            ref = db.reference('/Temperature')
            return ref.get()

    def get_humidity(self):
        while True:
            ref = db.reference('/Humidity')
            return ref.get()
    # sets into firebase
    def set(self, part, bool):
        ref = db.reference('/')
        ref.update({part: bool})

    # main buttons command
    def button(self, function):
        ref = db.reference('/')
        if ref.get()[function]:
            self.set(function, False)
        else:
            self.set(function, True)

    def home_button_event(self):
        self.select_frame_by_name("home")

    def values_button_event(self):
        self.select_frame_by_name("value")

    def help_button_event(self):
        self.select_frame_by_name("help")

    def feedback_button_event(self):
        self.select_frame_by_name("feedback")

    # changing modes
    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # changing scale
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    # changing types


app = App()
app.mainloop()
while True:
    temperature = customtkinter.CTkLabel(app.home_frame, text=app.get_temperature() + "°C")
    temperature.grid(sticky="e", row=4, padx=100)
    humidity = customtkinter.CTkLabel(app.home_frame, text=app.get_humidity() + "%")
    humidity.grid(sticky="e", row=5, padx=100)


