import customtkinter
import os
from PIL import Image,ImageTk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("smart_greenhouse.py")
        self.geometry("750x550")

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
        #self.ref.set({
         #   'Plant types': 'None',
        #    'Heating': False,
        #    'Cooling': False,
          #  'Water': False,
         #   'Ozon': False
       # })

        # load images with light and dark mode image
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
            Image.open(os.path.join(self.image_path, r"icons8-ozone-structure-64.png")), size=(30, 30))
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
        self.values_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(self.image_path, r"icon_value.png")),
            dark_image=Image.open(os.path.join(self.image_path, r"icon_value.png")), size=(40, 40))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  SMART GREENHOUSE",
                                                             image=self.logo_image,
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")
        self.values_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                     border_spacing=10, text="Values",
                                                     fg_color="transparent", text_color=("gray10", "gray90"),
                                                     hover_color=("gray70", "gray30"),
                                                     image=self.values_image, anchor="w",
                                                     command=self.values_button_event)
        self.values_button.grid(row=2, column=0, sticky="ew")

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

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="",
                                                                   image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="Heater", image=self.icon,
                                                           command=lambda: self.button('Heating'))
        self.home_frame_button_1.grid(row=4, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Cooler", image=self.icon_1,
                                                           command=lambda: self.button('Cooling'))
        self.home_frame_button_2.grid(row=5, column=0, padx=20, pady=10)
        self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="Water", image=self.icon_2,
                                                           command=lambda: self.button('Water'))
        self.home_frame_button_3.grid(row=6, column=0, padx=20, pady=10)
        self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="Ozon", image=self.icon_3,
                                                           command=lambda: self.button('Ozon'))
        self.home_frame_button_4.grid(row=7, column=0, padx=20, pady=10)
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))
        self.scaling_optionemenu.set("100%")
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.home_frame,
                                                               values=['None', 'Auto', 'Tomato', 'Cucumber',
                                                                       'Chamomile'],
                                                               command=self.change_mod_event)
        self.scaling_optionemenu.grid(row=3, column=0, padx=20, pady=(10), sticky="nsew")
        self.scaling_optionemenu.set("None")

        # create help frame
        self.help_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.help_frame.grid_columnconfigure(0, weight=1)
        self.scrollbar_help = customtkinter.CTkLabel(self.help_frame, bg_color="transparent",
                                                     justify=customtkinter.LEFT, text="")

        self.scrollbar_help.grid(row=0, column=0)
        self.textbox = customtkinter.CTkTextbox(self.help_frame, width=450)
        self.textbox.grid(row=0, column=2, padx=(10), pady=(100), sticky="nsew")
        self.textbox.insert("0.1",
                            """      
                     ․None-ջերմոցի ռեժիմները փոփոխելու 
                         համար պատասխանատու կոճակ
                     •Heater-տաքացուցիչը միացնելու և անջատելու 
                         համար պատասխանատու կոճակ
                     •Cooler-հովհացման համակարգը միացնելու և անջատելու
                         համար պատասխանատու կոճակ
                     •Water-բույսերի կենսագործունեության համար անհրաժեշտ
                          ջուրը 
                         միացնելու և անջատելու համար պատասխանատու կոճակ
                     •Ozon-թթվածինն օզոնով հագեցնելու
                         համար պատասխանատու կոճակ
                     •System-գունային գամայի փոփոխման համար 
                         պատասխանատու կոճակ
                     •%-ծրագրի մասշտաբը փոփոխելու համար 
                         պատասխանատու կոճակ
                     •Feedback-հետադարձ կապ  
                      
                     •None-button responsible for changing 
                         the modes of the greenhouse
                     •Heater-button responsible for 
                         turning the heater on and off
                     •Cooler-button responsible for
                         turning the ventilation system 
                         on and off
                     •Water-button responsible for turning 
                         on and off necessary water 
                         for plant life
                     •Ozon-button responsible for
                         saturation oxygen with ozone
                     •System-button responsible for 
                         changing the theme
                     •%-button responsible for 
                         changing the project scale 
                      
                     •None-кнопка отвечающая за смену 
                         режимов теплицы
                     •Heater-кнопка отвечающая за включения
                         или отключения обогревателя
                     •Cooler-кнопка отвечающая за включения
                         или отключения охлаждения
                     •Water-кнопка отвечающая за подачу
                         воды для жизнидеятельности растений
                     •Ozon-кнопка отвечающая за подачу
                         озонированного кислорода
                     •System-кнопка отвечающая за смену 
                         тем
                     •%-кнопка отвечающая за смену 
                         масштабов программы
                     •Feedback-Обратная связь """)

        # create feedback frame
        self.feedback_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.feedback_frame.grid_columnconfigure(0, weight=1)
        self.scrollbar_feedback = customtkinter.CTkLabel(self.feedback_frame,
                                                         justify=customtkinter.LEFT, bg_color="transparent",
                                                         text="""


        ©SPARTA-յի հետ կապ հաստատելու համար
        sparta.info2023@gmail.com
        +37499918631/+37494793697/+37477114429
        Երևան, Մամիկոնյանց 52,
        Երևանի ինֆորմատիկայի պետական քոլեջ


        ©To contact SPARTA
        sparta.info2023@gmail.com
        +37499918631/+37494793697/+37477114429
        Yerevan, Armenia, Mamikoniants 52,
        Yerevan state college of Informatics


        ©Сязаться со SPARTA
        sparta.info2023@gmail.com
        +37499918631/+37494793697/+37477114429
        Ереван, Мамиконянц 52,
        Ереванский государственный колледж информатики""")

        self.scrollbar_feedback.grid(row=0, column=0)

        #value frame
        self.value_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.value_frame.grid_columnconfigure(0, weight=1)
        self.value_frame_button = customtkinter.CTkButton(self.value_frame, text="Water sensor", image=self.icon_4)
        self.value_frame_button.grid(row=2,column=0,padx=20, pady=50)
        self.value_frame_button_1 = customtkinter.CTkButton(self.value_frame, text="Water sensor",
                                                            image=self.icon_5)
        self.value_frame_button_1.grid(row=4,column=0,padx=20, pady=10)
        self.value_frame_button_2 = customtkinter.CTkButton(self.value_frame, text="Water sensor",
                                                            image=self.icon_5)
        self.value_frame_button_2.grid(row=2, column=1,padx=20, pady=10)
        self.value_frame_button_3 = customtkinter.CTkButton(self.value_frame, text="Water sensor",
                                                            image=self.icon_6)
        self.value_frame_button_3.grid(row=4,column=1,padx=20, pady=10)
        # select default frame
        self.select_frame_by_name("home")

        self.progressbar_1 = customtkinter.CTkProgressBar(self.home_frame)
        self.progressbar_1.grid(row=20, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.values_button.configure(fg_color=("gray75", "gray25") if name == "value" else "transparent")
        self.help_button.configure(fg_color=("gray75", "gray25") if name == "help" else "transparent")
        self.feedback.configure(fg_color=("gray75", "gray25") if name == "feedback" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "value":
            self.value_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.value_frame.grid_forget()
        if name == "help":
            self.help_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.help_frame.grid_forget()
        if name == "feedback":
            self.feedback_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.feedback_frame.grid_forget()

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
    def change_mod_event(self, new_scaling: str):
        self.set('Plant types', new_scaling)


app = App()
app.mainloop()
