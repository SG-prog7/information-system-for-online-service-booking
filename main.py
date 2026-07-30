from tkinter import *
from tkinter import ttk, scrolledtext
import tkcalendar
from datetime import datetime
import webbrowser
import os

# Глобальные переменные
current_theme = 0
root = None
style = None
button_images = {}

# Цветовые схемы
light_theme = {
    'bg': '#ffffff',
    'fg': '#000080',
    'fg_secondary': '#7f8c8d',
    'button_bg': '#000080',
    'button_fg': 'white',
    'button_active': '#3498db',
    'accent': '#27ae60',
    'copyright': '#95a5a6',
    'window_bg': '#ffffff',
    'frame_bg': '#f8f9fa',
    'entry_bg': '#ffffff',
    'entry_fg': '#000080',
    'labelframe_bg': '#ffffff',
    'separator': '#dee2e6',
    'link': '#3498db'
}

dark_theme = {
    'bg': '#1a1a2e',
    'fg': '#e6e6e6',
    'fg_secondary': '#b0b0b0',
    'button_bg': '#3498db',
    'button_fg': 'white',
    'button_active': '#2980b9',
    'accent': '#27ae60',
    'copyright': '#7f8c8d',
    'window_bg': '#1a1a2e',
    'frame_bg': '#16213e',
    'entry_bg': '#2c3e50',
    'entry_fg': '#e6e6e6',
    'labelframe_bg': '#1a1a2e',
    'separator': '#34495e',
    'link': '#3498db'
}

colors = light_theme
theme_icons = {'light': "🌙", 'dark': "☀️"}


# Настройка стилей
def setup_styles():
    """Настройка стилей кнопок"""
    global style
    style = ttk.Style()
    style.theme_use('clam')
    update_styles()


def update_styles():
    """Обновление стилей в зависимости от темы"""
    global style, colors

    style.configure('.',
                    background=colors['bg'],
                    foreground=colors['fg'])

    style.configure('Menu.TButton',
                    font=('Arial', 12, 'bold'),
                    padding=15,
                    relief='flat',
                    background=colors['button_bg'],
                    foreground=colors['button_fg'],
                    borderwidth=0,
                    focuscolor='none')

    style.map('Menu.TButton',
              background=[('active', colors['button_active'])],
              foreground=[('active', 'white')])

    style.configure('Child.TButton',
                    font=('Arial', 12, 'bold'),
                    padding=10,
                    background=colors['button_bg'],
                    foreground=colors['button_fg'],
                    borderwidth=0)

    style.map('Child.TButton',
              background=[('active', colors['button_active'])],
              foreground=[('active', 'white')])

    style.configure('Treeview',
                    background=colors['window_bg'],
                    foreground=colors['fg'],
                    fieldbackground=colors['window_bg'],
                    borderwidth=0)

    style.configure('Treeview.Heading',
                    background=colors['frame_bg'],
                    foreground=colors['fg'],
                    borderwidth=0)

    style.configure('TEntry',
                    fieldbackground=colors['entry_bg'],
                    foreground=colors['entry_fg'],
                    insertcolor=colors['entry_fg'],
                    borderwidth=1,
                    relief='solid')

    style.map('TEntry',
              fieldbackground=[('active', colors['entry_bg'])],
              foreground=[('active', colors['entry_fg'])])

    style.configure('TCombobox',
                    fieldbackground=colors['entry_bg'],
                    foreground=colors['entry_fg'],
                    background=colors['entry_bg'],
                    borderwidth=1,
                    relief='solid')

    style.map('TCombobox',
              fieldbackground=[('active', colors['entry_bg'])],
              foreground=[('active', colors['entry_fg'])])

    style.configure('TFrame',
                    background=colors['bg'])

    style.configure('TLabelframe',
                    background=colors['labelframe_bg'],
                    foreground=colors['fg'],
                    borderwidth=1,
                    relief='solid')

    style.configure('TLabelframe.Label',
                    background=colors['labelframe_bg'],
                    foreground=colors['fg'])

    style.configure('TLabel',
                    background=colors['bg'],
                    foreground=colors['fg'])

    style.configure('TSeparator',
                    background=colors['separator'])


def create_text_button_image(key, filename):
    """Создание текстовой кнопки, если изображение не найдено"""
    global button_images, colors

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

    if '_n' in key:
        bg_color = colors['button_bg']
    else:
        bg_color = colors['button_active']

    img = PhotoImage(width=200, height=60)
    button_images[key] = img


def load_button_images():
    """Загрузка изображений для кнопок главного меню"""
    global button_images

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

    for key, filename in button_files:
        try:
            if os.path.exists(filename):
                button_images[key] = PhotoImage(file=filename)
            else:
                create_text_button_image(key, filename)
        except Exception as e:
            create_text_button_image(key, filename)


def toggle_theme():
    """Переключение темы"""
    global current_theme, colors, light_theme, dark_theme, theme_icons

    current_theme = 1 - current_theme

    if current_theme == 0:
        colors = light_theme
        theme_button.config(text=theme_icons['dark'])
    else:
        colors = dark_theme
        theme_button.config(text=theme_icons['light'])

    update_styles()
    apply_theme_to_window(root)

    for child in root.winfo_children():
        if isinstance(child, Toplevel):
            apply_theme_to_window(child)


def apply_theme_to_window(window):
    """Применение темы к окну и всем его виджетам"""
    global colors

    window.configure(bg=colors['bg'])
    apply_theme_to_widgets(window)


def apply_theme_to_widgets(parent):
    """Рекурсивное применение темы к виджетам"""
    global colors

    try:
        for widget in parent.winfo_children():
            widget_type = widget.winfo_class()

            if widget_type == 'Label':
                if widget.cget('text') == 'Добро пожаловать в Спортивный комплекс «Калининец»!':
                    widget.configure(bg=colors['bg'],
                                     fg=colors['fg'],
                                     font=('Cambria', 25))
                elif widget.cget('text') == "© 2025 СОК Калининец":
                    widget.configure(bg=colors['bg'],
                                     fg=colors['copyright'],
                                     font=('Arial', 12))
                else:
                    widget.configure(bg=colors['bg'],
                                     fg=colors['fg'])

            elif widget_type == 'Frame':
                if hasattr(widget, 'is_theme_frame'):
                    widget.configure(bg=colors['bg'])
                else:
                    widget.configure(bg=colors['frame_bg'])
                apply_theme_to_widgets(widget)

            elif widget_type == 'TFrame':
                widget.configure(style='TFrame')
                apply_theme_to_widgets(widget)

            elif widget_type == 'TLabelFrame':
                widget.configure(style='TLabelframe')
                apply_theme_to_widgets(widget)

            elif widget_type == 'TLabel':
                widget.configure(style='TLabel')

            elif widget_type == 'Button':
                if hasattr(widget, 'is_theme_button') and widget.is_theme_button:
                    widget.configure(bg=colors['bg'],
                                     fg=colors['fg'],
                                     activebackground=colors['bg'],
                                     activeforeground=colors['fg'])
                else:
                    if widget.cget('image'):
                        widget.configure(bg=colors['bg'],
                                         activebackground=colors['bg'])
                    else:
                        widget.configure(bg=colors['button_bg'],
                                         fg=colors['button_fg'],
                                         activebackground=colors['button_active'])

            elif widget_type == 'TButton':
                widget.configure(style='Child.TButton')

            elif widget_type == 'TEntry' or widget_type == 'TCombobox':
                widget.configure(style='TEntry')

            elif widget_type == 'Text' or widget_type == 'ScrolledText':
                widget.configure(bg=colors['entry_bg'],
                                 fg=colors['entry_fg'],
                                 insertbackground=colors['entry_fg'])

            elif widget_type == 'TSeparator':
                widget.configure(style='TSeparator')

            else:
                try:
                    apply_theme_to_widgets(widget)
                except:
                    pass

    except Exception as e:
        print(f"Ошибка при применении темы: {e}")


def create_image_buttons():
    """Создание кнопок с изображениями"""
    global button_images, colors, root

    if 'btn_n1' in button_images and 'btn_h1' in button_images:
        knopka1 = Button(root,
                         borderwidth=0,
                         bg=colors['bg'],
                         activebackground=colors['bg'],
                         image=button_images['btn_n1'],
                         command=open_login_window)
        knopka1.place(x=50, y=58)

        knopka1.bind('<Enter>', lambda e: knopka1.config(image=button_images['btn_h1']))
        knopka1.bind('<Leave>', lambda e: knopka1.config(image=button_images['btn_n1']))
    else:
        knopka1 = Button(root,
                         text="Вход / Регистрация",
                         bg=colors['button_bg'],
                         fg=colors['button_fg'],
                         activebackground=colors['button_active'],
                         font=('Arial', 14, 'bold'),
                         command=open_login_window)
        knopka1.place(x=50, y=58, width=200, height=60)

    if 'btn_n2' in button_images and 'btn_h2' in button_images:
        knopka2 = Button(root,
                         borderwidth=0,
                         bg=colors['bg'],
                         activebackground=colors['bg'],
                         image=button_images['btn_n2'],
                         command=open_booking_window)
        knopka2.place(x=360, y=58)

        knopka2.bind('<Enter>', lambda e: knopka2.config(image=button_images['btn_h2']))
        knopka2.bind('<Leave>', lambda e: knopka2.config(image=button_images['btn_n2']))
    else:
        knopka2 = Button(root,
                         text="Бронирование услуг",
                         bg=colors['button_bg'],
                         fg=colors['button_fg'],
                         activebackground=colors['button_active'],
                         font=('Arial', 14, 'bold'),
                         command=open_booking_window)
        knopka2.place(x=360, y=58, width=200, height=60)

    if 'btn_n3' in button_images and 'btn_h3' in button_images:
        knopka3 = Button(root,
                         borderwidth=0,
                         bg=colors['bg'],
                         activebackground=colors['bg'],
                         image=button_images['btn_n3'],
                         command=open_my_bookings_window)
        knopka3.place(x=670, y=58)

        knopka3.bind('<Enter>', lambda e: knopka3.config(image=button_images['btn_h3']))
        knopka3.bind('<Leave>', lambda e: knopka3.config(image=button_images['btn_n3']))
    else:
        knopka3 = Button(root,
                         text="Мои бронирования",
                         bg=colors['button_bg'],
                         fg=colors['button_fg'],
                         activebackground=colors['button_active'],
                         font=('Arial', 14, 'bold'),
                         command=open_my_bookings_window)
        knopka3.place(x=670, y=58, width=200, height=60)

    if 'btn_n4' in button_images and 'btn_h4' in button_images:
        knopka4 = Button(root,
                         borderwidth=0,
                         bg=colors['bg'],
                         activebackground=colors['bg'],
                         image=button_images['btn_n4'],
                         command=open_contacts_window)
        knopka4.place(x=980, y=58)

        knopka4.bind('<Enter>', lambda e: knopka4.config(image=button_images['btn_h4']))
        knopka4.bind('<Leave>', lambda e: knopka4.config(image=button_images['btn_n4']))
    else:
        knopka4 = Button(root,
                         text="Контакты",
                         bg=colors['button_bg'],
                         fg=colors['button_fg'],
                         activebackground=colors['button_active'],
                         font=('Arial', 14, 'bold'),
                         command=open_contacts_window)
        knopka4.place(x=980, y=58, width=200, height=60)


def create_main_menu_with_images():
    """Создание главного меню с кнопками-изображениями"""
    global root, colors, theme_icons, theme_button

    root.configure(bg=colors['bg'])

    title_label = Label(root,
                        text='Спортивно-оздоровительный комплекс «Калининец»',
                        font=('Cambria', 25),
                        bg=colors['bg'],
                        fg=colors['fg'])
    title_label.place(x=200, y=10)

    theme_frame = Frame(root, bg=colors['bg'])
    theme_frame.is_theme_frame = True
    theme_frame.place(x=1200, y=10, width=100, height=50)

    theme_button = Button(theme_frame,
                          text=theme_icons['dark'],
                          font=('Arial', 16),
                          bg=colors['bg'],
                          fg=colors['fg'],
                          borderwidth=0,
                          activebackground=colors['bg'],
                          activeforeground=colors['fg'],
                          command=toggle_theme)
    theme_button.is_theme_button = True
    theme_button.pack(side=RIGHT)

    about_text = """Один из наиболее мощных спортивных комплексов города Екатеринбурга — спорткомплекс «Калининец» создавался в конце 70-х годов. До 1994 года он принадлежал машиностроительному заводу имени М.И. Калинина, а в настоящее время является муниципальной собственностью города. Ежедневно сооружения спорткомплекса посещают 1500-2000 человек.

В состав комплекса входят:
• 50-метровый бассейн с артезианской водой
• Легкоатлетический манеж с 200-метровой дорожкой
• Спортивный павильон с залами единоборств
• Лыжная база с трассами 2-10 км
• Стадион с искусственным покрытием
• Стрелковый тир

СК «Калининец» — самый большой по площади спортивно-оздоровительный комплекс Уральского региона, являющийся одной из тренировочных баз ЧМ-2018 по футболу, расположенный в лесопарковой зоне города."""

    text_widget = Text(root, height=15, width=110, wrap=WORD,
                       font=("Arial", 14),
                       bg=colors['bg'],
                       fg=colors['fg'],
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

    text_widget_1 = Text(root, height=7, width=40, wrap=WORD,
                         font=("Arial", 14),
                         bg=colors['bg'],
                         fg=colors['fg'],
                         relief=FLAT,
                         borderwidth=0,
                         padx=10,
                         pady=10)
    text_widget_1.insert(1.0, about_text_1)
    text_widget_1.config(state=DISABLED)
    text_widget_1.place(x=757, y=456)

    create_image_buttons()

    copyright_label = Label(root,
                            text="© 2026 СОК Калининец",
                            font=('Arial', 12),
                            fg=colors['copyright'],
                            bg=colors['bg'])
    copyright_label.place(x=580, y=730)


# ==================== ОКНО ВХОДА / РЕГИСТРАЦИИ ====================
def open_login_window():
    """Окно входа и регистрации"""
    global root, colors

    window = Toplevel(root)
    window.title("Вход / Регистрация")
    window.geometry("400x450")
    window.transient(root)
    window.grab_set()

    apply_theme_to_window(window)

    title_label = ttk.Label(window,
                            text="Вход в систему",
                            font=('Arial', 14, 'bold'))
    title_label.pack(pady=20)

    form_frame = ttk.LabelFrame(window, text="Данные для входа", padding=20)
    form_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

    email_label = ttk.Label(form_frame, text="Email:")
    email_label.grid(row=0, column=0, sticky=W, pady=(10, 0))
    email_entry = ttk.Entry(form_frame, width=30, style='TEntry')
    email_entry.grid(row=0, column=1, pady=(10, 0), padx=(10, 0))

    password_label = ttk.Label(form_frame, text="Пароль:")
    password_label.grid(row=1, column=0, sticky=W, pady=10)
    password_entry = ttk.Entry(form_frame, width=30, show='*', style='TEntry')
    password_entry.grid(row=1, column=1, pady=10, padx=(10, 0))

    button_frame = ttk.Frame(form_frame)
    button_frame.grid(row=2, column=0, columnspan=2, pady=20)

    login_btn = ttk.Button(button_frame, text="Войти",
                           command=lambda: login(email_entry.get(), password_entry.get()),
                           style='Child.TButton')
    login_btn.pack(side=LEFT, padx=5)

    clear_btn = ttk.Button(button_frame, text="Очистить",
                           command=lambda: clear_login_form(email_entry, password_entry),
                           style='Child.TButton')
    clear_btn.pack(side=LEFT, padx=5)

    separator = ttk.Separator(window, orient='horizontal')
    separator.pack(fill=X, padx=20, pady=10)

    register_frame = ttk.Frame(window, padding=10)
    register_frame.pack(fill=X)

    no_account_label = ttk.Label(register_frame, text="Нет аккаунта?")
    no_account_label.pack(side=LEFT, padx=(0, 10))

    register_btn = ttk.Button(register_frame, text="Зарегистрироваться",
                              command=lambda: open_register_window(window),
                              style='Child.TButton')
    register_btn.pack(side=LEFT)


def clear_login_form(email_entry, password_entry):
    """Очистка формы входа"""
    email_entry.delete(0, END)
    password_entry.delete(0, END)


def login(email, password):
    """Обработка входа"""
    if not email or not password:
        show_custom_message("Ошибка", "Заполните все поля")
        return

    if email == "test@example.com" and password == "password":
        show_custom_message("Успешно", "Вход выполнен успешно!")
    else:
        show_custom_message("Ошибка", "Неверный email или пароль")


def open_register_window(parent_window):
    """Открыть окно регистрации"""
    global root, colors

    parent_window.destroy()

    window = Toplevel(root)
    window.title("Регистрация")
    window.geometry("600x520")
    window.transient(root)
    window.grab_set()

    apply_theme_to_window(window)

    title_label = ttk.Label(window,
                            text="Регистрация",
                            font=('Arial', 14, 'bold'))
    title_label.pack(pady=20)

    form_frame = ttk.LabelFrame(window, text="Данные для регистрации", padding=20)
    form_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

    def validate_name(text):
        if text == "":
            return True
        for char in text:
            if not (char.isalpha() or char in " -'"):
                return False
        return True

    def validate_phone(text):
        if text == "":
            return True
        if text.startswith('+'):
            return text[1:].isdigit()
        else:
            if text.isdigit():
                return True
            return False

    def validate_email(text):
        if text == "":
            return True
        return '@' in text

    def validate_password(text):
        if text == "":
            return True
        return len(text) >= 8

    def on_name_change(var_name, index, mode):
        current_text = name_var.get()
        if not validate_name(current_text) and current_text:
            name_var.set(current_text[:-1])

    def on_phone_change(var_name, index, mode):
        current_text = phone_var.get()
        if not validate_phone(current_text) and current_text:
            phone_var.set(current_text[:-1])
        elif current_text.isdigit() and len(current_text) > 0:
            phone_var.set('+' + current_text)

    name_var = StringVar()
    phone_var = StringVar()
    email_var = StringVar()
    password_var = StringVar()
    confirm_password_var = StringVar()

    name_var.trace('w', on_name_change)
    phone_var.trace('w', on_phone_change)

    name_label = ttk.Label(form_frame, text="ФИО:")
    name_label.grid(row=0, column=0, sticky=W, pady=(5, 0))
    name_entry = ttk.Entry(form_frame, width=30, textvariable=name_var, style='TEntry')
    name_entry.grid(row=0, column=1, pady=(5, 0), padx=(10, 0))
    ttk.Label(form_frame, text="только буквы и пробелы",
              font=('Arial', 8), foreground=colors['fg_secondary']
              ).grid(row=0, column=2, padx=(5, 0), pady=(5, 0), sticky=W)

    phone_label = ttk.Label(form_frame, text="Телефон:")
    phone_label.grid(row=1, column=0, sticky=W, pady=10)
    phone_entry = ttk.Entry(form_frame, width=30, textvariable=phone_var, style='TEntry')
    phone_entry.grid(row=1, column=1, pady=10, padx=(10, 0))
    ttk.Label(form_frame, text="формат: +79123456789",
              font=('Arial', 8), foreground=colors['fg_secondary']
              ).grid(row=1, column=2, padx=(5, 0), pady=10, sticky=W)

    email_label = ttk.Label(form_frame, text="Email:")
    email_label.grid(row=2, column=0, sticky=W, pady=10)
    email_entry = ttk.Entry(form_frame, width=30, textvariable=email_var, style='TEntry')
    email_entry.grid(row=2, column=1, pady=10, padx=(10, 0))
    ttk.Label(form_frame, text="должен содержать @",
              font=('Arial', 8), foreground=colors['fg_secondary']
              ).grid(row=2, column=2, padx=(5, 0), pady=10, sticky=W)

    password_label = ttk.Label(form_frame, text="Пароль:")
    password_label.grid(row=3, column=0, sticky=W, pady=10)
    password_entry = ttk.Entry(form_frame, width=30, show='*',
                               textvariable=password_var, style='TEntry')
    password_entry.grid(row=3, column=1, pady=10, padx=(10, 0))
    ttk.Label(form_frame, text="минимум 8 символов",
              font=('Arial', 8), foreground=colors['fg_secondary']
              ).grid(row=3, column=2, padx=(5, 0), pady=10, sticky=W)

    confirm_label = ttk.Label(form_frame, text="Подтвердите пароль:")
    confirm_label.grid(row=4, column=0, sticky=W, pady=10)
    confirm_password_entry = ttk.Entry(form_frame, width=30, show='*',
                                       textvariable=confirm_password_var, style='TEntry')
    confirm_password_entry.grid(row=4, column=1, pady=10, padx=(10, 0))

    validation_frame = ttk.Frame(form_frame)
    validation_frame.grid(row=5, column=0, columnspan=3, pady=(10, 0), sticky=W)

    name_valid = BooleanVar(value=False)
    phone_valid = BooleanVar(value=False)
    email_valid = BooleanVar(value=False)
    password_valid = BooleanVar(value=False)
    passwords_match = BooleanVar(value=False)

    def update_validation_indicators():
        name = name_var.get()
        phone = phone_var.get()
        email = email_var.get()
        password = password_var.get()
        confirm_password = confirm_password_var.get()

        name_valid.set(validate_name(name) and len(name.strip()) >= 2)
        phone_valid.set(validate_phone(phone) and len(phone) >= 12)
        email_valid.set(validate_email(email) and len(email) >= 5)
        password_valid.set(validate_password(password))
        passwords_match.set(password == confirm_password and password != "")

    for var in [name_var, phone_var, email_var, password_var, confirm_password_var]:
        var.trace('w', lambda *args: update_validation_indicators())

    update_validation_indicators()

    button_frame = ttk.Frame(form_frame)
    button_frame.grid(row=6, column=0, columnspan=2, pady=20)

    register_btn = ttk.Button(button_frame, text="Зарегистрироваться",
                              command=lambda: register_func(
                                  name_var.get(), phone_var.get(),
                                  email_var.get(), password_var.get(),
                                  confirm_password_var.get(), window,
                                  name_valid.get(), phone_valid.get(),
                                  email_valid.get(), password_valid.get(),
                                  passwords_match.get()),
                              style='Child.TButton')
    register_btn.pack(side=LEFT, padx=5)

    clear_btn = ttk.Button(button_frame, text="Очистить",
                           command=lambda: clear_register_form(
                               name_var, phone_var, email_var,
                               password_var, confirm_password_var),
                           style='Child.TButton')
    clear_btn.pack(side=LEFT, padx=5)

    back_frame = ttk.Frame(window, padding=10)
    back_frame.pack(fill=X)

    back_btn = ttk.Button(back_frame, text="Назад к входу",
                          command=lambda: back_to_login(window),
                          style='Child.TButton')
    back_btn.pack()


def clear_register_form(name_var, phone_var, email_var, password_var, confirm_password_var):
    """Очистка формы регистрации"""
    name_var.set('')
    phone_var.set('')
    email_var.set('')
    password_var.set('')
    confirm_password_var.set('')


def register_func(name, phone, email, password, confirm_password, window,
                  name_valid=False, phone_valid=False, email_valid=False,
                  password_valid=False, passwords_match=False):
    """Обработка регистрации с валидацией"""

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

    if validation_errors:
        error_message = "Исправьте следующие ошибки:\n\n" + "\n".join(validation_errors)
        show_custom_message("Ошибка валидации", error_message)
        return

    show_custom_message("Успешно",
                        f"Регистрация завершена!\nДобро пожаловать, {name}!",
                        lambda: close_all_windows(window))


def back_to_login(register_window):
    """Вернуться к окну входа"""
    register_window.destroy()
    open_login_window()


def show_custom_message(title, message, callback=None):
    """Показать кастомное сообщение"""
    global root, colors

    message_window = Toplevel(root)
    message_window.title(title)
    message_window.geometry("300x300")
    message_window.transient(root)
    message_window.resizable(False, False)
    message_window.grab_set()

    message_window.update_idletasks()
    x = root.winfo_x() + (root.winfo_width() // 2) - (300 // 2)
    y = root.winfo_y() + (root.winfo_height() // 2) - (150 // 2)
    message_window.geometry(f"+{x}+{y}")

    apply_theme_to_window(message_window)

    color = colors['accent'] if "Успешно" in title or "Успех" in title else "#e74c3c"
    title_label = Label(message_window, text=title,
                        font=('Arial', 14, 'bold'),
                        fg=color,
                        bg=colors['bg'])
    title_label.pack(pady=(20, 10))

    message_label = Label(message_window, text=message,
                          font=('Arial', 10),
                          fg=colors['fg'],
                          bg=colors['bg'],
                          wraplength=250,
                          justify='center')
    message_label.pack(pady=(0, 20), padx=20)

    ok_btn = ttk.Button(message_window, text="OK",
                        style='Child.TButton',
                        command=lambda: close_message(message_window, callback))
    ok_btn.pack(pady=(0, 15))

    ok_btn.focus_set()
    message_window.bind('<Return>', lambda e: ok_btn.invoke())
    message_window.bind('<Escape>', lambda e: ok_btn.invoke())


def close_message(message_window, callback=None):
    """Закрыть окно сообщения"""
    message_window.destroy()
    if callback:
        callback()


def close_all_windows(*windows):
    """Закрыть несколько окон"""
    for window in windows:
        window.destroy()


# ==================== ОКНО БРОНИРОВАНИЯ ====================
def open_booking_window():
    """Окно бронирования услуг"""
    global root, colors

    window = Toplevel(root)
    window.title("Бронирование услуг")
    window.geometry("600x500")
    window.transient(root)
    window.grab_set()

    apply_theme_to_window(window)

    title_label = ttk.Label(window, text="Бронирование услуг",
                            font=('Arial', 16, 'bold'))
    title_label.pack(pady=20)

    form_frame = ttk.LabelFrame(window, text="Детали бронирования", padding=20)
    form_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

    ttk.Label(form_frame, text="Выберите объект:").grid(row=0, column=0, sticky=W, pady=10)
    facility_var = StringVar()
    facility_combo = ttk.Combobox(form_frame, textvariable=facility_var,
                                  values=['Бассейн', 'Легкоатлетический манеж',
                                          'Спортивный павильон', 'Лыжная база'],
                                  state='readonly', width=30, style='TCombobox')
    facility_combo.grid(row=0, column=1, pady=10, padx=(10, 0))
    facility_combo.set('Бассейн')

    ttk.Label(form_frame, text="Тип услуги:").grid(row=1, column=0, sticky=W, pady=10)
    service_var = StringVar()
    service_combo = ttk.Combobox(form_frame, textvariable=service_var,
                                 state='readonly', width=30, style='TCombobox')
    service_combo.grid(row=1, column=1, pady=10, padx=(10, 0))
    service_combo['values'] = ['50-метровая дорожка', 'Детский бассейн', 'Аквааэробика']
    service_combo.set('50-метровая дорожка')

    ttk.Label(form_frame, text="Дата посещения:").grid(row=2, column=0, sticky=W, pady=10)
    date_entry = DateEntry(form_frame, width=28, style='TEntry',
                           background='darkblue', foreground='white',
                           date_pattern='dd.mm.yyyy')
    date_entry.grid(row=2, column=1, pady=10, padx=(10, 0), sticky=W)

    ttk.Label(form_frame, text="Время:").grid(row=3, column=0, sticky=W, pady=10)
    time_var = StringVar()
    time_combo = ttk.Combobox(form_frame, textvariable=time_var,
                              values=['07:00-09:00', '09:00-11:00', '11:00-13:00',
                                      '13:00-15:00', '15:00-17:00', '17:00-19:00',
                                      '19:00-21:00', '21:00-23:00'],
                              state='readonly', width=30, style='TCombobox')
    time_combo.grid(row=3, column=1, pady=10, padx=(10, 0))
    time_combo.set('07:00-09:00')

    ttk.Label(form_frame, text="Тип посещения:").grid(row=4, column=0, sticky=W, pady=10)
    type_var = StringVar(value='разовое')

    type_frame = ttk.Frame(form_frame)
    type_frame.grid(row=4, column=1, pady=10, padx=(10, 0), sticky=W)

    ttk.Radiobutton(type_frame, text="Разовое посещение",
                    variable=type_var, value='разовое').pack(side=LEFT, padx=(0, 20))
    ttk.Radiobutton(type_frame, text="По абонементу",
                    variable=type_var, value='абонемент').pack(side=LEFT)

    ttk.Label(form_frame, text="Стоимость:").grid(row=5, column=0, sticky=W, pady=20)
    price_label = ttk.Label(form_frame, text="500 руб.",
                            font=('Arial', 12, 'bold'),
                            foreground=colors['accent'])
    price_label.grid(row=5, column=1, pady=20, padx=(10, 0), sticky=W)

    button_frame = ttk.Frame(form_frame)
    button_frame.grid(row=6, column=0, columnspan=2, pady=20)

    ttk.Button(button_frame, text="Забронировать",
               command=lambda: create_booking(facility_var.get(), service_var.get(),
                                              date_entry.get_date(), time_var.get(),
                                              type_var.get(), window),
               style='Child.TButton').pack(side=LEFT, padx=5)

    ttk.Button(button_frame, text="Очистить",
               command=lambda: clear_booking_form(facility_combo, service_combo,
                                                  date_entry, time_combo, type_var,
                                                  price_label),
               style='Child.TButton').pack(side=LEFT, padx=5)


def create_booking(facility, service, date, time, booking_type, window):
    """Создание бронирования"""
    if not all([facility, service, time]):
        show_custom_message("Ошибка", "Заполните все поля")
        return

    price = "3000 руб." if booking_type == 'абонемент' else "500 руб."

    message = (f"Бронирование создано!\n\n"
               f"Объект: {facility}\n"
               f"Услуга: {service}\n"
               f"Дата: {date.strftime('%d.%m.%Y')}\n"
               f"Время: {time}\n"
               f"Тип: {booking_type}\n"
               f"Стоимость: {price}")

    show_custom_message("Успех", message, lambda: window.destroy())


def clear_booking_form(facility_combo, service_combo, date_entry, time_combo, type_var, price_label):
    """Очистка формы бронирования"""
    facility_combo.set('')
    service_combo.set('')
    date_entry.set_date(datetime.now())
    time_combo.set('')
    type_var.set('разовое')
    price_label.config(text="0 руб.")


# ==================== ОКНО МОИХ БРОНИРОВАНИЙ ====================
def open_my_bookings_window():
    """Окно моих бронирований"""
    global root, colors

    window = Toplevel(root)
    window.title("Мои бронирования")
    window.geometry("700x400")
    window.transient(root)
    window.grab_set()

    apply_theme_to_window(window)

    ttk.Label(window, text="Мои бронирования",
              font=('Arial', 16, 'bold')).pack(pady=10)

    control_frame = ttk.Frame(window)
    control_frame.pack(fill=X, padx=20, pady=10)

    ttk.Button(control_frame, text="Обновить список",
               command=lambda: load_bookings_table(tree),
               style='Child.TButton').pack(side=LEFT)

    ttk.Button(control_frame, text="Отменить выбранное",
               command=lambda: cancel_booking(tree),
               style='Child.TButton').pack(side=LEFT, padx=10)

    columns = ('id', 'object', 'date', 'time', 'type', 'status', 'price')
    tree = ttk.Treeview(window, columns=columns, show='headings', height=10)

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

    scrollbar = ttk.Scrollbar(window, orient=VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    tree.pack(side=LEFT, fill=BOTH, expand=True, padx=(20, 0), pady=(0, 20))
    scrollbar.pack(side=RIGHT, fill=Y, pady=(0, 20))

    load_bookings_table(tree)


def load_bookings_table(tree):
    """Загрузка данных в таблицу бронирований"""
    for item in tree.get_children():
        tree.delete(item)

    bookings = [
        (1, 'Бассейн', '25.12.2024', '09:00-11:00', 'разовое', 'подтверждено', '500 руб.'),
        (2, 'Легкоатлетический манеж', '26.12.2024', '14:00-16:00', 'абонемент', 'подтверждено', '2000 руб.'),
        (3, 'Спортивный павильон', '20.12.2024', '17:00-19:00', 'разовое', 'завершено', '400 руб.'),
        (4, 'Лыжная база', '27.12.2024', '10:00-12:00', 'абонемент', 'подтверждено', '2200 руб.')
    ]

    for booking in bookings:
        tree.insert('', END, values=booking)


def cancel_booking(tree):
    """Отмена выбранного бронирования"""
    selected = tree.selection()
    if not selected:
        show_custom_message("Внимание", "Выберите бронирование для отмены")
        return

    def confirm_cancel():
        tree.delete(selected[0])
        show_custom_message("Успех", "Бронирование отменено")

    show_confirm_message("Подтверждение", "Отменить выбранное бронирование?", confirm_cancel)


def show_confirm_message(title, message, callback):
    """Показать окно подтверждения"""
    global root, colors

    confirm_window = Toplevel(root)
    confirm_window.title(title)
    confirm_window.geometry("350x180")
    confirm_window.transient(root)
    confirm_window.resizable(False, False)
    confirm_window.grab_set()

    confirm_window.update_idletasks()
    x = root.winfo_x() + (root.winfo_width() // 2) - (350 // 2)
    y = root.winfo_y() + (root.winfo_height() // 2) - (180 // 2)
    confirm_window.geometry(f"+{x}+{y}")

    apply_theme_to_window(confirm_window)

    title_label = Label(confirm_window, text=title,
                        font=('Arial', 14, 'bold'),
                        fg=colors['fg'],
                        bg=colors['bg'])
    title_label.pack(pady=(20, 10))

    message_label = Label(confirm_window, text=message,
                          font=('Arial', 10),
                          fg=colors['fg'],
                          bg=colors['bg'],
                          wraplength=300,
                          justify='center')
    message_label.pack(pady=(0, 20))

    button_frame = Frame(confirm_window, bg=colors['bg'])
    button_frame.pack(pady=(0, 15))

    yes_btn = ttk.Button(button_frame, text="Да",
                         style='Child.TButton',
                         command=lambda: [callback(), confirm_window.destroy()])
    yes_btn.pack(side=LEFT, padx=10)

    no_btn = ttk.Button(button_frame, text="Нет",
                        style='Child.TButton',
                        command=confirm_window.destroy)
    no_btn.pack(side=LEFT, padx=10)

    no_btn.focus_set()
    confirm_window.bind('<Return>', lambda e: no_btn.invoke())
    confirm_window.bind('<Escape>', lambda e: no_btn.invoke())
    confirm_window.bind('y', lambda e: yes_btn.invoke())
    confirm_window.bind('n', lambda e: no_btn.invoke())


# ==================== ОКНО КОНТАКТОВ ====================
def open_contacts_window():
    """Окно контактов"""
    global root, colors

    window = Toplevel(root)
    window.title("Контакты")
    window.geometry("430x500")
    window.transient(root)
    window.grab_set()

    apply_theme_to_window(window)

    ttk.Label(window, text="Контакты",
              font=('Arial', 16, 'bold')).pack(pady=20)

    container = ttk.Frame(window, padding=20)
    container.pack(fill=BOTH, expand=True)

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
        if label:
            ttk.Label(container, text=label, font=('Arial', 10, 'bold')).grid(row=i, column=0, sticky=W, pady=5)
            ttk.Label(container, text=value, font=('Arial', 10)).grid(row=i, column=1, sticky=W, pady=5,
                                                                      padx=(10, 0))
        else:
            ttk.Label(container, text="").grid(row=i, column=0, pady=10)

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

    map_frame = ttk.Frame(window)
    map_frame.pack(pady=10)

    ttk.Label(map_frame, text="Проложить маршрут:").pack(side=LEFT)
    map_link = Label(map_frame, text="Яндекс.Карты",
                     font=('Arial', 10, 'underline'),
                     fg=colors['link'],
                     bg=colors['bg'],
                     cursor='hand2')
    map_link.pack(side=LEFT, padx=(5, 0))
    map_link.bind('<Button-1>', lambda e: webbrowser.open("https://yandex.ru/maps/-/CDUbMFUP"))


# ==================== ЗАПУСК ПРИЛОЖЕНИЯ ====================
def main():
    """Основная функция запуска приложения"""
    global root, current_theme, colors, light_theme, theme_icons, theme_button

    root = Tk()
    root.title("СОК «Калининец» - Онлайн-бронирование")
    root.geometry("1348x780")
    root.resizable(False, False)

    current_theme = 0
    colors = light_theme

    setup_styles()
    load_button_images()
    create_main_menu_with_images()

    root.mainloop()


# Запуск приложения
if __name__ == "__main__":
    main()