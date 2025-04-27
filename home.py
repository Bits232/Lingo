import flet as ft
from database import load_lang, delete_lang
from data_loader import load_courses

home_ui_texts = {
    "english": {
        "welcome": "Welcome!",
        "select_category": "Select a Category",
    },
    "spanish": {
        "welcome": "¡Bienvenido!",
        "select_category": "Selecciona una categoría",
    },
    "yoruba": {
        "welcome": "Kaabo!",
        "select_category": "Yan Ẹ̀ka Kan",
    }
}

class HomePage(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.lang = load_lang()
        self.courses = load_courses(self.lang)
        self.texts = home_ui_texts.get(self.lang, home_ui_texts["english"])

    def build(self):
        course_widgets = []

        for category in self.courses:
            course_widgets.append(
                ft.Card(
                    content=ft.Container(
                        padding=10,
                        content=ft.Column([
                            ft.ListTile(
                                title=ft.Text(category["category"], weight='Bold'),
                                subtitle=ft.Text(f'Take {category["category"]} course here')
                            ),
                            ft.ElevatedButton('Take Course', on_click=lambda e, c=category: self.open_subcategory(c))
                        ])
                    )
                )
            )

        return ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(f"{self.texts['welcome']} ", weight="bold", size=18),
                        ft.IconButton(ft.icons.LANGUAGE, tooltip="Change Language", on_click=self.change_language)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Text(self.texts["select_category"], size=16, weight="bold"),
                ft.Column(course_widgets, scroll=ft.ScrollMode.AUTO)
            ],
            alignment=ft.MainAxisAlignment.START,
            expand=True
        )

    def open_subcategory(self, category_data):
        self.page.client_storage.set("category_data", category_data)
        self.page.go("/subcategory")

    def change_language(self, e):
        delete_lang()
        self.page.go("/")
