from tkinter import *
from tkinter import ttk, scrolledtext
from tkcalendar import DateEntry
from datetime import datetime
import webbrowser
import os


class SportsBookingClient:
    def __init__(self):
        self.root = Tk()
        self.root.title("СОК «Калининец» - Онлайн-бронирование")
        self.root.geometry("1348x780")
        self.root.resizable(False, False)

        # Текущая тема (0 - светлая, 1 - темная)
        self.current_theme = 0

        # Цветовые схемы
        self.light_theme = {
            'bg': '#ffffff',  # Чистый белый фон
            'fg': '#000080',  # синий текст
            'fg_secondary': '#7f8c8d',  # Серый подзаголовок
            'button_bg': '#000080',  # Темные кнопки
            'button_fg': 'white',  # Белый текст кнопок
            'button_active': '#3498db',  # Синий при наведении
            'accent': '#27ae60',  # Зеленый акцент
            'copyright': '#95a5a6',  # Серый копирайт
            'window_bg': '#ffffff',  # Белый фон окон
            'frame_bg': '#f8f9fa',  # Светло-серый фон фреймов
            'entry_bg': '#ffffff',  # Белый фон полей ввода
            'entry_fg': '#000080',  # Темный текст полей
            'labelframe_bg': '#ffffff',  # Белый фон рамок
            'separator': '#dee2e6',  # Светлый разделитель
            'link': '#3498db'  # Синий цвет ссылок
        }

        self.dark_theme = {
            'bg': '#1a1a2e',  # Темно-синий фон
            'fg': '#e6e6e6',  # Светло-серый текст
            'fg_secondary': '#b0b0b0',  # Серый подзаголовок
            'button_bg': '#3498db',  # Синие кнопки
            'button_fg': 'white',  # Белый текст кнопок
            'button_active': '#2980b9',  # Темно-синий при наведении
            'accent': '#27ae60',  # Зеленый акцент
            'copyright': '#7f8c8d',  # Серый копирайт
            'window_bg': '#1a1a2e',  # Темный фон окон
            'frame_bg': '#16213e',  # Темно-синий фон фреймов
            'entry_bg': '#2c3e50',  # Темно-синий фон полей ввода
            'entry_fg': '#e6e6e6',  # Светлый текст полей
            'labelframe_bg': '#1a1a2e',  # Темный фон рамок
            'separator': '#34495e',  # Темный разделитель
            'link': '#3498db'  # Синий цвет ссылок
        }

        self.colors = self.light_theme

        self.theme_icons = {
            'light': "🌙",
            'dark': "☀️"
        }

        # Настройка стиля
        self.setup_styles()

        # Загрузка изображений для кнопок
        self.load_button_images()

        # Создаем главное меню с кнопками-изображениями
        self.create_main_menu_with_images()

    def setup_styles(self):
        """Настройка стилей кнопок"""
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Стили для светлой темы
        self.update_styles()

    def update_styles(self):
        """Обновление стилей в зависимости от темы"""
        self.style.configure('.',
                             background=self.colors['bg'],
                             foreground=self.colors['fg'])

        # Стиль для кнопок меню
        self.style.configure('Menu.TButton',
                             font=('Arial', 12, 'bold'),
                             padding=15,
                             relief='flat',
                             background=self.colors['button_bg'],
                             foreground=self.colors['button_fg'],
                             borderwidth=0,
                             focuscolor='none')

        self.style.map('Menu.TButton',
                       background=[('active', self.colors['button_active'])],
                       foreground=[('active', 'white')])

        self.style.configure('Child.TButton',
                             font=('Arial', 12, 'bold'),
                             padding=10,
                             background=self.colors['button_bg'],
                             foreground=self.colors['button_fg'],
                             borderwidth=0)

        self.style.map('Child.TButton',
                       background=[('active', self.colors['button_active'])],
                       foreground=[('active', 'white')])

        # Стиль для Treeview
        self.style.configure('Treeview',
                             background=self.colors['window_bg'],
                             foreground=self.colors['fg'],
                             fieldbackground=self.colors['window_bg'],
                             borderwidth=0)

        self.style.configure('Treeview.Heading',
                             background=self.colors['frame_bg'],
                             foreground=self.colors['fg'],
                             borderwidth=0)

        # Стили для полей ввода
        self.style.configure('TEntry',
                             fieldbackground=self.colors['entry_bg'],
                             foreground=self.colors['entry_fg'],
                             insertcolor=self.colors['entry_fg'],
                             borderwidth=1,
                             relief='solid')

        self.style.map('TEntry',
                       fieldbackground=[('active', self.colors['entry_bg'])],
                       foreground=[('active', self.colors['entry_fg'])])

        # Стиль для Combobox
        self.style.configure('TCombobox',
                             fieldbackground=self.colors['entry_bg'],
                             foreground=self.colors['entry_fg'],
                             background=self.colors['entry_bg'],
                             borderwidth=1,
                             relief='solid')

        self.style.map('TCombobox',
                       fieldbackground=[('active', self.colors['entry_bg'])],
                       foreground=[('active', self.colors['entry_fg'])])

        # Стиль для Frame
        self.style.configure('TFrame',
                             background=self.colors['bg'])

        # Стиль для LabelFrame
        self.style.configure('TLabelframe',
                             background=self.colors['labelframe_bg'],
                             foreground=self.colors['fg'],
                             borderwidth=1,
                             relief='solid')

        self.style.configure('TLabelframe.Label',
                             background=self.colors['labelframe_bg'],
                             foreground=self.colors['fg'])

        # Стиль для Label
        self.style.configure('TLabel',
                             background=self.colors['bg'],
                             foreground=self.colors['fg'])

        # Стиль для Separator
        self.style.configure('TSeparator',
                             background=self.colors['separator'])

    def load_button_images(self):
        """Загрузка изображений для кнопок главного меню"""
        self.button_images = {}

        button_files = [
            ('btn_n1', '1.png'),
            ('btn_n2', '2.png'),
            ('btn_n3', '3.png'),
            ('btn_n4', '4.png'),
            ('btn_h1', '1h.png'),
            ('btn_h2', '2h.png'),
            ('btn_h3', '3h.png'),
            ('btn_h4', '4h.png')
        ]

        # Пытаемся загрузить изображения
        for key, filename in button_files:
            try:
                if os.path.exists(filename):
                    self.button_images[key] = PhotoImage(file=filename)
                    print(f"Загружено: {filename}")
                else:
                    # Создаем текстовую кнопку вместо изображения
                    self.create_text_button_image(key, filename)
            except Exception as e:
                print(f"Ошибка загрузки {filename}: {e}")
                self.create_text_button_image(key, filename)

    def create_text_button_image(self, key, filename):
        """Создание текстовой кнопки, если изображение не найдено"""
        # Определяем текст для кнопки по ключу
        if 'btn_n1' in key or 'btn_h1' in key:
            text = "Вход / Регистрация"
        elif 'btn_n2' in key or 'btn_h2' in key:
            text = "Бронирование услуг"
        elif 'btn_n3' in key or 'btn_h3' in key:
            text = "Мои бронирования"
        elif 'btn_n4' in key or 'btn_h4' in key:
            text = "Контакты"
        else:
            text = "Кнопка"

        # Определяем цвет для нормального и hover состояния
        if '_n' in key:  # normal
            bg_color = self.colors['button_bg']
        else:  # hover
            bg_color = self.colors['button_active']

        # Создаем изображение с текстом
        img = PhotoImage(width=200, height=60)

        # Сохраняем в словарь
        self.button_images[key] = img

    def create_main_menu_with_images(self):
        """Создание главного меню с кнопками-изображениями"""
        self.root.configure(bg=self.colors['bg'])

        # Заголовок
        title_label = Label(self.root,
                            text='Спортивно-оздоровительный комплекс «Калининец»',
                            font=('Cambria', 25),
                            bg=self.colors['bg'],
                            fg=self.colors['fg'])
        title_label.place(x=200, y=10)

        # Кнопка переключения темы
        theme_frame = Frame(self.root, bg=self.colors['bg'])
        theme_frame.is_theme_frame = True
        theme_frame.place(x=1200, y=10, width=100, height=50)

        self.theme_button = Button(theme_frame,
                                   text=self.theme_icons['dark'],
                                   font=('Arial', 16),
                                   bg=self.colors['bg'],
                                   fg=self.colors['fg'],
                                   borderwidth=0,
                                   activebackground=self.colors['bg'],
                                   activeforeground=self.colors['fg'],
                                   command=self.toggle_theme)
        self.theme_button.is_theme_button = True
        self.theme_button.pack(side=RIGHT)

        # Основной текст о комплексе
        about_text = """Один из наиболее мощных спортивных комплексов города Екатеринбурга — спорткомплекс «Калининец» создавался в конце 70-х годов. До 1994 года он принадлежал машиностроительному заводу имени М.И. Калинина, а в настоящее время является муниципальной собственностью города. Ежедневно сооружения спорткомплекса посещают 1500-2000 человек.

В состав комплекса входят:
• 50-метровый бассейн с артезианской водой
• Легкоатлетический манеж с 200-метровой дорожкой
• Спортивный павильон с залами единоборств
• Лыжная база с трассами 2-10 км
• Стадион с искусственным покрытием
• Стрелковый тир

СК «Калининец» — самый большой по площади спортивно-оздоровительный комплекс Уральского региона, являющийся одной из тренировочных баз ЧМ-2018 по футболу, расположенный в лесопарковой зоне города."""

        text_widget = Text(self.root, height=15, width=110, wrap=WORD,
                           font=("Arial", 14),
                           bg=self.colors['bg'],
                           fg=self.colors['fg'],
                           relief=FLAT,
                           borderwidth=0,
                           padx=10,
                           pady=10)
        text_widget.insert(1.0, about_text)
        text_widget.config(state=DISABLED)
        text_widget.place(x=57, y=370)

        about_text_1 = """На базе комплекса работают спортивные школы:
• СШ №19 «Детский стадион»
• СШ №16 (единоборства)
• СШОР «Локомотив–Изумруд» (волейбол)
• СДЮСШОР по велоспорту
• СШ «УРАЛ» (футбол)
• СШ «Родонит» (спортивное ориентирование)"""

        text_widget_1 = Text(self.root, height=7, width=40, wrap=WORD,
                           font=("Arial", 14),
                           bg=self.colors['bg'],
                           fg=self.colors['fg'],
                           relief=FLAT,
                           borderwidth=0,
                           padx=10,
                           pady=10)
        text_widget_1.insert(1.0, about_text_1)
        text_widget_1.config(state=DISABLED)
        text_widget_1.place(x=757, y=456)

        # Создаём кнопки с изображениями
        self.create_image_buttons()

        # Копирайт
        copyright_label = Label(self.root,
                                text="© 2026 СОК Калининец",
                                font=('Arial', 12),
                                fg=self.colors['copyright'],
                                bg=self.colors['bg'])
        copyright_label.place(x=580, y=730)

    def create_image_buttons(self):
        """Создание кнопок с изображениями"""
        if 'btn_n1' in self.button_images and 'btn_h1' in self.button_images:
            self.knopka1 = Button(self.root,
                                  borderwidth=0,
                                  bg=self.colors['bg'],
                                  activebackground=self.colors['bg'],
                                  image=self.button_images['btn_n1'],
                                  command=self.open_login_window)
            self.knopka1.place(x=50, y=58)

            # Назначаем события hover
            self.knopka1.bind('<Enter>', lambda e: self.knopka1.config(image=self.button_images['btn_h1']))
            self.knopka1.bind('<Leave>', lambda e: self.knopka1.config(image=self.button_images['btn_n1']))
        else:
            # Если нет изображения, создаем текстовую кнопку
            self.knopka1 = Button(self.root,
                                  text="Вход / Регистрация",
                                  bg=self.colors['button_bg'],
                                  fg=self.colors['button_fg'],
                                  activebackground=self.colors['button_active'],
                                  font=('Arial', 14, 'bold'),
                                  command=self.open_login_window)
            self.knopka1.place(x=50, y=58, width=200, height=60)

        if 'btn_n2' in self.button_images and 'btn_h2' in self.button_images:
            self.knopka2 = Button(self.root,
                                  borderwidth=0,
                                  bg=self.colors['bg'],
                                  activebackground=self.colors['bg'],
                                  image=self.button_images['btn_n2'],
                                  command=self.open_booking_window)
            self.knopka2.place(x=360, y=58)

            self.knopka2.bind('<Enter>', lambda e: self.knopka2.config(image=self.button_images['btn_h2']))
            self.knopka2.bind('<Leave>', lambda e: self.knopka2.config(image=self.button_images['btn_n2']))
        else:
            self.knopka2 = Button(self.root,
                                  text="Бронирование услуг",
                                  bg=self.colors['button_bg'],
                                  fg=self.colors['button_fg'],
                                  activebackground=self.colors['button_active'],
                                  font=('Arial', 14, 'bold'),
                                  command=self.open_booking_window)
            self.knopka2.place(x=360, y=58, width=200, height=60)

        if 'btn_n3' in self.button_images and 'btn_h3' in self.button_images:
            self.knopka3 = Button(self.root,
                                  borderwidth=0,
                                  bg=self.colors['bg'],
                                  activebackground=self.colors['bg'],
                                  image=self.button_images['btn_n3'],
                                  command=self.open_my_bookings_window)
            self.knopka3.place(x=670, y=58)

            self.knopka3.bind('<Enter>', lambda e: self.knopka3.config(image=self.button_images['btn_h3']))
            self.knopka3.bind('<Leave>', lambda e: self.knopka3.config(image=self.button_images['btn_n3']))
        else:
            self.knopka3 = Button(self.root,
                                  text="Мои бронирования",
                                  bg=self.colors['button_bg'],
                                  fg=self.colors['button_fg'],
                                  activebackground=self.colors['button_active'],
                                  font=('Arial', 14, 'bold'),
                                  command=self.open_my_bookings_window)
            self.knopka3.place(x=670, y=58, width=200, height=60)

        if 'btn_n4' in self.button_images and 'btn_h4' in self.button_images:
            self.knopka4 = Button(self.root,
                                  borderwidth=0,
                                  bg=self.colors['bg'],
                                  activebackground=self.colors['bg'],
                                  image=self.button_images['btn_n4'],
                                  command=self.open_contacts_window)
            self.knopka4.place(x=980, y=58)

            self.knopka4.bind('<Enter>', lambda e: self.knopka4.config(image=self.button_images['btn_h4']))
            self.knopka4.bind('<Leave>', lambda e: self.knopka4.config(image=self.button_images['btn_n4']))
        else:
            self.knopka4 = Button(self.root,
                                  text="Контакты",
                                  bg=self.colors['button_bg'],
                                  fg=self.colors['button_fg'],
                                  activebackground=self.colors['button_active'],
                                  font=('Arial', 14, 'bold'),
                                  command=self.open_contacts_window)
            self.knopka4.place(x=980, y=58, width=200, height=60)

    def toggle_theme(self):
        """Переключение темы"""
        self.current_theme = 1 - self.current_theme  # Переключаем между 0 и 1

        if self.current_theme == 0:
            self.colors = self.light_theme
            self.theme_button.config(text=self.theme_icons['dark'])
        else:
            self.colors = self.dark_theme
            self.theme_button.config(text=self.theme_icons['light'])

        # Обновляем стили
        self.update_styles()

        # Применяем тему к главному окну
        self.apply_theme_to_window(self.root)

        # Обновляем все дочерние окна
        for child in self.root.winfo_children():
            if isinstance(child, Toplevel):
                self.apply_theme_to_window(child)

    def apply_theme_to_window(self, window):
        """Применение темы к окну и всем его виджетам"""
        window.configure(bg=self.colors['bg'])
        self.apply_theme_to_widgets(window)

    def apply_theme_to_widgets(self, parent):
        """Рекурсивное применение темы к виджетам"""
        try:
            for widget in parent.winfo_children():
                widget_type = widget.winfo_class()

                # Применяем тему в зависимости от типа виджета
                if widget_type == 'Label':
                    if widget.cget('text') == 'Добро пожаловать в Спортивный комплекс «Калининец»!':
                        widget.configure(bg=self.colors['bg'],
                                         fg=self.colors['fg'],
                                         font=('Cambria', 25))
                    elif widget.cget('text') == "© 2025 СОК Калининец":
                        widget.configure(bg=self.colors['bg'],
                                         fg=self.colors['copyright'],
                                         font=('Arial', 12))
                    else:
                        widget.configure(bg=self.colors['bg'],
                                         fg=self.colors['fg'])

                elif widget_type == 'Frame':
                    if hasattr(widget, 'is_theme_frame'):
                        widget.configure(bg=self.colors['bg'])
                    else:
                        widget.configure(bg=self.colors['frame_bg'])
                    self.apply_theme_to_widgets(widget)

                elif widget_type == 'TFrame':
                    # Для ttk.Frame
                    widget.configure(style='TFrame')
                    self.apply_theme_to_widgets(widget)

                elif widget_type == 'TLabelFrame':
                    # Для ttk.LabelFrame
                    widget.configure(style='TLabelframe')
                    self.apply_theme_to_widgets(widget)

                elif widget_type == 'TLabel':
                    # Для ttk.Label
                    widget.configure(style='TLabel')

                elif widget_type == 'Button':
                    if hasattr(widget, 'is_theme_button') and widget.is_theme_button:
                        widget.configure(bg=self.colors['bg'],
                                         fg=self.colors['fg'],
                                         activebackground=self.colors['bg'],
                                         activeforeground=self.colors['fg'])
                    else:
                        # Проверяем, есть ли у кнопки изображение
                        if widget.cget('image'):
                            # Для кнопок с изображениями обновляем только фон
                            widget.configure(bg=self.colors['bg'],
                                           activebackground=self.colors['bg'])
                        else:
                            # Для текстовых кнопок обновляем все свойства
                            widget.configure(bg=self.colors['button_bg'],
                                           fg=self.colors['button_fg'],
                                           activebackground=self.colors['button_active'])

                elif widget_type == 'TButton':
                    widget.configure(style='Child.TButton')

                elif widget_type == 'TEntry' or widget_type == 'TCombobox':
                    widget.configure(style='TEntry')

                elif widget_type == 'Text' or widget_type == 'ScrolledText':
                    widget.configure(bg=self.colors['entry_bg'],
                                     fg=self.colors['entry_fg'],
                                     insertbackground=self.colors['entry_fg'])

                elif widget_type == 'TSeparator':
                    widget.configure(style='TSeparator')

                else:
                    try:
                        self.apply_theme_to_widgets(widget)
                    except:
                        pass

        except Exception as e:
            print(f"Ошибка при применении темы: {e}")

    # ==================== ОКНО ВХОДА / РЕГИСТРАЦИИ ====================
    def open_login_window(self):
        """Окно входа и регистрации"""
        window = Toplevel(self.root)
        window.title("Вход / Регистрация")
        window.geometry("400x450")
        window.transient(self.root)
        window.grab_set()

        # Применяем тему
        self.apply_theme_to_window(window)

        title_label = ttk.Label(window,
                                text="Вход в систему",
                                font=('Arial', 14, 'bold'))
        title_label.pack(pady=20)

        # Контейнер формы
        form_frame = ttk.LabelFrame(window, text="Данные для входа", padding=20)
        form_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

        # Email
        email_label = ttk.Label(form_frame, text="Email:")
        email_label.grid(row=0, column=0, sticky=W, pady=(10, 0))
        email_entry = ttk.Entry(form_frame, width=30, style='TEntry')
        email_entry.grid(row=0, column=1, pady=(10, 0), padx=(10, 0))

        # Пароль
        password_label = ttk.Label(form_frame, text="Пароль:")
        password_label.grid(row=1, column=0, sticky=W, pady=10)
        password_entry = ttk.Entry(form_frame, width=30, show='*', style='TEntry')
        password_entry.grid(row=1, column=1, pady=10, padx=(10, 0))

        # Кнопки
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=20)

        login_btn = ttk.Button(button_frame, text="Войти",
                               command=lambda: self.login(email_entry.get(), password_entry.get()),
                               style='Child.TButton')
        login_btn.pack(side=LEFT, padx=5)

        clear_btn = ttk.Button(button_frame, text="Очистить",
                               command=lambda: self.clear_login_form(email_entry, password_entry),
                               style='Child.TButton')
        clear_btn.pack(side=LEFT, padx=5)

        # Разделитель
        separator = ttk.Separator(window, orient='horizontal')
        separator.pack(fill=X, padx=20, pady=10)

        # Кнопка регистрации
        register_frame = ttk.Frame(window, padding=10)
        register_frame.pack(fill=X)

        no_account_label = ttk.Label(register_frame, text="Нет аккаунта?")
        no_account_label.pack(side=LEFT, padx=(0, 10))

        register_btn = ttk.Button(register_frame, text="Зарегистрироваться",
                                  command=lambda: self.open_register_window(window),
                                  style='Child.TButton')
        register_btn.pack(side=LEFT)

    def clear_login_form(self, email_entry, password_entry):
        """Очистка формы входа"""
        email_entry.delete(0, END)
        password_entry.delete(0, END)

    def login(self, email, password):
        """Обработка входа"""
        if not email or not password:
            self.show_custom_message("Ошибка", "Заполните все поля")
            return

        # Тестовый вход для демонстрации
        if email == "test@example.com" and password == "password":
            self.show_custom_message("Успешно", "Вход выполнен успешно!")
        else:
            self.show_custom_message("Ошибка", "Неверный email или пароль")

    def open_register_window(self, parent_window):
        """Открыть окно регистрации"""
        parent_window.destroy()

        window = Toplevel(self.root)
        window.title("Регистрация")
        window.geometry("600x520")
        window.transient(self.root)
        window.grab_set()

        # Применяем тему
        self.apply_theme_to_window(window)

        # Заголовок
        title_label = ttk.Label(window,
                                text="Регистрация",
                                font=('Arial', 14, 'bold'))
        title_label.pack(pady=20)

        # Контейнер формы
        form_frame = ttk.LabelFrame(window, text="Данные для регистрации", padding=20)
        form_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

        # Валидационные функции
        def validate_name(text):
            """Валидация имени: только буквы, пробелы и дефисы"""
            if text == "":
                return True
            # Разрешаем буквы (русские и латинские), пробелы, дефисы и апострофы
            for char in text:
                if not (char.isalpha() or char in " -'"):
                    return False
            return True

        def validate_phone(text):
            """Валидация телефона: только цифры и плюс в начале"""
            if text == "":
                return True
            if text.startswith('+'):
                return text[1:].isdigit()
            else:
                # Автоматически добавляем плюс, если пользователь ввел цифры без него
                if text.isdigit():
                    return True
                return False

        def validate_email(text):
            """Валидация email: должен содержать @"""
            if text == "":
                return True
            return '@' in text

        def validate_password(text):
            """Валидация пароля: минимум 8 символов"""
            if text == "":
                return True
            return len(text) >= 8

        def on_name_change(var_name, index, mode):
            """Отслеживание изменений в поле имени"""
            current_text = name_var.get()
            if not validate_name(current_text) and current_text:
                # Удаляем последний введенный символ если он невалидный
                name_var.set(current_text[:-1])

        def on_phone_change(var_name, index, mode):
            """Отслеживание изменений в поле телефона"""
            current_text = phone_var.get()
            if not validate_phone(current_text) and current_text:
                # Удаляем последний введенный символ если он невалидный
                phone_var.set(current_text[:-1])
            # Автоматически добавляем плюс если пользователь начал вводить цифры
            elif current_text.isdigit() and len(current_text) > 0:
                phone_var.set('+' + current_text)

        # Переменные для отслеживания изменений
        name_var = StringVar()
        phone_var = StringVar()
        email_var = StringVar()
        password_var = StringVar()
        confirm_password_var = StringVar()

        # Настройка отслеживания изменений
        name_var.trace('w', on_name_change)
        phone_var.trace('w', on_phone_change)

        # Имя
        name_label = ttk.Label(form_frame, text="ФИО:")
        name_label.grid(row=0, column=0, sticky=W, pady=(5, 0))
        name_entry = ttk.Entry(form_frame, width=30, textvariable=name_var, style='TEntry')
        name_entry.grid(row=0, column=1, pady=(5, 0), padx=(10, 0))
        ttk.Label(form_frame, text="только буквы и пробелы",
                  font=('Arial', 8), foreground=self.colors['fg_secondary']
                  ).grid(row=0, column=2, padx=(5, 0), pady=(5, 0), sticky=W)

        # Телефон
        phone_label = ttk.Label(form_frame, text="Телефон:")
        phone_label.grid(row=1, column=0, sticky=W, pady=10)
        phone_entry = ttk.Entry(form_frame, width=30, textvariable=phone_var, style='TEntry')
        phone_entry.grid(row=1, column=1, pady=10, padx=(10, 0))
        ttk.Label(form_frame, text="формат: +79123456789",
                  font=('Arial', 8), foreground=self.colors['fg_secondary']
                  ).grid(row=1, column=2, padx=(5, 0), pady=10, sticky=W)

        # Email
        email_label = ttk.Label(form_frame, text="Email:")
        email_label.grid(row=2, column=0, sticky=W, pady=10)
        email_entry = ttk.Entry(form_frame, width=30, textvariable=email_var, style='TEntry')
        email_entry.grid(row=2, column=1, pady=10, padx=(10, 0))
        ttk.Label(form_frame, text="должен содержать @",
                  font=('Arial', 8), foreground=self.colors['fg_secondary']
                  ).grid(row=2, column=2, padx=(5, 0), pady=10, sticky=W)

        # Пароль
        password_label = ttk.Label(form_frame, text="Пароль:")
        password_label.grid(row=3, column=0, sticky=W, pady=10)
        password_entry = ttk.Entry(form_frame, width=30, show='*',
                                   textvariable=password_var, style='TEntry')
        password_entry.grid(row=3, column=1, pady=10, padx=(10, 0))
        ttk.Label(form_frame, text="минимум 8 символов",
                  font=('Arial', 8), foreground=self.colors['fg_secondary']
                  ).grid(row=3, column=2, padx=(5, 0), pady=10, sticky=W)

        # Подтверждение пароля
        confirm_label = ttk.Label(form_frame, text="Подтвердите пароль:")
        confirm_label.grid(row=4, column=0, sticky=W, pady=10)
        confirm_password_entry = ttk.Entry(form_frame, width=30, show='*',
                                           textvariable=confirm_password_var, style='TEntry')
        confirm_password_entry.grid(row=4, column=1, pady=10, padx=(10, 0))

        # Индикаторы валидации
        validation_frame = ttk.Frame(form_frame)
        validation_frame.grid(row=5, column=0, columnspan=3, pady=(10, 0), sticky=W)

        self.name_valid = BooleanVar(value=False)
        self.phone_valid = BooleanVar(value=False)
        self.email_valid = BooleanVar(value=False)
        self.password_valid = BooleanVar(value=False)
        self.passwords_match = BooleanVar(value=False)

        # Функция для обновления индикаторов
        def update_validation_indicators():
            name = name_var.get()
            phone = phone_var.get()
            email = email_var.get()
            password = password_var.get()
            confirm_password = confirm_password_var.get()

            self.name_valid.set(validate_name(name) and len(name.strip()) >= 2)
            self.phone_valid.set(validate_phone(phone) and len(phone) >= 12)  # +79123456789 = 12 символов
            self.email_valid.set(validate_email(email) and len(email) >= 5)
            self.password_valid.set(validate_password(password))
            self.passwords_match.set(password == confirm_password and password != "")

        # Связываем обновление индикаторов с изменением полей
        for var in [name_var, phone_var, email_var, password_var, confirm_password_var]:
            var.trace('w', lambda *args: update_validation_indicators())

        # Сразу обновляем индикаторы
        update_validation_indicators()

        # Кнопки
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=6, column=0, columnspan=2, pady=20)

        register_btn = ttk.Button(button_frame, text="Зарегистрироваться",
                                  command=lambda: self.register(
                                      name_var.get(), phone_var.get(),
                                      email_var.get(), password_var.get(),
                                      confirm_password_var.get(), window,
                                      self.name_valid.get(), self.phone_valid.get(),
                                      self.email_valid.get(), self.password_valid.get(),
                                      self.passwords_match.get()),
                                  style='Child.TButton')
        register_btn.pack(side=LEFT, padx=5)

        clear_btn = ttk.Button(button_frame, text="Очистить",
                               command=lambda: self.clear_register_form(
                                   name_var, phone_var, email_var,
                                   password_var, confirm_password_var),
                               style='Child.TButton')
        clear_btn.pack(side=LEFT, padx=5)

        # Кнопка назад
        back_frame = ttk.Frame(window, padding=10)
        back_frame.pack(fill=X)

        back_btn = ttk.Button(back_frame, text="Назад к входу",
                              command=lambda: self.back_to_login(window),
                              style='Child.TButton')
        back_btn.pack()

    def clear_register_form(self, name_var, phone_var, email_var, password_var, confirm_password_var):
        """Очистка формы регистрации"""
        name_var.set('')
        phone_var.set('')
        email_var.set('')
        password_var.set('')
        confirm_password_var.set('')

    def register(self, name, phone, email, password, confirm_password, window,
                 name_valid=False, phone_valid=False, email_valid=False,
                 password_valid=False, passwords_match=False):
        """Обработка регистрации с валидацией"""

        # Проверяем валидацию каждого поля
        validation_errors = []

        if not name_valid or not name.strip():
            validation_errors.append("• ФИО должно содержать только буквы")

        if not phone_valid or len(phone) < 12:
            validation_errors.append("• Телефон должен быть в формате +79123456789 (минимум 11 цифр)")
        elif not phone.startswith('+'):
            phone = '+' + phone

        if not email_valid or '@' not in email or '.' not in email.split('@')[-1]:
            validation_errors.append("• Email должен содержать @ и домен (например, example@mail.ru)")

        if not password_valid or len(password) < 8:
            validation_errors.append("• Пароль должен быть не менее 8 символов")

        if not passwords_match:
            validation_errors.append("• Пароли не совпадают")

        # Если есть ошибки валидации
        if validation_errors:
            error_message = "Исправьте следующие ошибки:\n\n" + "\n".join(validation_errors)
            self.show_custom_message("Ошибка валидации", error_message)
            return

        # Все проверки пройдены
        self.show_custom_message("Успешно",
                                 f"Регистрация завершена!\nДобро пожаловать, {name}!",
                                 lambda: self.close_all_windows(window))

    def back_to_login(self, register_window):
        """Вернуться к окну входа"""
        register_window.destroy()
        self.open_login_window()

    def show_custom_message(self, title, message, callback=None):
        """Показать кастомное сообщение"""
        message_window = Toplevel(self.root)
        message_window.title(title)
        message_window.geometry("300x300")
        message_window.transient(self.root)
        message_window.resizable(False, False)

        # Делаем окно модальным
        message_window.grab_set()

        # Центрируем окно
        message_window.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - (300 // 2)
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - (150 // 2)
        message_window.geometry(f"+{x}+{y}")

        # Применяем тему
        self.apply_theme_to_window(message_window)

        # Заголовок с цветом в зависимости от типа сообщения
        color = self.colors['accent'] if "Успешно" in title or "Успех" in title else "#e74c3c"
        title_label = Label(message_window, text=title,
                            font=('Arial', 14, 'bold'),
                            fg=color,
                            bg=self.colors['bg'])
        title_label.pack(pady=(20, 10))

        # Сообщение
        message_label = Label(message_window, text=message,
                              font=('Arial', 10),
                              fg=self.colors['fg'],
                              bg=self.colors['bg'],
                              wraplength=250,
                              justify='center')
        message_label.pack(pady=(0, 20), padx=20)

        # Кнопка OK
        ok_btn = ttk.Button(message_window, text="OK",
                            style='Child.TButton',
                            command=lambda: self.close_message(message_window, callback))
        ok_btn.pack(pady=(0, 15))

        ok_btn.focus_set()
        message_window.bind('<Return>', lambda e: ok_btn.invoke())
        message_window.bind('<Escape>', lambda e: ok_btn.invoke())

    def close_message(self, message_window, callback=None):
        """Закрыть окно сообщения"""
        message_window.destroy()
        if callback:
            callback()

    def close_all_windows(self, *windows):
        """Закрыть несколько окон"""
        for window in windows:
            window.destroy()

    # ==================== ОКНО БРОНИРОВАНИЯ ====================
    def open_booking_window(self):
        """Окно бронирования услуг"""
        window = Toplevel(self.root)
        window.title("Бронирование услуг")
        window.geometry("600x500")
        window.transient(self.root)
        window.grab_set()

        # Применяем тему
        self.apply_theme_to_window(window)

        # Заголовок
        title_label = ttk.Label(window, text="Бронирование услуг",
                                font=('Arial', 16, 'bold'))
        title_label.pack(pady=20)

        # Контейнер формы
        form_frame = ttk.LabelFrame(window, text="Детали бронирования", padding=20)
        form_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

        # Объект
        ttk.Label(form_frame, text="Выберите объект:").grid(row=0, column=0, sticky=W, pady=10)
        facility_var = StringVar()
        facility_combo = ttk.Combobox(form_frame, textvariable=facility_var,
                                      values=['Бассейн', 'Легкоатлетический манеж',
                                              'Спортивный павильон', 'Лыжная база'],
                                      state='readonly', width=30, style='TCombobox')
        facility_combo.grid(row=0, column=1, pady=10, padx=(10, 0))
        facility_combo.set('Бассейн')

        # Тип услуги
        ttk.Label(form_frame, text="Тип услуги:").grid(row=1, column=0, sticky=W, pady=10)
        service_var = StringVar()
        service_combo = ttk.Combobox(form_frame, textvariable=service_var,
                                     state='readonly', width=30, style='TCombobox')
        service_combo.grid(row=1, column=1, pady=10, padx=(10, 0))
        service_combo['values'] = ['50-метровая дорожка', 'Детский бассейн', 'Аквааэробика']
        service_combo.set('50-метровая дорожка')

        # Дата
        ttk.Label(form_frame, text="Дата посещения:").grid(row=2, column=0, sticky=W, pady=10)
        date_entry = DateEntry(form_frame, width=28, style='TEntry',
                               background='darkblue', foreground='white',
                               date_pattern='dd.mm.yyyy')
        date_entry.grid(row=2, column=1, pady=10, padx=(10, 0), sticky=W)

        # Время
        ttk.Label(form_frame, text="Время:").grid(row=3, column=0, sticky=W, pady=10)
        time_var = StringVar()
        time_combo = ttk.Combobox(form_frame, textvariable=time_var,
                                  values=['07:00-09:00', '09:00-11:00', '11:00-13:00',
                                          '13:00-15:00', '15:00-17:00', '17:00-19:00',
                                          '19:00-21:00', '21:00-23:00'],
                                  state='readonly', width=30, style='TCombobox')
        time_combo.grid(row=3, column=1, pady=10, padx=(10, 0))
        time_combo.set('07:00-09:00')

        # Тип посещения
        ttk.Label(form_frame, text="Тип посещения:").grid(row=4, column=0, sticky=W, pady=10)
        type_var = StringVar(value='разовое')

        type_frame = ttk.Frame(form_frame)
        type_frame.grid(row=4, column=1, pady=10, padx=(10, 0), sticky=W)

        ttk.Radiobutton(type_frame, text="Разовое посещение",
                        variable=type_var, value='разовое').pack(side=LEFT, padx=(0, 20))
        ttk.Radiobutton(type_frame, text="По абонементу",
                        variable=type_var, value='абонемент').pack(side=LEFT)

        # Цена
        ttk.Label(form_frame, text="Стоимость:").grid(row=5, column=0, sticky=W, pady=20)
        price_label = ttk.Label(form_frame, text="500 руб.",
                                font=('Arial', 12, 'bold'),
                                foreground=self.colors['accent'])
        price_label.grid(row=5, column=1, pady=20, padx=(10, 0), sticky=W)

        # Кнопки
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=6, column=0, columnspan=2, pady=20)

        ttk.Button(button_frame, text="Забронировать",
                   command=lambda: self.create_booking(facility_var.get(), service_var.get(),
                                                       date_entry.get_date(), time_var.get(),
                                                       type_var.get(), window),
                   style='Child.TButton').pack(side=LEFT, padx=5)

        ttk.Button(button_frame, text="Очистить",
                   command=lambda: self.clear_booking_form(facility_combo, service_combo,
                                                           date_entry, time_combo, type_var,
                                                           price_label),
                   style='Child.TButton').pack(side=LEFT, padx=5)

    def create_booking(self, facility, service, date, time, booking_type, window):
        """Создание бронирования"""
        if not all([facility, service, time]):
            self.show_custom_message("Ошибка", "Заполните все поля")
            return

        price = "3000 руб." if booking_type == 'абонемент' else "500 руб."

        message = (f"Бронирование создано!\n\n"
                   f"Объект: {facility}\n"
                   f"Услуга: {service}\n"
                   f"Дата: {date.strftime('%d.%m.%Y')}\n"
                   f"Время: {time}\n"
                   f"Тип: {booking_type}\n"
                   f"Стоимость: {price}")

        self.show_custom_message("Успех", message, lambda: window.destroy())

    def clear_booking_form(self, facility_combo, service_combo, date_entry, time_combo, type_var, price_label):
        """Очистка формы бронирования"""
        facility_combo.set('')
        service_combo.set('')
        date_entry.set_date(datetime.now())
        time_combo.set('')
        type_var.set('разовое')
        price_label.config(text="0 руб.")

    # ==================== ОКНО МОИХ БРОНИРОВАНИЙ ====================
    def open_my_bookings_window(self):
        """Окно моих бронирований"""
        window = Toplevel(self.root)
        window.title("Мои бронирования")
        window.geometry("700x400")
        window.transient(self.root)
        window.grab_set()

        # Применяем тему
        self.apply_theme_to_window(window)

        # Заголовок
        ttk.Label(window, text="Мои бронирования",
                  font=('Arial', 16, 'bold')).pack(pady=10)

        # Панель управления
        control_frame = ttk.Frame(window)
        control_frame.pack(fill=X, padx=20, pady=10)

        ttk.Button(control_frame, text="Обновить список",
                   command=lambda: self.load_bookings_table(tree),
                   style='Child.TButton').pack(side=LEFT)

        ttk.Button(control_frame, text="Отменить выбранное",
                   command=lambda: self.cancel_booking(tree),
                   style='Child.TButton').pack(side=LEFT, padx=10)

        # Таблица
        columns = ('id', 'object', 'date', 'time', 'type', 'status', 'price')
        tree = ttk.Treeview(window, columns=columns, show='headings', height=10)

        # Настройка колонок
        tree.heading('id', text='№')
        tree.heading('object', text='Объект')
        tree.heading('date', text='Дата')
        tree.heading('time', text='Время')
        tree.heading('type', text='Тип')
        tree.heading('status', text='Статус')
        tree.heading('price', text='Цена')

        tree.column('id', width=50, anchor=CENTER)
        tree.column('object', width=120)
        tree.column('date', width=100)
        tree.column('time', width=100)
        tree.column('type', width=100)
        tree.column('status', width=100)
        tree.column('price', width=80)

        # Скроллбар
        scrollbar = ttk.Scrollbar(window, orient=VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        tree.pack(side=LEFT, fill=BOTH, expand=True, padx=(20, 0), pady=(0, 20))
        scrollbar.pack(side=RIGHT, fill=Y, pady=(0, 20))

        # Загружаем тестовые данные
        self.load_bookings_table(tree)

    def load_bookings_table(self, tree):
        """Загрузка данных в таблицу бронирований"""
        # Очищаем таблицу
        for item in tree.get_children():
            tree.delete(item)

        # Тестовые данные
        bookings = [
            (1, 'Бассейн', '25.12.2024', '09:00-11:00', 'разовое', 'подтверждено', '500 руб.'),
            (2, 'Легкоатлетический манеж', '26.12.2024', '14:00-16:00', 'абонемент', 'подтверждено', '2000 руб.'),
            (3, 'Спортивный павильон', '20.12.2024', '17:00-19:00', 'разовое', 'завершено', '400 руб.'),
            (4, 'Лыжная база', '27.12.2024', '10:00-12:00', 'абонемент', 'подтверждено', '2200 руб.')
        ]

        for booking in bookings:
            tree.insert('', END, values=booking)

    def cancel_booking(self, tree):
        """Отмена выбранного бронирования"""
        selected = tree.selection()
        if not selected:
            self.show_custom_message("Внимание", "Выберите бронирование для отмены")
            return

        def confirm_cancel():
            tree.delete(selected[0])
            self.show_custom_message("Успех", "Бронирование отменено")

        self.show_confirm_message("Подтверждение", "Отменить выбранное бронирование?", confirm_cancel)

    def show_confirm_message(self, title, message, callback):
        """Показать окно подтверждения"""
        confirm_window = Toplevel(self.root)
        confirm_window.title(title)
        confirm_window.geometry("350x180")
        confirm_window.transient(self.root)
        confirm_window.resizable(False, False)

        # Делаем окно модальным
        confirm_window.grab_set()

        # Центрируем окно
        confirm_window.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - (350 // 2)
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - (180 // 2)
        confirm_window.geometry(f"+{x}+{y}")

        # Применяем тему
        self.apply_theme_to_window(confirm_window)

        # Заголовок
        title_label = Label(confirm_window, text=title,
                            font=('Arial', 14, 'bold'),
                            fg=self.colors['fg'],
                            bg=self.colors['bg'])
        title_label.pack(pady=(20, 10))

        # Сообщение
        message_label = Label(confirm_window, text=message,
                              font=('Arial', 10),
                              fg=self.colors['fg'],
                              bg=self.colors['bg'],
                              wraplength=300,
                              justify='center')
        message_label.pack(pady=(0, 20))

        # Фрейм для кнопок
        button_frame = Frame(confirm_window, bg=self.colors['bg'])
        button_frame.pack(pady=(0, 15))

        # Кнопка "Да"
        yes_btn = ttk.Button(button_frame, text="Да",
                             style='Child.TButton',
                             command=lambda: [callback(), confirm_window.destroy()])
        yes_btn.pack(side=LEFT, padx=10)

        # Кнопка "Нет"
        no_btn = ttk.Button(button_frame, text="Нет",
                            style='Child.TButton',
                            command=confirm_window.destroy)
        no_btn.pack(side=LEFT, padx=10)

        no_btn.focus_set()
        confirm_window.bind('<Return>', lambda e: no_btn.invoke())  # Enter -> Нет
        confirm_window.bind('<Escape>', lambda e: no_btn.invoke())  # Escape -> Нет
        # Также привяжем клавишу 'y' для Да и 'n' для Нет
        confirm_window.bind('y', lambda e: yes_btn.invoke())
        confirm_window.bind('n', lambda e: no_btn.invoke())

    # ==================== ОКНО КОНТАКТОВ ====================
    def open_contacts_window(self):
        """Окно контактов"""
        window = Toplevel(self.root)
        window.title("Контакты")
        window.geometry("430x500")
        window.transient(self.root)
        window.grab_set()

        # Применяем тему
        self.apply_theme_to_window(window)

        # Заголовок
        ttk.Label(window, text="Контакты",
                  font=('Arial', 16, 'bold')).pack(pady=20)

        # Контейнер
        container = ttk.Frame(window, padding=20)
        container.pack(fill=BOTH, expand=True)

        # Контактная информация
        contacts = [
            ("📍  Адрес:", "г. Екатеринбург, ул. Краснофлотцев, 48"),
            ("📞  Телефон:", "+7 (343) 331-37-98 (приемная)"),
            ("📧  Email:", "info@калининец.екатеринбург.рф"),
            ("🌐  Сайт:", "https://калининец.екатеринбург.рф"),
            ("", ""),
            ("⏰ Режим работы:", "Ежедневно 7:00 - 23:00"),
            ("", "Администрация: Пн-Пт 9:00-18:00")
        ]

        for i, (label, value) in enumerate(contacts):
            if label:  # Пропускаем пустые строки
                ttk.Label(container, text=label, font=('Arial', 10, 'bold')).grid(row=i, column=0, sticky=W, pady=5)
                ttk.Label(container, text=value, font=('Arial', 10)).grid(row=i, column=1, sticky=W, pady=5,
                                                                          padx=(10, 0))
            else:
                # Пустая строка для разделения
                ttk.Label(container, text="").grid(row=i, column=0, pady=10)

        # Кнопки действий
        button_frame = ttk.Frame(window)
        button_frame.pack(pady=20)

        ttk.Button(button_frame, text="Открыть сайт",
                   command=lambda: webbrowser.open("https://калининец.екатеринбург.рф"),
                   style='Child.TButton').pack(side=LEFT, padx=5)

        ttk.Button(button_frame, text="Позвонить",
                   command=lambda: webbrowser.open("tel:+73433313798"),
                   style='Child.TButton').pack(side=LEFT, padx=5)

        ttk.Button(button_frame, text="Написать email",
                   command=lambda: webbrowser.open("mailto:info@калининец.екатеринбург.рф"),
                   style='Child.TButton').pack(side=LEFT, padx=5)

        # Карта (текстовая ссылка)
        map_frame = ttk.Frame(window)
        map_frame.pack(pady=10)

        ttk.Label(map_frame, text="Проложить маршрут:").pack(side=LEFT)
        map_link = Label(map_frame, text="Яндекс.Карты",
                            font=('Arial', 10, 'underline'),
                            fg=self.colors['link'],
                            bg=self.colors['bg'],
                            cursor='hand2')
        map_link.pack(side=LEFT, padx=(5, 0))
        map_link.bind('<Button-1>', lambda e: webbrowser.open("https://yandex.ru/maps/-/CDUbMFUP"))

    def run(self):
        """Запуск приложения"""
        self.root.mainloop()


# Запуск приложения
if __name__ == "__main__":
    app = SportsBookingClient()
    app.run()